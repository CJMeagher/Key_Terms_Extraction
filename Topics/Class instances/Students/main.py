class Student:
    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = f"{self.name[0]}{self.last_name}{self.birth_year}"


in_name = input()
in_last_name = input()
in_birth_year = input()

student = Student(in_name, in_last_name, in_birth_year)
print(student.student_id)
