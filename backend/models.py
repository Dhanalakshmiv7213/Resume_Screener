from sqlalchemy import Column, Integer, String, Float, Text
from database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    extracted_skills = Column(Text)
    match_score = Column(Float)