from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import SessionDep
from models.patient import Patient
from models.doctor import Doctor
from schemas.patient import PatientUpdate

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/", response_model=Patient)
def create_patient(patient: Patient, session: SessionDep):
    if patient.doctor_id is not None and not session.get(Doctor, patient.doctor_id):
        raise HTTPException(404, "Doctor not found")
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.get("/", response_model=list[Patient])
def get_patients(session: SessionDep):
    return session.exec(select(Patient)).all()


@router.get("/{patient_id}", response_model=Patient)
def get_patient(patient_id: int, session: SessionDep):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(404, "Patient not found")
    return patient


@router.put("/{patient_id}", response_model=Patient)
def replace_patient(patient_id: int, data: Patient, session: SessionDep):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(404, "Patient not found")
    if data.doctor_id is not None and not session.get(Doctor, data.doctor_id):
        raise HTTPException(404, "Doctor not found")
    patient.sqlmodel_update(data.model_dump(exclude={"id"}))
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.patch("/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, data: PatientUpdate, session: SessionDep):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(404, "Patient not found")
    changes = data.model_dump(exclude_unset=True)
    new_doctor_id = changes.get("doctor_id")
    if new_doctor_id is not None and not session.get(Doctor, new_doctor_id):
        raise HTTPException(404, "Doctor not found")
    patient.sqlmodel_update(changes)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.delete("/{patient_id}")
def delete_patient(patient_id: int, session: SessionDep):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(404, "Patient not found")
    session.delete(patient)
    session.commit()
    return {"message": "Patient deleted"}