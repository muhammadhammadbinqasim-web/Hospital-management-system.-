from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import SessionDep
from models.appointment import Appointment
from models.doctor import Doctor
from models.patient import Patient
from schemas.appointment import AppointmentUpdate

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("/", response_model=Appointment)
def create_appointment(appt: Appointment, session: SessionDep):
    if not session.get(Doctor, appt.doctor_id):
        raise HTTPException(404, "Doctor not found")
    if not session.get(Patient, appt.patient_id):
        raise HTTPException(404, "Patient not found")
    session.add(appt)
    session.commit()
    session.refresh(appt)
    return appt


@router.get("/", response_model=list[Appointment])
def get_appointments(session: SessionDep):
    return session.exec(select(Appointment)).all()


@router.get("/{appt_id}", response_model=Appointment)
def get_appointment(appt_id: int, session: SessionDep):
    appt = session.get(Appointment, appt_id)
    if not appt:
        raise HTTPException(404, "Appointment not found")
    return appt


@router.put("/{appt_id}", response_model=Appointment)
def replace_appointment(appt_id: int, data: Appointment, session: SessionDep):
    appt = session.get(Appointment, appt_id)
    if not appt:
        raise HTTPException(404, "Appointment not found")
    if not session.get(Doctor, data.doctor_id):
        raise HTTPException(404, "Doctor not found")
    if not session.get(Patient, data.patient_id):
        raise HTTPException(404, "Patient not found")
    appt.sqlmodel_update(data.model_dump(exclude={"id"}))
    session.add(appt)
    session.commit()
    session.refresh(appt)
    return appt


@router.patch("/{appt_id}", response_model=Appointment)
def update_appointment(appt_id: int, data: AppointmentUpdate, session: SessionDep):
    appt = session.get(Appointment, appt_id)
    if not appt:
        raise HTTPException(404, "Appointment not found")
    appt.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(appt)
    session.commit()
    session.refresh(appt)
    return appt


@router.delete("/{appt_id}")
def delete_appointment(appt_id: int, session: SessionDep):
    appt = session.get(Appointment, appt_id)
    if not appt:
        raise HTTPException(404, "Appointment not found")
    session.delete(appt)
    session.commit()
    return {"message": "Appointment deleted"}