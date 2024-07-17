from auth import * 


class menu:
    def __init__(self) -> None:
        self.auth_ctrl = authcontrol()
    
    def display_menu(self):
        print('choose from the list :')
        print('Sign in -> write "1"')
        print('sign up -> write "2" ')
        
        choice = input('what is your choice : ')
        
        if   choice == '1':
            self.auth_ctrl.sign_in()
            
        elif choice == '2':
            self.auth_ctrl.sign_up()
        elif choice == '3':
            exit()
            
        else :
            print("invalid choice")
            
            