import mysql.connector
from mysql.connector import Error

class Database:
    def get_db_connection(self):
        """
        Establish a connection to the MySQL database.
        """
        try:
            # Attempt to connect to the database
            connection = mysql.connector.connect(
                host="localhost",         # Your database host
                user="root",              # Your MySQL username
                password="root",          # Your MySQL password
                database="student_management_kongu_college"  # Your database name
            )

            # Check if the connection was successful
            if connection.is_connected():
                print("Successfully connected to MySQL database")  # Connection confirmation
                return connection
            else:
                print("Failed to connect to MySQL database")  # If connection fails
                return None

        except Error as e:
            # Handle any connection errors
            print(f"Error: {e}")
            return None

        finally:
            # Ensure the connection is closed
            if connection.is_connected():
                #connection.close()
                print("MySQL connection is still open")

# Create an instance of the Database class (if required)
database_instance = Database()
