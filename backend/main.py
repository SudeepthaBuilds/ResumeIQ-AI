from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from utils import extract_text_from_pdf
from gemini_service import analyze_resume

app = FastAPI(title="ResumeIQ AI")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    job_description: str = Form("")
):
    try:
        if file.content_type != "application/pdf":
            return {"error": "Please upload a PDF file."}

        resume_text = extract_text_from_pdf(file.file)

        if not resume_text.strip():
            return {"error": "No text found in the PDF."}

        result = analyze_resume(resume_text, job_description)

        return {
            "success": True,
            "analysis": result
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }