#Students Records
class Students:
    def __init__(self, student_id, student_name, email, grades= None, courses=None):
        self.id_name = (students_id, student_name)
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else []
