from users import *
from Data import *
from menu import *
from models import *

def std_menu(student):
    while True:
        print(st_opt)  # Display the main menu options
        
        choice = input("Write your choice: ")
        
        if choice == "1":
            course = input("What course do you want to register for? ")
            student.register_course(course)
        elif choice == '2':
            print("Courses list: ")
            student.view_mycourses()
        elif choice == '3':  # view courses
            print("Courses list: ")
            student.view_mycourses()
            course_index = int(input("Which course do you want to view? "))
            course = student.courses[course_index-1]
            course.view_assignments()
            print(sub_st_opt)  # Display the sub-menu options
            
            sub_choice = input("Write your choice: ")
            if sub_choice == "1":  # unregister from course
                student.unregister_course(course)
            elif sub_choice == "2":  # submit solution
                assignment_index = int(input("Which assignment do you want to submit? "))
                assignment = course.assignments[assignment_index-1]
                submission = input("Submission: ")
                student.submit_assignment(course_id=course.id, assignment_id=assignment.id, submission=submission)
            elif sub_choice == "3":  # Back
                continue  # Skip to the next iteration of the while loop (display the main menu again)
            else:
                print("Invalid choice")
                
        elif choice == '4':
            for course_ in student.courses:
                for assignment_ in course_.assignments:
                    student.grades(course_id=course_.id, assignment_id=assignment_.id)
        elif choice == '5':  # log out
            menu.display_menu()
            break  # Exit the loop and return to the main menu
        else:
            print("Invalid choice")