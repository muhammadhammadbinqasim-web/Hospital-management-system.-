from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Pharmacy(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    doctor_id: Optional[int] = Field(default=None, foreign_key="doctor.id")
    patient_id: int = Field(foreign_key="patient.id")
    medicine_name: str = Field(min_length=2, max_length=100)
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    date: str

    doctor: Optional["Doctor"] = Relationship(back_populates="pharmacies")
    patient: Optional["Patient"] = Relationship(back_populates="pharmacies")