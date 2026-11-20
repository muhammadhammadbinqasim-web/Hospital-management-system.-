# Hospital Management System API

ایک جدید اور مکمل ہاسپٹل مینجمنٹ سسٹم جو **FastAPI** اور **SQLModel** کے ذریعے بنایا گیا ہے۔

## پروجیکٹ کا ڈھانچہ (Project Structure)

```text
Hospital managment system/
│
├── database.py                 # SQLite انجن اور سیشن سیٹ اپ
├── main.py                     # مین ایپلیکیشن فائل
├── requirements.txt            # درکار لائبریریز
├── hospital.db                 # SQLite ڈیٹا بیس فائل
│
├── models/                     # SQLModel کے ڈیٹا بیس ماڈلز
│   ├── doctor.py               # ڈاکٹر کا ماڈل
│   ├── patient.py              # مریض کا ماڈل
│   ├── appointment.py          # اپوائنٹمنٹ کا ماڈل
│   └── bill.py                 # بل اور فیس کا ماڈل
│
├── schemas/                    # جزوی اپڈیٹ (PATCH) سکیماز
│   ├── doctor.py               # DoctorUpdate
│   ├── patient.py              # PatientUpdate
│   ├── appointment.py          # AppointmentUpdate
│   └── bill.py                 # BillUpdate
│
└── routers/                    # تمام CRUD اینڈ پوائنٹس
    ├── doctor.py               # /doctors
    ├── patient.py              # /patients
    ├── appointment.py          # /appointments
    └── bill.py                 # /bills
```

## پروجیکٹ چلانے کا طریقہ (How to Run)

1. **لائبریریز انسٹال کریں:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **ایپلیکیشن چلائیں:**
   ```powershell
   python main.py
   ```
   یا
   ```powershell
   uvicorn main:app --reload
   ```

3. **انٹرایکٹو API ڈاکومنٹیشن دیکھیں:**
   براؤزر میں یہ لنک کھولیں:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
