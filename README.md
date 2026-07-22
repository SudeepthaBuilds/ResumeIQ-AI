# 📄 ResumeIQ AI

An AI-powered Resume Analyzer that evaluates resumes against a job description using Google's Gemini AI. The application extracts text from PDF resumes, analyzes ATS compatibility, and provides personalized improvement suggestions through a clean and user-friendly web interface.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 🤖 AI-powered Resume Analysis using Gemini
- 📊 ATS Score Generation
- 💼 Job Description Matching
- ✅ Resume Strengths
- ❌ Resume Weaknesses
- 🛠 Missing Skills Detection
- ✍ Grammar Suggestions
- 🎨 Formatting Suggestions
- 💡 Resume Improvement Tips
- 🎯 Best Job Role Recommendations
- 🌐 Responsive Web Interface
- 🐳 Docker Support

---

## 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- FastAPI
- Python

### AI
- Google Gemini API

### Libraries
- PyMuPDF (PDF Text Extraction)
- python-dotenv
- Uvicorn
- Jinja2

### Deployment
- Docker
- AWS App Runner

---

## 📂 Project Structure

```
ResumeIQ-AI/
│
├── backend/
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── main.py
│   ├── utils.py
│   ├── gemini_service.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   └── .env
│
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ResumeIQ-AI.git
```

```bash
cd ResumeIQ-AI/backend
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file inside the backend folder.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

### Run the Project

```bash
uvicorn main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

## 🐳 Docker

Build Docker Image

```bash
docker build -t resumeiq-ai .
```

Run Docker Container

```bash
docker run -p 8000:8000 --env-file .env resumeiq-ai
```

Open

```
http://localhost:8000
```

---

## 📷 Application Workflow

1. Upload Resume (PDF)
2. Enter Job Description
3. Click **Analyze Resume**
4. AI Extracts Resume Text
5. Gemini AI Evaluates Resume
6. Displays:
   - ATS Score
   - Professional Summary
   - Strengths
   - Weaknesses
   - Missing Skills
   - Grammar Suggestions
   - Formatting Suggestions
   - Best Job Roles
   - Improvement Tips
   - Final Verdict

---

## 📌 Future Enhancements

- Resume Download (PDF)
- User Authentication
- Resume History
- Dashboard Analytics
- Multiple Resume Comparison
- Cover Letter Generator
- Interview Question Generator

---

## 👩‍💻 Author

**Sudeeptha Thoram**

B.Tech (CSE - AIML)

---

## 📄 License

This project is developed for educational and learning purposes.