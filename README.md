# ♻️ Smart Waste Sorter ft. Amazon Bedrock

An AI-powered waste sorting assistant that helps users correctly identify and dispose of waste items.
This project combines Roboflow YOLO for real-time object detection and Amazon Bedrock for intelligent conversational insights.

# 🚀 Features

✅ Multi-Modal Input – Detect waste using live camera feed or uploaded images. 

✅ High-Accuracy Detection – Roboflow YOLO model trained on 42 specific waste classes.

✅ Disposal Guidance – Instant, item-specific instructions on how to dispose of detected waste.

✅ Conversational AI Assistant – Powered by Amazon Bedrock (Anthropic Claude 3 Sonnet / Nova Pro) to answer questions about recycling and environmental impact.

✅ Simple & Clean UI – Intuitive design for easy waste sorting.

# 🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript (Flask templates)

Backend: Python (Flask)

AI Models:

Roboflow YOLO (waste classification – 42 classes)

Amazon Bedrock (Claude 3 Sonnet / Nova Pro for Q&A)

Cloud: AWS (Bedrock, CLI configuration)

⚡ Getting Started

1️⃣ Prerequisites

Python 3.10 installed.

AWS Account with Bedrock access.

AWS CLI installed.

Bedrock model access for Nova Pro in us-east-1 (N. Virginia) region.

2️⃣ Project Setup

Clone the repository and set up dependencies:

1. Clone repo
git clone https://github.com/your-username/smart-waste-sorter.git
cd smart-waste-sorter

2. Create virtual environment

For Windows:
py -3.10 -m venv venv
.\venv\Scripts\activate

For Mac/Linux:
python3.10 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

3️⃣ Configure AWS

In your terminal, run the command aws configure.

You will be prompted to enter your AWS Access Key ID and AWS Secret Access Key. (See the AWS_CREDENTIALS_GUIDE.md for instructions on how to generate these).

For the Default region name, you must enter us-east-1.

For the Default output format, you can just press Enter.

4️⃣ Run the Application
python app.py


Open in browser:
👉 http://127.0.0.1:5000

# 🌱 Future Improvements

✅ Mobile-friendly responsive design

✅ Support for more waste classes

✅ Gamification features (badges for eco-friendly behavior)

✅ Cloud deployment (AWS Elastic Beanstalk / Docker)

# 📜 License

MIT License – feel free to use, modify, and distribute.

# 🧠 Acknowledgments

Roboflow
 – YOLO waste dataset & model training

Amazon Bedrock
 – Conversational AI integration

Flask
 – Web app framework
