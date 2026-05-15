from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

SKILLS = [
    "python",
    "fastapi",
    "sql",
    "docker",
    "react",
    "machine learning",
    "nlp"
]

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text.lower()

def extract_skills(text):
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found

def calculate_similarity(resume_text, job_description):
    embeddings = model.encode([
        resume_text,
        job_description
    ])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(similarity * 100, 2)