from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import SessionDep
from models.bill import Bill
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment
from schemas.bill import BillUpdate

router = APIRouter(prefix="/bills", tags=["Bills"])


@router.post("/", response_model=Bill)
def create_bill(bill: Bill, session: SessionDep):
    if not session.get(Doctor, bill.doctor_id):
        raise HTTPException(404, "Doctor not found")
    if not session.get(Patient, bill.patient_id):
        raise HTTPException(404, "Patient not found")
    if bill.appointment_id is not None and not session.get(Appointment, bill.appointment_id):
        raise HTTPException(404, "Appointment not found")
    session.add(bill)
    session.commit()
    session.refresh(bill)
    return bill


@router.get("/", response_model=list[Bill])
def get_bills(session: SessionDep):
    return session.exec(select(Bill)).all()


@router.get("/{bill_id}", response_model=Bill)
def get_bill(bill_id: int, session: SessionDep):
    bill = session.get(Bill, bill_id)
    if not bill:
        raise HTTPException(404, "Bill not found")
    return bill


@router.put("/{bill_id}", response_model=Bill)
def replace_bill(bill_id: int, data: Bill, session: SessionDep):
    bill = session.get(Bill, bill_id)
    if not bill:
        raise HTTPException(404, "Bill not found")
    if not session.get(Doctor, data.doctor_id):
        raise HTTPException(404, "Doctor not found")
    if not session.get(Patient, data.patient_id):
        raise HTTPException(404, "Patient not found")
    if data.appointment_id is not None and not session.get(Appointment, data.appointment_id):
        raise HTTPException(404, "Appointment not found")
    bill.sqlmodel_update(data.model_dump(exclude={"id"}))
    session.add(bill)
    session.commit()
    session.refresh(bill)
    return bill


@router.patch("/{bill_id}", response_model=Bill)
def update_bill(bill_id: int, data: BillUpdate, session: SessionDep):
    bill = session.get(Bill, bill_id)
    if not bill:
        raise HTTPException(404, "Bill not found")
    bill.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(bill)
    session.commit()
    session.refresh(bill)
    return bill


@router.delete("/{bill_id}")
def delete_bill(bill_id: int, session: SessionDep):
    bill = session.get(Bill, bill_id)
    if not bill:
        raise HTTPException(404, "Bill not found")
    session.delete(bill)
    session.commit()
    return {"message": "Bill deleted"}