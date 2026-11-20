from typing import Optional
from sqlmodel import SQLModel


class BillUpdate(SQLModel):
    amount: Optional[float] = None
    paid: Optional[bool] = None