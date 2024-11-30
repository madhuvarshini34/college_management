from fastapi import APIRouter, HTTPException
from database import database 

class Students:
    router = APIRouter()

    @router.get("/") 
    def list_students(self):
        connection = database.get_db_connection()  
        if not connection:
            raise HTTPException(status_code=500, detail="Failed to connect to the database")
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute("SELECT * FROM students")  
            students = cursor.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error fetching data from database")
        finally:
            connection.close()
        
        if not students:
            raise HTTPException(status_code=404, detail="No students found")
        
        return students
students_router= Students()
