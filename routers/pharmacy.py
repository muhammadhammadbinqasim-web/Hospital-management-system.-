from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import SessionDep
from models.pharmacy import Pharmacy
from models.doctor import Doctor
from models.patient import Patient
from schemas.pharmacy import PharmacyUpdate

router = APIRouter(prefix="/pharmacy", tags=["Pharmacy"])


@router.post("/", response_model=Pharmacy)
def create_pharmacy(item: Pharmacy, session: SessionDep):
    if item.doctor_id is not None and not session.get(Doctor, item.doctor_id):
        raise HTTPException(404, "Doctor not found")
    if not session.get(Patient, item.patient_id):
        raise HTTPException(404, "Patient not found")
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/", response_model=list[Pharmacy])
def get_pharmacies(session: SessionDep):
    return session.exec(select(Pharmacy)).all()


@router.get("/{pharmacy_id}", response_model=Pharmacy)
def get_pharmacy(pharmacy_id: int, session: SessionDep):
    item = session.get(Pharmacy, pharmacy_id)
    if not item:
        raise HTTPException(404, "Pharmacy record not found")
    return item


@router.put("/{pharmacy_id}", response_model=Pharmacy)
def replace_pharmacy(pharmacy_id: int, data: Pharmacy, session: SessionDep):
    item = session.get(Pharmacy, pharmacy_id)
    if not item:
        raise HTTPException(404, "Pharmacy record not found")
    if data.doctor_id is not None and not session.get(Doctor, data.doctor_id):
        raise HTTPException(404, "Doctor not found")
    if not session.get(Patient, data.patient_id):
        raise HTTPException(404, "Patient not found")
    item.sqlmodel_update(data.model_dump(exclude={"id"}))
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.patch("/{pharmacy_id}", response_model=Pharmacy)
def update_pharmacy(pharmacy_id: int, data: PharmacyUpdate, session: SessionDep):
    item = session.get(Pharmacy, pharmacy_id)
    if not item:
        raise HTTPException(404, "Pharmacy record not found")
    item.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{pharmacy_id}")
def delete_pharmacy(pharmacy_id: int, session: SessionDep):
    item = session.get(Pharmacy, pharmacy_id)
    if not item:
        raise HTTPException(404, "Pharmacy record not found")
    session.delete(item)
    session.commit()
    return {"message": "Pharmacy record deleted"}