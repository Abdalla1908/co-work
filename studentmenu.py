from Data import *
from models import *
from users import Student
import auth


def std_menu(student,auth_control):
    while True:
        print(st_opt)  # Display the main menu options
        
        choice = input("Write your choice: ").strip()
        
        if choice == "1":
            course = input("What course do you want to register for? ")
            for c in Course.courses:
                if c.name == course:
                    break
            else:
                print("Invalid course name")
                continue
            try:
                student.register_course(course)
            except Exception as e:
                print(f"Error registering course: {e}")
                continue
        elif choice == '2':
            print("Courses list: ")
            student.view_mycourses()
            continue
        elif choice == '3':  # view courses
            print("Courses list: ")
            student.view_mycourses()
            course_index = int(input("Which course do you want to view? "))
            course = student.courses[course_index-1]
            course.view_student_assignments(student=student)
            print(sub_st_opt)  # Display the sub-menu options
            
            sub_choice = input("Write your choice: ").strip()
            if sub_choice == "1":  # unregister from course
                try:
                    student.unregister_course(course_name=course.name)
                except Exception as e:
                    print(f"Error : {e}")
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
            auth.save_data(auth_control)
            from menu import menu
            menu()
            break  # Exit the loop and return to the main menu
        else:
            print("Invalid choice")