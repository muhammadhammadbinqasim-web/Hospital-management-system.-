from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Laboratory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    doctor_id: Optional[int] = Field(default=None, foreign_key="doctor.id")
    patient_id: int = Field(foreign_key="patient.id")
    test_name: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)
    result: Optional[str] = None
    status: str = "pending"
    date: str

    doctor: Optional["Doctor"] = Relationship(back_populates="laboratories")
    patient: Optional["Patient"] = Relationship(back_populates="laboratories")