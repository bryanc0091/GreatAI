Smart Waste Sorter ft. Amazon Bedrock
This is an advanced AI-powered web application designed to help users correctly identify and sort waste. It uses a multi-AI architecture, leveraging Roboflow for fast, accurate object detection and Amazon Bedrock for intelligent, conversational follow-up and detailed analysis.
Features
Multi-Modal Input: Classify waste using either a live camera feed or by uploading an image.
High-Accuracy Detection: Powered by a Roboflow YOLO model trained on 42 specific waste classes.
Detailed Disposal Tips: Provides immediate, specific instructions for how to dispose of each of the 42 detected items.
Conversational AI Assistant: Integrated with Amazon Bedrock (Anthropic Claude 3 Sonnet) to answer follow-up questions about detected items, recycling processes, and environmental impact.
Simple & Clean UI: An intuitive and user-friendly interface that makes waste sorting easy.
How to Run the Application Locally
Follow these instructions to set up and run the project on your computer.
Step 1: Prerequisites
Python 3.10: You must have Python version 3.10 installed on your system.
AWS Account & CLI:
An AWS account with access to Amazon Bedrock.
You must have the AWS CLI installed on your machine.
Bedrock Model Access: You must go to the Amazon Bedrock console in the us-east-1 (N. Virginia) region and manually request and be granted access to the "Nova Pro" model.
Step 2: Project Setup
Check Folder Structure: Make sure your project has a folder named templates and that the waste_sorter.html file is inside it.
Open a Terminal: Open your terminal or command prompt and navigate to the main project folder (e.g., /GreatAI/).
Create a Virtual Environment:
# On Windows
py -3.10 -m venv venv

# On Mac/Linux
python3.10 -m venv venv


Activate the Environment:
# On Windows
.\venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate


Install Dependencies: Run the following command to install all the necessary Python libraries.
pip install -r requirements.txt


Step 3: Configuration
Configure AWS Credentials:
In your terminal, run the command aws configure.
You will be prompted to enter your AWS Access Key ID and AWS Secret Access Key. (See the AWS_CREDENTIALS_GUIDE.md for instructions on how to generate these).
For the Default region name, you must enter us-east-1.
For the Default output format, you can just press Enter.
Step 4: Run the Application
Start the Server: In your activated terminal, run the following command:
python app.py


Open the App: Open your web browser and go to this address:
[http://127.0.0.1:5000](http://127.0.0.1:5000)


The Smart Waste Sorter application should now be running successfully on your local machine.
