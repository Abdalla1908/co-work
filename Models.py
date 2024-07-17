from users import *


class Course:
    def __init__(self, name: str, id: str, doctor: str) -> None:
        self.name = name
        self.id = id
        self.doctor = doctor
        self.assignments = []
        self.students = []
        self.ta = []

    def add_assignment(self, assignment) -> None:
        self.assignments.append(assignment)
        print(f"Added assignment: {assignment}")

    def add_student(self, student) -> None:
        self.students.append(student)
        print(f"Added student: {student.full_name}")

    def add_ta(self, ta):
        self.ta.append(ta)
        print(f'{ta.name} has been assigned to course {self.name}')

    def info(self) -> None:
        registered_students = ", ".join(student.full_name for student in self.students)
        print(f"Course {self.name} with code {self.id} - taught by Dr. {self.doctor}")
        print(f"Registered Students: {registered_students}")

    

    def __repr__(self) -> str:
        return f"Course {self.name} with code {self.id} - taught by Dr. {self.doctor}\nhas {len(self.assignments)} Assignments"


class Assignment:
    def __init__(self, id: str, description: str) -> None:
        self.id = id
        self.description = description
        self.submissions = {}
        self.grades = {}
        self.commits = {}

    def submit(self, student, submission: str) -> None:
        self.submissions[student.user_name] = submission
        print(f"Assignment submitted by {student.full_name}")

    def grade(self, student, grade: str) -> None:
        if student.user_name in self.submissions:
            self.grades[student.user_name] = grade
            print(f"Assignment graded for {student.full_name} with grade: {grade}")
        else:
            print(f"No submission found for {student.full_name}")
    def comment(self, student, comment: str) -> None:
        if student.user_name in self.submissions:
            self.grades[student.user_name] = comment
            print(f"Assignment graded for {student.full_name} with grade: {comment}")
        else:
            print(f"No submission found for {student.full_name}")

    def __str__(self) -> str:
        return f"Assignment(ID: {self.id}, Description: {self.description})"