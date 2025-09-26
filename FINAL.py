# OOP

class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        # Initialize attributes as per instructions
        self.id_name = (student_id, student_name)  # tuple for immutable ID and name
        self.email = email  # string for email
        self.grades = grades if grades is not None else {}  # dictionary for grades {subject: score}
        self.courses = courses if courses is not None else set()  # set for unique courses

    def __str__(self):
        # Return formatted string of student info to match output style
        courses_list = sorted(list(self.courses))  # Convert set to sorted list for printing
        courses_str = str(courses_list) if courses_list else '[]'
        grades_str = str(self.grades)  # Use str() for dict, which shows {'key': value}
        return (f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, "
                f"Email: {self.email}, Grades: {grades_str}, Courses: {courses_str}")

    def calculate_gpa(self):
        # Calculate numerical GPA (challenge)
        if not self.grades:
            return 0.0
        total_points = 0.0
        num_grades = 0
        for score in self.grades.values():
            if score >= 90:
                points = 4.0  # A
            elif score >= 80:
                points = 3.0  # B
            elif score >= 70:
                points = 2.0  # C
            elif score >= 60:
                points = 1.0  # D
            else:
                points = 0.0  # F
            total_points += points
            num_grades += 1
        return total_points / num_grades if num_grades > 0 else 0.0

    def get_letter_grade(self, gpa):
        # Map GPA to letter grade
        if gpa >= 3.7:
            return 'A'
        elif gpa >= 3.0:
            return 'B'
        elif gpa >= 2.0:
            return 'C'
        elif gpa >= 1.0:
            return 'D'
        else:
            return 'F'


class StudentRecords:
    def __init__(self):
        # Initialize empty list for students
        self.students = []  # list to store multiple Student objects

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        # Create Student object and append to list
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added successfully"

    def update_student(self, student_id, email=None, grades=None, courses=None):
        # Find student by ID and update only provided values
        for student in self.students:
            if student.id_name[0] == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades.update(grades)  # merge new grades
                if courses is not None:
                    student.courses.update(courses)  # add new courses to set
                return "Student updated successfully"
        return "Student not found"

    def delete_student(self, student_id):
        # Remove student if found
        for student in self.students:
            if student.id_name[0] == student_id:
                self.students.remove(student)
                return "Student deleted successfully"
        return "Student not found"

    def enroll_course(self, student_id, course):
        # Add course to student’s set (duplicates handled automatically by set)
        for student in self.students:
            if student.id_name[0] == student_id:
                if course in student.courses:
                    return f"{student.id_name[1]} is already enrolled in {course}"
                student.courses.add(course)
                return f"{student.id_name[1]} enrolled in {course}"
        return "Student not found"

    def search_student(self, student_id):
        # Return student info if found, else "Student not found"
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found"

    def search_by_name(self, name):
        # Search by partial or exact name match (challenge)
        matches = []
        for student in self.students:
            if name.lower() in student.id_name[1].lower():
                matches.append(str(student))
        return matches if matches else ["No students found"]

    def print_all_students(self):
        # Helper to print all students (to match "All Students:" output)
        if not self.students:
            print("No students")
            return
        for student in self.students:
            print(str(student))


# Example Run to Match the Provided Output (Updated Names, IDs, and Grades for A)
if __name__ == "__main__":
    records = StudentRecords()

    # Add students (updated names and IDs)
    print(records.add_student("24-38720", "Karl", "karl@example.com",
                              {"Math": 90}, {"Math"}))
    print(records.add_student("24-99999", "Shawn", "shawn@example.com",
                              {"Science": 85}, {"Science"}))

    # All Students:
    print("\nAll Students:")
    records.print_all_students()

    # Updating Info for Student ID: 24-38720
    print("\nUpdating Info for Student ID: 24-38720")
    print(records.update_student("24-38720", email="update@example.com",
                                 grades={"Math": 95, "English": 95}, courses={"English"}))

    # Print all after update
    records.print_all_students()

    # Delete Student:
    print("\nDelete Student:")
    print(records.delete_student("24-99999"))
    print(records.delete_student("99-99999"))  # Not found for "Student not found"

    # Print remaining
    records.print_all_students()

    # Enroll in Course:
    print("\nEnroll in Course:")
    print(records.enroll_course("24-99999", "Science"))  # Student not found (deleted)
    print(records.enroll_course("24-38720", "Science"))  # Karl enrolled in Science
    print(records.enroll_course("24-38720", "Math"))     # Already enrolled

    # Print after enroll
    records.print_all_students()

    # Search by ID:
    print("\nSearch by ID:")
    print(records.search_student("24-38720"))

    # Search by Name:
    print("\nSearch by Name:")
    results = records.search_by_name("Karl")
    for r in results:
        print(r)
    results = records.search_by_name("Shawn")
    for r in results:
        print(r)

    # Getting the student GPA:
    print("\nGetting the student GPA:")
    student = next((s for s in records.students if s.id_name[0] == "24-38720"), None)
    if student:
        gpa = student.calculate_gpa()
        letter = student.get_letter_grade(gpa)
        print(f"{student.id_name[1]}'s GPA: GPA: {gpa:.1f}, Grade: {letter}")
