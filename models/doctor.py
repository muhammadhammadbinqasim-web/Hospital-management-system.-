from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Doctor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=50)
    specialization: str
    phone: str = Field(unique=True)
    fee: float = Field(gt=0)

    appointments: list["Appointment"] = Relationship(back_populates="doctor")
    patients: list["Patient"] = Relationship(back_populates="doctor")
    bills: list["Bill"] = Relationship(back_populates="doctor")
    pharmacies: list["Pharmacy"] = Relationship(back_populates="doctor")
    laboratories: list["Laboratory"] = Relationship(back_populates="doctor")