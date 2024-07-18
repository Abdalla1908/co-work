from users import TA
from Data import ta_opt
from models import Course, Assignment

def ta_menu(ta):
    while True:
        print(ta_opt)
        choice = input("\nwrite your choice : ")
        if choice == "1" : # show courses
            ta.view_courses()    
        elif choice == "2" : #Invitations
            ta.view_invetations()
            
            invitations_menu(ta=ta)
    
        elif choice == "3" :  #  Create Assignment
            course_id = input("Course ID : ")
            assignment_id = input("Assignment ID")
            description   = input("Description : ")
            
            ta.create_assignment(course_id=course_id,assignment_id=assignment_id,description=description)
            
        elif choice == "4" :  # Log Out
            menu.display_menu()
            break
            
        else :
            print("Invalid Choice")
    
    
def invitations_menu(ta):
    while True:
    
        print("1).Aceeebt Invetation")
        print("2). Reject Invetation")
        print("3).Back")
    
        sub_choice = input("Your choice : ")
        
        
        if sub_choice == "1" : 
            invitation_index = int(input("Which invetation : ")) -1
            
            ta.accept_invitation(invitation_index = invitation_index )
            
        elif sub_choice == "2" :
            invitation_index = int(input("Which invetation : ")) -1
            
            ta.reject_invitation(invitation_index = invitation_index )
            
        elif sub_choice == "3" : 
            break
        else :
            print("Invalid choice")
            
    
    