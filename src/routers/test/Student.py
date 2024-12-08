from datetime import datetime

class Student:
    # Class attribute
    school_name = "ABC High School"
    
    def __init__(self):
        # Private instance attributes
        self._name = None
        self._age = None
        self._grade = None
        self._dob = None  # Private DOB attribute
    
    def display_info(self):
        dob_str = self.dob.strftime("%Y-%m-%d") if self.dob else "Not Provided"
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Date of Birth: {dob_str}")

    # Getter for name
    @property
    def name(self):
        return self._name
    
    # Setter for name
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()
    
    # Getter for age
    @property
    def age(self):
        return self._age
    
    # Setter for age
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or not (0 < value < 120):
            raise ValueError("Age must be a positive integer between 1 and 119.")
        self._age = value

    # Getter for grade
    @property
    def grade(self):
        return self._grade
    
    # Setter for grade
    @grade.setter
    def grade(self, value):
        if not value.strip():
            raise ValueError("Grade cannot be empty.")
        self._grade = value.strip()

    # Getter for dob
    @property
    def dob(self):
        return self._dob
    
    # Setter for dob
    @dob.setter
    def dob(self, value):
        if not value:
            self._dob = None
            return
        try:
            # Parse the date string into a datetime object
            self._dob = datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
