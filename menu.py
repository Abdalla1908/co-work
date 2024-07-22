from auth import Authcontrol , load_data , save_data
import models

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
            elif choice == '3':
                save_data(auth_control)
                exit()
            
            else :
                print("invalid choice")
            
            
    
            
            
menu()