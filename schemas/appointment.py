from typing import Optional
from sqlmodel import SQLModel


class AppointmentUpdate(SQLModel):
    date: Optional[str] = None
    status: Optional[str] = None