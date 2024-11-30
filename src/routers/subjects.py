# subjects.py
from fastapi import APIRouter, HTTPException
from db import get_db_connection

router = APIRouter()

# This endpoint handles listing subjects for a specific department
@router.get("/")
def list_subjects_of_department(department_name: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM subjects WHERE department = %s"
    
    try:
        cursor.execute(query, (department_name,))
        subjects = cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching subjects")
    finally:
        connection.close()
    
    if not subjects:
        raise HTTPException(status_code=404, detail="Subjects not found for the department")
    
    return subjects