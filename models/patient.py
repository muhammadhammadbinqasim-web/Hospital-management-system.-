from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=0, le=120)
    gender: str
    phone: str = Field(unique=True)
    disease: str
    doctor_id: Optional[int] = Field(default=None, foreign_key="doctor.id")

    doctor: Optional["Doctor"] = Relationship(back_populates="patients")
    appointments: list["Appointment"] = Relationship(back_populates="patient")
    bills: list["Bill"] = Relationship(back_populates="patient")
    pharmacies: list["Pharmacy"] = Relationship(back_populates="patient")
    laboratories: list["Laboratory"] = Relationship(back_populates="patient")