from typing import Optional
from sqlmodel import SQLModel


class PatientUpdate(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    disease: Optional[str] = None
    doctor_id: Optional[int] = None