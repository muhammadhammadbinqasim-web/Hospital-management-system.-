from typing import Optional
from sqlmodel import SQLModel


class DoctorUpdate(SQLModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None
    fee: Optional[float] = None