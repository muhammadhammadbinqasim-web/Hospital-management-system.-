from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Appointment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    doctor_id: int = Field(foreign_key="doctor.id")
    patient_id: int = Field(foreign_key="patient.id")
    date: str
    status: str = "pending"

    doctor: Optional["Doctor"] = Relationship(back_populates="appointments")
    patient: Optional["Patient"] = Relationship(back_populates="appointments")
    bills: list["Bill"] = Relationship(back_populates="appointment")