from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Bill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    doctor_id: int = Field(foreign_key="doctor.id")
    patient_id: int = Field(foreign_key="patient.id")
    appointment_id: Optional[int] = Field(default=None, foreign_key="appointment.id")
    amount: float = Field(gt=0)
    paid: bool = False

    doctor: Optional["Doctor"] = Relationship(back_populates="bills")
    patient: Optional["Patient"] = Relationship(back_populates="bills")
    appointment: Optional["Appointment"] = Relationship(back_populates="bills")