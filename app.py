import os
import json
import uuid
import boto3
import base64
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- AWS & Roboflow Configuration ---
ROBOFLOW_API_KEY = os.environ.get('ROBOFLOW_API_KEY', "EqOaPy7RBc9rLyxKOJYM")
ROBOFLOW_PROJECT = "yolo-waste-detection"
AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')

# Initialize Bedrock client
bedrock_runtime = boto3.client(
    'bedrock-runtime', 
    region_name=AWS_DEFAULT_REGION
)

ROBOFLOW_API_URL = f"https://detect.roboflow.com/{ROBOFLOW_PROJECT}/1"

# Store conversation sessions
conversation_sessions = {}

class BedrockChatbot:
    def __init__(self):
        # Using a powerful, widely available multimodal model.
        # You MUST request access to this model in the Bedrock console (us-east-1).
        self.model_id = "amazon.nova-pro-v1:0"
    
    def get_initial_analysis(self, image_bytes, object_detected):
        prompt = f"""
        An object has been identified as '{object_detected}'. 
        Look at the image and provide a brief, engaging, one-sentence introduction 
        inviting the user to ask you more about this item. For example: 
        'This looks like a {object_detected}. Ask me how to recycle it!'
        """
        return self._call_bedrock_multimodal(prompt, image_bytes)

    def get_chat_response(self, user_question, image_bytes, context):
        prompt = f"""
        Here is the context of our conversation so far: {context}
        The user's new question is: "{user_question}"
        Please answer the question, referring to the image if it's relevant.
        """
        return self._call_bedrock_multimodal(prompt, image_bytes)

    def _call_bedrock_multimodal(self, prompt, image_bytes):
        """Correctly calls the Bedrock Converse API for multimodal chat."""
        try:
            message = {
                "role": "user",
                "content": [
                    {"text": prompt},
                    {"image": {"format": "jpeg", "source": {"bytes": image_bytes}}}
                ]
            }
            response = bedrock_runtime.converse(
                modelId=self.model_id,
                messages=[message],
                inferenceConfig={"maxTokens": 2000, "temperature": 0.7}
            )
            return response['output']['message']['content'][0]['text']
        except Exception as e:
            print(f"Bedrock API Error: {str(e)}")
            if "AccessDeniedException" in str(e):
                return "Error: Access to the Bedrock model has been denied. Please ensure you have requested access to Anthropic Claude 3 Sonnet in the us-east-1 region."
            return f"AI analysis is temporarily unavailable: {str(e)}"

chatbot = BedrockChatbot()

@app.route('/')
def index():
    return render_template('waste_sorter.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        image_bytes = file.read()
        
        # We need the base64 string for Roboflow
        image_for_roboflow = base64.b64encode(image_bytes).decode('utf-8')

        # Roboflow detection
        params = {"api_key": ROBOFLOW_API_KEY}
        response = requests.post(
            ROBOFLOW_API_URL, params=params, data=image_for_roboflow,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        response.raise_for_status()
        results = response.json()
        
        predictions = results.get('predictions', [])
        best_prediction = max(predictions, key=lambda p: p['confidence']) if predictions else None

        if best_prediction and best_prediction['confidence'] > 0.3:
            object_class = best_prediction['class']
            
            # Get the initial conversational intro from Bedrock
            bedrock_intro = chatbot.get_initial_analysis(image_bytes, object_class)
            
            session_id = str(uuid.uuid4())
            conversation_sessions[session_id] = {
                'object': object_class,
                'image_bytes': image_bytes
            }
            
            return jsonify({
                'success': True, 
                'prediction': object_class, 
                'bedrock_intro': bedrock_intro, 
                'session_id': session_id
            })
        
        return jsonify({'success': False, 'message': 'No objects detected with high confidence.'})
    except Exception as e:
        return jsonify({'success': False, 'error': f'An error occurred: {str(e)}'})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        session_id = data.get('session_id')
        user_question = data.get('question')

        if session_id not in conversation_sessions:
            return jsonify({'success': False, 'message': 'Session expired.'})

        context = conversation_sessions[session_id]
        context_str = f"The detected object is a {context['object']}."
        
        ai_response = chatbot.get_chat_response(
            user_question, context['image_bytes'], context_str
        )
        return jsonify({'success': True, 'answer': ai_response})
    except Exception as e:
        return jsonify({'success': False, 'error': f'Chat failed: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

