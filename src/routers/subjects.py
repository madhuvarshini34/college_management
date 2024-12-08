from fastapi import APIRouter, HTTPException
from database import database_instance

class Subjects:
    def get_subjects(self):
        connection = database_instance.get_db_connection()  
        if not connection:
            raise HTTPException(status_code=500, detail="Failed to connect to the database")
        
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("SELECT * FROM subjects")
            subjects = cursor.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
        finally:
            connection.close()
        
        if not subjects:
            raise HTTPException(status_code=404, detail="No subjects found")
        
        return subjects
    
subjects_instance = Subjects()
