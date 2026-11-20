from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_db_and_tables
from models import doctor, patient, appointment, bill, pharmacy, laboratory
from routers import doctor, patient, appointment, bill, pharmacy, laboratory


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(title="Hospital Management System", lifespan=lifespan)

app.include_router(doctor.router)
app.include_router(patient.router)
app.include_router(appointment.router)
app.include_router(bill.router)
app.include_router(pharmacy.router)
app.include_router(laboratory.router)


@app.get("/")
def home():
    return {"message": "Hospital Management System is running"}