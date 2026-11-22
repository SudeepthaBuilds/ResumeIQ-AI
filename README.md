# 📄 ResumeIQ AI — Intelligent ATS & Career Optimization Engine
**Next-Generation AI Resume Analyzer, Job-Description Matcher & ATS Scoring Command Center**

ResumeIQ AI is a high-performance, **FastAPI and Google Gemini-powered career intelligence platform** engineered to evaluate PDF resumes against target job descriptions. By combining high-speed **PyMuPDF text extraction** with structured **Gemini AI prompt evaluation**, it delivers instant ATS compatibility scores, skill-gap diagnostics, and actionable resume optimization insights through a sleek, containerized web interface.

**`🟢 STATUS: ACTIVE`** &nbsp; **`✨ GEMINI AI`** &nbsp; **`⚡ FASTAPI`** &nbsp; **`🐳 DOCKER & AWS READY`**

---

## 🛠️ Performance Tech Stack & Technologies Built With

**`🐍 Python`** &nbsp; **`⚡ FastAPI`** &nbsp; **`✨ Google Gemini API`** &nbsp; **`📄 PyMuPDF`** &nbsp; **`🐳 Docker`** &nbsp; **`☁️ AWS App Runner`** &nbsp; **`🎨 HTML5 / CSS3 / JS`**

| Component | Technology |
| :--- | :--- |
| **Core AI Engine** | Google Gemini API (`gemini_service.py`) |
| **Backend & Server** | FastAPI, Uvicorn (ASGI High-Performance Server) |
| **Document Parsing** | PyMuPDF (`fitz` — Fast PDF Text Extraction) |
| **Frontend & UI** | HTML5, CSS3, Vanilla JavaScript, Jinja2 Templates |
| **Configuration** | `python-dotenv` (Secure API Key & Environment Management) |
| **Container & Cloud** | Docker, AWS App Runner Deployment Ready |

---

## 🚀 Career Intelligence Command Center Features

### 📊 ATS Compatibility & Role Matching
- **Real-Time ATS Score Generation:** Quantifies how well a resume aligns with Applicant Tracking System filters and target job requirements.
- **Job Description Semantic Matching:** Compares candidate experience directly against pasted job descriptions to uncover alignment gaps.
- **Best-Fit Job Role Recommendations:** Suggests optimal target roles tailored to the candidate's existing technical stack and projects.

### 🔍 Deep Resume Diagnostics
- **Strengths & Weaknesses Audit:** Highlights high-impact accomplishments alongside areas that need stronger quantification.
- **Missing Skills Detection:** Pinpoints critical keywords, tools, and domain skills missing relative to the target role.
- **Grammar & Formatting Review:** Flags structural, readability, and phrasing issues to ensure recruiter-ready polish.
- **Actionable Improvement Tips & Final Verdict:** Delivers concrete rewrite recommendations and a clear hiring-readiness summary.

### 🖥️ Modern Web UI & Cloud-Native Deployment
- **Frictionless PDF Upload:** Clean, responsive interface for drag-and-drop resume analysis in seconds.
- **Dockerized Microservice:** Packaged with `Dockerfile` and `.dockerignore` for consistent local execution and one-click cloud deployment on **AWS App Runner**.

---

## 📂 System Architecture

The repository follows a clean backend-encapsulated architecture, separating PDF parsing, Gemini AI evaluation services, and Jinja2 frontend assets.

```text
ResumeIQ-AI/
├── backend/
│   ├── static/                 # 🎨 Frontend Styling & Interactive Client Logic
│   │   ├── style.css           # Responsive UI design tokens & layout
│   │   └── script.js           # Async form submission & dynamic result rendering
│   ├── templates/              # 🖥️ Server-Rendered Web Interface
│   │   └── index.html          # Main resume upload & ATS dashboard view
│   ├── main.py                 # ⚡ FastAPI application entry point & API routes
│   ├── utils.py                # 📄 PyMuPDF text extraction & preprocessing helpers
│   ├── gemini_service.py       # 🤖 Google Gemini API integration & structured prompting
│   ├── requirements.txt        # 📦 Python dependency manifest
│   ├── Dockerfile              # 🐳 Production container image configuration
│   ├── .dockerignore           # 🚫 Container build exclusions
│   └── .env                    # 🔐 Local environment variables (excluded from Git)
└── README.md                   # 📘 Professional Project Documentation
```

---

## 🔄 End-to-End Evaluation Workflow

```text
[1. Upload PDF Resume + Paste Job Description (index.html)]
                           │
                           ▼
[2. High-Speed PDF Text Extraction (utils.py / PyMuPDF)]
                           │
                           ▼
[3. Structured ATS & Gap Evaluation (gemini_service.py)]
                           │
                           ▼
[4. Comprehensive Career Report Rendered in UI]
    ├── ATS Compatibility Score & Final Verdict
    ├── Key Strengths, Weaknesses & Missing Skills
    ├── Grammar, Formatting & Rewrite Suggestions
    └── Best-Fit Job Role Recommendations
```

---

## 🏁 Quick Start Guide

### 1️⃣ Environment Setup
```bash
git clone https://github.com
cd ResumeIQ-AI/backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Configure Environment Variables
Create a `.env` file inside the `backend/` directory and add your Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3️⃣ Launch the FastAPI Server
```bash
uvicorn main:app --reload
```
🌐 **Application URL:** `http://127.0.0.1:8000`

---

## 🐳 Docker Deployment

Run **ResumeIQ AI** inside an isolated container ready for **AWS App Runner** or any cloud host:

```bash
# Build the Docker image (from inside ResumeIQ-AI/backend)
docker build -t resumeiq-ai .

# Run the container with environment variables
docker run -p 8000:8000 --env-file .env resumeiq-ai
```
🌐 **Container URL:** `http://localhost:8000`

---

## 🚀 Product Roadmap
- [ ] **Exportable PDF Report:** One-click download of the full ATS audit and rewrite suggestions.
- [ ] **User Accounts & Resume History:** Track score improvements across multiple resume versions.
- [ ] **Multi-Resume Comparison:** Side-by-side benchmarking for tailored role applications.
- [ ] **AI Cover Letter & Interview Prep Generator:** Auto-generate role-specific cover letters and likely interview questions from the parsed resume.

---

## 🛡️ Security & Privacy Notes
- **API Key Protection:** Ensure `.env` is listed in your `.gitignore` file so your `GEMINI_API_KEY` is never committed to public repositories.
- **Educational & Demonstration Use:** Built as an AI career-tech showcase demonstrating FastAPI, LLM structured evaluation, and containerized cloud deployment.

**Crafted for Innovation by [SudeepthaBuilds](https://github.com) | B.Tech CSE (AI & ML)**
