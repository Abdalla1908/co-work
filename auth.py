from studentmenu import std_menu
from users import User,Student,TA,Doctor
from dr_menu import doctor_menu,view_course_menu,view_assignment_menu
from tamenu import ta_menu , invitations_menu
from models import Course,Assignment 
import pickle
import os

#Data_File = 'data.pkl'
save_file = 'Data.pkl'

def save_data(auth_ctrl):
    with open(save_file,'wb') as file:
        data = {"auth_control":auth_ctrl,
                      "Courses" : Course.courses,
                      "Assignments" : Assignment.assignments}
        pickle.dump( data,file)
        
        
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
        
        
        