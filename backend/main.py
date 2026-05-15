from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, Form
from database import engine
from models import Base
from utils import (
    extract_text_from_pdf,
    extract_skills,
    calculate_similarity
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Resume Screener backend is running"}

@app.post("/analyze")
async def analyze_resume(
    job_description: str = Form(...),
    file: UploadFile = File(...)
):
    # Extract text
    resume_text = extract_text_from_pdf(file.file)

    # Extract skills
    skills = extract_skills(resume_text)

    # Calculate similarity
    score = calculate_similarity(
        resume_text,
        job_description
    )

    return {
        "filename": file.filename,
        "skills": skills,
        "match_score": score
    }