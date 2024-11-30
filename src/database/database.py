import mysql.connector
from mysql.connector import Error

class Database:
    @staticmethod
    def get_db_connection():
        try:
        
            connection = mysql.connector.connect(
                host="localhost", 
                user="root",       
                password="root",   
                database="student_management_kongu_college"  
            )
            
            if connection.is_connected():
                print("Successfully connected to MySQL database")
                return connection
            else:
                print("Failed to connect to MySQL database")
                return None
        except Error as e:
            print(f"Error: {e}")
            return None
        finally:
            if connection and connection.is_connected():
                connection.close()
                print("MySQL connection is closed")


