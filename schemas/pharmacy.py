from typing import Optional
from sqlmodel import SQLModel


class PharmacyUpdate(SQLModel):
    medicine_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    date: Optional[str] = None