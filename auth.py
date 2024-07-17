from users import *
from models import *

class authcontrol :
    def __init__(self) -> None:
        self.users    = []
        self.username = []
    def sign_up(self):
        username  = input("Enter your user name : ")
        
        password  = input("Enter your Password : ")
        full_name = input("Enter your Full Name : ")
        email     = input("Enter your valid email as (user@gmail.com) : ")
        role      = input('what is your role { Student , Doctor or TA } : ')
        
        if username not in self.username :
            user = User(username,password,full_name,email,role)
            self.users.append(user)
            print('User signed up sucessfuly')
            self.sign_in()
        else :
            print("User name is used by another one try with a different username")
        
        
        
    def sign_in(self):
        username = input('Enter your user name : ')
        password = input("Enter your password : ")
        role     = input('what is your role { Student , Doctor or TA } : ')
        
        for user in self.users:
            if user.name == username and user.password == password and user.role == role :
                print(f'Welcome {user.fullname}')
                return
        print('invalid input data , chaeck your signin info')
        
        if role.lower() == "student" :
            pass
        elif role.lower() == 'doctor' :
            pass
        elif role.lower() == 'ta' :
            pass
        
        