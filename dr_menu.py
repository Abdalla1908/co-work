from users import Doctor
from Data import *
from menu import menu
from models import * 


def doctor_menu(doctor):
    while True:    
        print(dr_opt)
        
        choice = input("Write your choice : ")
        
        if choice == '1': #List Courses
            
            doctor.view_courses()
            
            doctor_menu(doctor=doctor)
        
        elif choice == '2': #Create course
            
            course_name = input("Course name : ")
            
            course_id   = input("course ID : ")
        
            
            doctor.create_course(course_name=course_name,course_id=course_id)
            
            doctor_menu(doctor)
        
        elif choice == '3': # View course
            
            doctor.view_courses()
            
            course_index  = int(input("Which course you want to view ?  "))
            
            course = doctor.courses[course_index-1]
            
            view_course_menu(course)
        
        
        
        elif choice == '4': # LOg Out
            
            menu.display_menu()
            break
        
        else : print("Invalid Choice") 
    
    
    
    
def view_course_menu(course):
    while True:
        print(f"Course {course.name} Menu:")
        print("1. List Assignments")
        print("2. Create Assignment")
        print("3. View Assignment")
        print("4. Back")

        choice = input("Write your choice: ")

        if choice == "1":
            course.list_assignments()
        elif choice == "2":
            assignment_id = input("Assignment ID: ")
            description = input("Description: ")
            assignment = Assignment(assignment_id, description)
            course.add_assignment(assignment)
            print(f"Assignment {assignment_id} created successfully.")
        elif choice == "3":
            course.list_assignments()
            assignment_index = int(input("Which assignment do you want to view? "))
            assignment = course.assignments[assignment_index - 1]
            view_assignment_menu(assignment)
        elif choice == "4":
            break
        else:
            print("Invalid choice")
            
def view_assignment_menu(assignment):
    while True:
        print(f"Assignment {assignment.id} Menu:")
        print(assignment_opt)

        choice = input("Write your choice: ")

        if choice == "1":
            print(f"Assignment Info:\nID: {assignment.id}\nDescription: {assignment.description}")
        elif choice == "2":
            print("Grades Report:")
            for student, grade in assignment.grades.items():
                print(f"Student: {student}, Grade: {grade}")
        elif choice == "3":
            print("List of Submissions:")
            for student, submission in assignment.submissions.items():
                print(f"Student: {student}, Submission: {submission}")
        elif choice == "4":
            student_username = input("Enter student username to view submission: ")
            if student_username in assignment.submissions:
                print(f"Submission: {assignment.submissions[student_username]}")
                print("1. Set Grade")
                print("2. Set a Comment")
                print("3. Back")
                sub_choice = input("Write your choice: ")
                if sub_choice == "1":
                    grade = input("Grade: ")
                    assignment.grade(student_username, grade)
                elif sub_choice == "2":
                    comment = input("Comment: ")
                    assignment.comment(student,comment)
                    print(f"Comment set for {student_username}")
                elif sub_choice == "3":
                    continue
                else:
                    print("Invalid choice")
            else:
                print("No submission found for this student.")
        elif choice == "5":
            break
        else:
            print("Invalid Choice")
