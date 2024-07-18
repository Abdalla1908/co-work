from models import *


from models import Course,Assignment
import re

class User:
    counter_id = 41220001

    def __init__(self, user_name: str, password: str, full_name: str, email: str, role: str) -> None:
        self.user_id = User.counter_id
        User.counter_id += 1

        self.user_name = user_name
        self.password = self.validate_password(password)
        self.full_name = full_name
        self.email = self.validate_email(email)
        self.role = role

    def validate_email(self, email: str) -> str:
        email_regex = r'^[a-zA-Z]+[a-zA-Z0-9._%+-]*@gmail\.com$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format. Must be in the format user@gmail.com.")
        return email

    def validate_password(self, password: str) -> str:
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long.")
        return password

    def __repr__(self) -> str:
        return f"{self.role} {self.full_name} with user ID {self.user_id}"
        
class Student(User):
    def __init__(self, user_name: str, password: str, full_name: str, email: str, role='Student') -> None:
        super().__init__(user_name, password, full_name, email, role)
        
        self.courses     = []
        self.assignments = []
        
    def register_course(self, course):
        course.add_student(self)
        self.courses.append(course)
        print(f"Registered in course: {course.id}")
        
    def unregister_course(self,course):
        course.students.pop(self)
        self.courses.pop(course)
        print('You have not been in course any more')

    def view_mycourses(self):
        if self.courses:
            for i, course in enumerate(self.courses, start=1):
                print(f"{i}. {course.name}")
        else:
            print("You have not enrolled in any courses yet")

    def submit_assignment(self, course_id, assignment_id, submission):
        for course in self.courses:
            if course.id == course_id:
                for assignment in course.assignments:
                    if assignment.id == assignment_id:
                        assignment.submit(self, submission)
                        return
                print(f"Assignment with ID {assignment_id} not found")
                return
        print(f"Course with ID {course_id} not found")
        
    def grades(self, course_id, assignment_id):
        for course in self.courses:
            if course.id == course_id:
                for assignment in course.assignments:
                    if assignment.id == assignment_id:
                        print(f"{assignment.id}: {assignment.grades.get(self.user_name, 'No grade')}")
                        return
                print(f"Assignment with ID {assignment_id} not found")
                return
        print(f"Course with ID {course_id} not found")
        
    def view_course_assignments(self, course_index):
        course = self.courses[course_index]
        course.view_assignments()
        
    def __repr__(self) -> str:
        if self.courses:
            course_list = ' '.join(course.id for course in self.courses)
            return f"{super().__repr__()} Registered in {len(self.courses)} courses. Course List: {course_list}"
        else:
            return f"{super().__repr__()} Not registered in any course yet"
        
        
class Doctor(User):
    def __init__(self, user_name: str, password: str, full_name: str, email: str, role='Doctor') -> None:
        super().__init__(user_name, password, full_name, email, role)
        self.courses = []

    def create_course(self, course_name, course_id):
        course = Course(name=course_name, id=course_id, doctor=self)
        self.courses.append(course)
        print(f"Course {course_name} with ID {course_id} has been created successfully")

    def invite_ta(self, ta, course_id):
        for course in self.courses:
            if course.id == course_id:
                ta.receive_invitation(self, course)
                return
        print(f"Course with ID {course_id} not found.")

    def view_courses(self):
        if self.courses:
            print("Courses:")
            for course in self.courses:
                print(f"Course ID: {course.id}, Name: {course.name}")
        else:
            print('You are not teaching any courses yet.')

    def handle_ta_response(self, ta, course_id, accepted):
        for course in self.courses:
            if course.id == course_id:
                if accepted:
                    print(f"TA {ta.full_name} has accepted the invitation for course {course.name}.")
                else:
                    print(f"TA {ta.full_name} has rejected the invitation for course {course.name}.")
                return
        print(f"Course with ID {course_id} not found.")

    def create_assignment(self, course_id, assignment_id, description):
        for course in self.courses:
            if course.id == course_id:
                assignment = Assignment(assignment_id, description)
                course.add_assignment(assignment)
                print(f"Assignment {assignment_id} created successfully for course {course_id}.")
                return
        print(f"Course with ID {course_id} not found.")

    def grade_assignment(self, course_id, assignment_id, student, grade):
        for course in self.courses:
            if course.id == course_id:
                for assignment in course.assignments:
                    if assignment.id == assignment_id:
                        assignment.grade(student, grade)
                        return
                print(f"Assignment with ID {assignment_id} not found.")
                return
        print(f"Course with ID {course_id} not found.")

    def __repr__(self) -> str:
        if self.courses:
            course_list = ', '.join(course.id for course in self.courses)
            return f'{super().__repr__()} teaching {len(self.courses)} courses: {course_list}'
        else:
            return f'{super().__repr__()} not teaching any courses yet.'

        
    
    
class TA(User):
    def __init__(self, user_name: str, password: str, full_name: str, email: str, role: str) -> None:
        super().__init__(user_name, password, full_name, email, role)
        self.courses = []
        self.invitations = []

    def view_courses(self):
        if self.courses:
            print("Courses List : ")
            for i , course in enumerate(self.courses,start=1):
                print(f'{i} ). {course.name}')
                
        else : print("You have not assigned to any course yet")
        
    def receive_invitation(self, doctor, course):
        invitation = (doctor, course)
        self.invitations.append(invitation)
        print(f"Received invitation from Doctor {doctor.full_name} for course {course.name}")

    def view_invitations(self):
        if self.invitations:
            print("Pending Invitations:")
            for i, (doctor, course) in enumerate(self.invitations, start=1):
                print(f"{i}. From Doctor {doctor.full_name} for course {course.name}")
        else:
            print("You have no pending invitations.")

    def accept_invitation(self, invitation_index):
        if 1 <= invitation_index <= len(self.invitations):
            doctor, course = self.invitations[invitation_index - 1]
            doctor.handle_ta_response(self, course.id, accepted=True)
            self.courses.append(course)
            del self.invitations[invitation_index - 1]
        else:
            print("Invalid invitation index.")

    def reject_invitation(self, invitation_index):
        if 1 <= invitation_index <= len(self.invitations):
            doctor, course = self.invitations[invitation_index - 1]
            doctor.handle_ta_response(self, course.id, accepted=False)
            del self.invitations[invitation_index - 1]
        else:
            print("Invalid invitation index.")

    def create_assignment(self, course_id, assignment_id, description):
        for course in self.courses:
            if course.id == course_id:
                assignment = Assignment(assignment_id, description)
                course.add_assignment(assignment)
                print(f"Assignment {assignment_id} created successfully for course {course_id}.")
                return
        print(f"Course with ID {course_id} not found.")

    def __repr__(self) -> str:
        if self.courses:
            course_list = ' '.join(course.id for course in self.courses)
            return f"{super().__repr__()} TA for {len(self.courses)} courses. Course List: {course_list}"
        else:
            return f"{super().__repr__()} Not assigned to any courses yet."


                 