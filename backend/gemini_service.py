import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume_text, job_description=""):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the following resume.

Return the response in this format:

ATS Score:

Professional Summary:

Strengths:

Weaknesses:

Missing Skills:

Grammar Suggestions:

Formatting Suggestions:

Best Job Roles:

Resume Improvement Tips:

Final Verdict:

Resume:
{resume_text}

Job Description:
{job_description}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="models/gemini-flash-lite-latest",
                contents=prompt
            )
            return response.text

        except Exception as e:
            if attempt == 2:
                raise e
            time.sleep(2)