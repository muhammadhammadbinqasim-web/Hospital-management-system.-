from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import SessionDep
from models.laboratory import Laboratory
from models.doctor import Doctor
from models.patient import Patient
from schemas.laboratory import LaboratoryUpdate

router = APIRouter(prefix="/laboratory", tags=["Laboratory"])


@router.post("/", response_model=Laboratory)
def create_laboratory(item: Laboratory, session: SessionDep):
    if item.doctor_id is not None and not session.get(Doctor, item.doctor_id):
        raise HTTPException(404, "Doctor not found")
    if not session.get(Patient, item.patient_id):
        raise HTTPException(404, "Patient not found")
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/", response_model=list[Laboratory])
def get_laboratories(session: SessionDep):
    return session.exec(select(Laboratory)).all()


@router.get("/{lab_id}", response_model=Laboratory)
def get_laboratory(lab_id: int, session: SessionDep):
    item = session.get(Laboratory, lab_id)
    if not item:
        raise HTTPException(404, "Laboratory record not found")
    return item


@router.put("/{lab_id}", response_model=Laboratory)
def replace_laboratory(lab_id: int, data: Laboratory, session: SessionDep):
    item = session.get(Laboratory, lab_id)
    if not item:
        raise HTTPException(404, "Laboratory record not found")
    if data.doctor_id is not None and not session.get(Doctor, data.doctor_id):
        raise HTTPException(404, "Doctor not found")
    if not session.get(Patient, data.patient_id):
        raise HTTPException(404, "Patient not found")
    item.sqlmodel_update(data.model_dump(exclude={"id"}))
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.patch("/{lab_id}", response_model=Laboratory)
def update_laboratory(lab_id: int, data: LaboratoryUpdate, session: SessionDep):
    item = session.get(Laboratory, lab_id)
    if not item:
        raise HTTPException(404, "Laboratory record not found")
    item.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{lab_id}")
def delete_laboratory(lab_id: int, session: SessionDep):
    item = session.get(Laboratory, lab_id)
    if not item:
        raise HTTPException(404, "Laboratory record not found")
    session.delete(item)
    session.commit()
    return {"message": "Laboratory record deleted"}