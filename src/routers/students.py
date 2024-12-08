from fastapi import APIRouter, HTTPException
from database import database_instance  # Correct import of the 'database' class

class Students:
    def get_students(self):
        # Establishing the database connection using the static method
        connection = database_instance.get_db_connection()
        if not connection:
            raise HTTPException(status_code=500, detail="Failed to connect to the database")
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute("SELECT * FROM students")  # Query to fetch students
            students = cursor.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error fetching data from database")
        finally:
            connection.close()  # Ensure the connection is closed after the operation
        
        if not students:
            raise HTTPException(status_code=404, detail="No students found")
        
        return students  # Return the result as JSON

# Create an instance of the Students class
students_instance = Students()
