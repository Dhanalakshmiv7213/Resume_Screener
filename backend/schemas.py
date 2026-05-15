from pydantic import BaseModel
from typing import Optional

class ResumeBase(BaseModel):
    name: str
    email: str
    summary: Optional[str] = None
    skills: Optional[str] = None

class ResumeCreate(ResumeBase):
    pass

class Resume(ResumeBase):
    id: int

    class Config:
        orm_mode = True
