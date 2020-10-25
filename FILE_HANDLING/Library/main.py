"""
    This file is the entry point of our
    Library Management System For CBSE project for 2020
"""
from books import bookmenu
from members import membermenu
from myprint import printcenter,inputcenter
if __name__ == '__main__':
    '''    
    It displays the main menu and transfer execution to 'members' module or 'books' module accordingly. After execution of
    any one of those modules, we come back here to exit the app by pressing 0.
    
    '''
    while True:
        print()
        printcenter("=============================")
        printcenter("=====Apka Guruji Library=====")
        printcenter("=============================")
        printcenter("1. Manage Books/Issue/Return")
        printcenter("2. Manage Members")
        printcenter("0. Exit")
        print()

        choice = int(inputcenter("Enter your choice: "))
        if choice == 1:
            bookmenu()
        elif choice == 2:
            membermenu()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to exit)")
    printcenter("GoodBye")