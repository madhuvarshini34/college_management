from fastapi import FastAPI
from students import router as students_router  
from departments import router as departments_router
from subjects import router as subjects_router  

app = FastAPI()

app.include_router(students_router, prefix="/students", tags=["students"])
app.include_router(departments_router, prefix="/departments", tags=["departments"])
app.include_router(subjects_router, prefix="/subjects", tags=["subjects"])



