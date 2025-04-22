
# English Language Learning App

This is a full-stack web app built with Flask (backend) and React (frontend) to help users learn English using AI.

---

## Setup Instructions

### 1. Clone the Repository & Unzip

Unzip the project folder and navigate to the directory:

```
cd english-language-app
```

---

### 2. Backend Setup

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Paste your OpenAI API key into the .env file

##Receive your OpenAI key from: https://platform.openai.com/api-keys
python app.py
```

The Flask server will run at `http://127.0.0.1:5000`

---

### 3. Frontend Setup

(You can replace this with your React frontend)

```
cd ../frontend
npm install
npm run dev
```

The frontend will run at `http://localhost:5173`

---

###Features

- Vocabulary definition
- English conversation continuation
- Reading comprehension summarization

---
