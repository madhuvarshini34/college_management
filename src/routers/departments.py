from fastapi import APIRouter, HTTPException
from database import database_instance    # Correct import of the 'database' class

class Departments:
    def get_departments(self):
        connection = database_instance.get_db_connection()  # Establish the connection using the static method
        if not connection:
            raise HTTPException(status_code=500, detail="Failed to connect to the database")
        print("checking connection",connection.is_connected())
        cursor = connection.cursor(dictionary=True)
        print("checking cursor",cursor)
        
        try:
            cursor.execute("SELECT * FROM departments")  # Query to fetch departments
            departments = cursor.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error fetching data from database")
        finally:
            connection.close()
        
        if not departments:
            raise HTTPException(status_code=404, detail="No departments found")
        
        return departments  # Return the result as JSON

# Create an instance of the Departments class
departments_instance = Departments()


