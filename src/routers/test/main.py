from Student import Student

def main():
    # Create student objects
    students = []

    # Add student data
    student_data = [
        {"name": "Madhu", "age": 21, "grade": "A", "dob": "2002-04-15"},
        {"name": "Aishu", "age": 20, "grade": "A", "dob": "2003-05-20"},
        {"name": "Monica", "age": 22, "grade": "B", "dob": "2001-02-10"},
        {"name": "Aswi", "age": 19, "grade": "C", "dob": "2004-07-01"},
        {"name": "Jeeva", "age": 23, "grade": "B", "dob": "2000-12-30"},
        {"name": "Ilan", "age": 18, "grade": "A", "dob": "2005-11-11"},
        {"name": "Ani", "age": 21, "grade": "B", "dob": "2002-08-05"},
        {"name": "Rithikaa", "age": 22, "grade": "A", "dob": "2001-03-18"},
        {"name": "Sumi", "age": 20, "grade": "B", "dob": "2003-01-25"},
        {"name": "Vinitha", "age": 21, "grade": "A", "dob": "2002-06-10"}
    ]

    for data in student_data:
        student = Student()
        student.name = data["name"]
        student.age = data["age"]
        student.grade = data["grade"]
        student.dob = data["dob"]
        students.append(student)

    # Display student information
    print("Student Information:")
    for student in students:
        student.display_info()

    # Create a dictionary of students
    student_dict = {student.name: student for student in students}

    # Input to filter names by the first letter
    input_letter = input("Enter a letter to filter names by the first letter: ").strip().upper()
    filtered_by_letter = {
        name: details for name, details in student_dict.items() if name.upper().startswith(input_letter)
    }

    if filtered_by_letter:
        print(f"\nStudents with names starting with '{input_letter}':")
        for name, details in filtered_by_letter.items():
            details.display_info()
    else:
        print(f"No students found with names starting with '{input_letter}'.")

    # Input to filter students by age
    try:
        input_age = int(input("\nEnter an age to filter students below that age: ").strip())
        filtered_by_age = {
            name: details for name, details in student_dict.items() if details.age < input_age
        }

        if filtered_by_age:
            print(f"\nStudents with age below '{input_age}':")
            for name, details in filtered_by_age.items():
                details.display_info()
        else:
            print(f"No students found below the age of '{input_age}'.")
    except ValueError:
        print("Please enter a valid numeric age.")

    # Input to filter students born before a specific year
    try:
        input_year = int(input("\nEnter a year to filter students born before that year: ").strip())
        filtered_by_dob = {
            name: details for name, details in student_dict.items() if details.dob.year < input_year
        }

        if filtered_by_dob:
            print(f"\nStudents born before the year '{input_year}':")
            for name, details in filtered_by_dob.items():
                details.display_info()
        else:
            print(f"No students found born before the year '{input_year}'.")
    except ValueError:
        print("Please enter a valid numeric year.")

if __name__ == "__main__":
    main()
