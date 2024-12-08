from fastapi import FastAPI
from students import students_instance  # Import the instance of the Students class
from departments import departments_instance  # Import the instance of the Departments class
from subjects import subjects_instance  # Import the instance of the Subjects class

app = FastAPI()

# Include the students, departments, and subjects routers in the main app
#app.include_router(students_instance.router, prefix="/students", tags=["students"])
#app.include_router(departments_instance.router, prefix="/departments", tags=["departments"])
#app.include_router(subjects_instance.router, prefix="/subjects", tags=["subjects"])

# Example of a route in the main app that calls the get_students method directly
@app.get("/students")
async def get_all_students():
    return students_instance.get_students()

# Example of a route in the main app that calls the get_departments method directly
@app.get("/departments")
async def get_all_departments():
    print("initiating department class")
    return departments_instance.get_departments()

# Example of a route in the main app that calls the get_subjects method directly
@app.get("/subjects")
async def get_all_subjects():
    return subjects_instance.get_subjects()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)


