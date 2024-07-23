the code is about managing courses in command line interfac

# to run the code we start with calling 'menu' function
run the follwing :
```python
def menu():
    
    auth_control = load_data()
    
    while True:
        
            print('\nchoose from the list :')
            print('Sign in -> write "1"')
            print('sign up -> write "2" ')
            print("Shut Down -> 3")
        
            choice = input('what is your choice : ').strip()
        
            if   choice == '1':
                auth_control.sign_in(auth_control=auth_control)
            
            elif choice == '2':
                auth_control.sign_up(auth_control=auth_control)
            elif choice == '3': # shutdown
                save_data(auth_control)
                exit()
            
            else :
                print("invalid choice")

```
the result will be as that :
```python
<auth.Authcontrol object at 0x0000025249377EC0>
[<models.Course object at 0x000002524946B5F0>]    
[<models.Assignment object at 0x000002524946B710>]

choose from the list :
Sign in -> write "1"
sign up -> write "2"
Shut Down -> 3
what is your choice :

```
First 3 lines are to be sure that changes are saved if empty that's mean you are running the file for the first line and don't have any saving data

you just need to go with system 

# Users info be saved when signup and the other Data be saved only when Logout or shutdown system
That is the save function : 
```python
import pickle
import os
save_file = 'Data.pkl'

def save_data(auth_ctrl):
    with open(save_file,'wb') as file:
        data = {"auth_control":auth_ctrl,
                      "Courses" : Course.courses,
                      "Assignments" : Assignment.assignments}
        pickle.dump( data,file)

```

# As  we call the menu function to run the code it load the data we saved automatically 
that is the code of function:
```python
def load_data():
    if os.path.exists(save_file):
        with open (save_file,"rb") as file :
            data = pickle.load(file)
            print(data.get("auth_control"))
            print(data.get("Courses"))
            print(data.get("Assignments"))
        auth_control    = data.get('auth_control')
        Course.courses         = data.get('Courses',[])
        Assignment.assignments     = data.get("Assignments",[])
        
        return auth_control
    else:
        return Authcontrol()
```

it checks if there's a saved data file if there will load it if not will call the class  and as we say the print functions just to be sure we can remove it of course
# the Authcontrol start as that
it make list of users to save it into and have the functions of sign in and up 
```python
class Authcontrol :
    def __init__(self) -> None:
        self.users    = []
        self.username = []
    
    def sign_up(self,auth_control):
        
        username  = input("Enter your user name : ")
        
        password  = input("Enter your Password : ")
        full_name = input("Enter your Full Name : ")
        email     = input("Enter your valid email as (user@gmail.com) : ")
        role      = input('what is your role { Student , Doctor or TA } : ').strip()
        
        if not username :
            print("User name can't be empty")
            return
        
        if username not in self.username :
            if role.lower() == "student" :
                user = Student(username,password,full_name,email,role)
                self.users.append(user)
                save_data(self)
                print('User signed up sucessfuly')
                self.sign_in(auth_control=auth_control)
        
            elif role.lower() == 'doctor' :
                    user = Doctor(username,password,full_name,email,role)
                    self.users.append(user)
                    save_data(self)
                    print('User signed up sucessfuly')
                    self.sign_in(auth_control=auth_control)
            elif role.lower() == 'ta' :
                    user = TA(username,password,full_name,email,role)
                    self.users.append(user)
                    save_data(self)
                    print('User signed up sucessfuly')
                    self.sign_in(auth_control=auth_control)    
            
            
        else :
            print("User name is used by another one try with a different username")
        
        
        
    def sign_in(self,auth_control):
        username = input('Enter your user name : ')
        password = input("Enter your password : ")
        role     = input('what is your role { Student , Doctor or TA } : ')
        
        for user in self.users:
            if user.user_name == username and user.password == password and user.role == role :
                print(f'Welcome {user.full_name}')
                if role.lower() == "student" :
                    std_menu(user,auth_control)
                elif role.lower() == 'doctor' :
                    doctor_menu(user,auth_control)
                elif role.lower() == 'ta' :
                    ta_menu(user,auth_control)
                return
        print('invalid input data , chaeck your signin info')

```
as we see if some one go to signup after finish it goas automatically to signin function

# every user have a different menu from other user depending on User Role
# Student Menu 
when signin and Role is student that is what system calll
```python
def std_menu(student, auth_control):
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
            course.list_assignments()
            print(sub_st_opt)  # Display the sub-menu options
            
            sub_choice = input("Write your choice: ").strip()
            if sub_choice == "1":  # unregister from course
                try:
                    student.unregister_course(course_name=course.name)
                except Exception as e:
                    print(f"Error : {e}")
            elif sub_choice == "2":  # submit solution
                assignment_index = int(input("Which assignment do you want to submit? ")) - 1
                assignment = course.assignments[assignment_index]
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
```
it will be shown as this in output:

```python
choose from the list :
Sign in -> write "1"
sign up -> write "2"
Shut Down -> 3
what is your choice : 1
Enter your user name : abdo
Enter your password : 1234
what is your role { Student , Doctor or TA } : student
Welcome abdalla hassan

1).Register in course
2).list my courses
3). view course
4). Grades Report
5). Log out

Write your choice:
```
as this for every user depending on Role
