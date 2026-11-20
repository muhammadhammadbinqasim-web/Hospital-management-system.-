from .doctor import router as doctor_router
from .patient import router as patient_router
from .appointment import router as appointment_router
from .bill import router as bill_router

__all__ = ["doctor_router", "patient_router", "appointment_router", "bill_router"]
