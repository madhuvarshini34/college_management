from fastapi import APIRouter, HTTPException
from db import get_db_connection

router = APIRouter()

@router.get("/")
def list_all_departments():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM departments"
    cursor.execute(query)
    departments = cursor.fetchall()
    connection.close()
    
    if not departments:
        raise HTTPException(status_code=404, detail="No departments found")
    
    return departments
