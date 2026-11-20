from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import SessionDep
from models.doctor import Doctor
from schemas.doctor import DoctorUpdate

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.post("/", response_model=Doctor)
def create_doctor(doctor: Doctor, session: SessionDep):
    session.add(doctor)
    session.commit()
    session.refresh(doctor)
    return doctor


@router.get("/", response_model=list[Doctor])
def get_doctors(session: SessionDep):
    return session.exec(select(Doctor)).all()


@router.get("/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int, session: SessionDep):
    doctor = session.get(Doctor, doctor_id)
    if not doctor:
        raise HTTPException(404, "Doctor not found")
    return doctor


@router.put("/{doctor_id}", response_model=Doctor)
def replace_doctor(doctor_id: int, data: Doctor, session: SessionDep):
    doctor = session.get(Doctor, doctor_id)
    if not doctor:
        raise HTTPException(404, "Doctor not found")
    doctor.sqlmodel_update(data.model_dump(exclude={"id"}))
    session.add(doctor)
    session.commit()
    session.refresh(doctor)
    return doctor


@router.patch("/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, data: DoctorUpdate, session: SessionDep):
    doctor = session.get(Doctor, doctor_id)
    if not doctor:
        raise HTTPException(404, "Doctor not found")
    doctor.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(doctor)
    session.commit()
    session.refresh(doctor)
    return doctor


@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int, session: SessionDep):
    doctor = session.get(Doctor, doctor_id)
    if not doctor:
        raise HTTPException(404, "Doctor not found")
    session.delete(doctor)
    session.commit()
    return {"message": "Doctor deleted"}