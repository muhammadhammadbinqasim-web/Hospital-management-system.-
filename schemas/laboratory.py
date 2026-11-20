from typing import Optional
from sqlmodel import SQLModel


class LaboratoryUpdate(SQLModel):
    test_name: Optional[str] = None
    price: Optional[float] = None
    result: Optional[str] = None
    status: Optional[str] = None
    date: Optional[str] = None