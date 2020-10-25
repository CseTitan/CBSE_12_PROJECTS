from books import book_menu
from members import membermenu
from myprint import print_center, input_center


if __name__ == '__main__':
    while True:
        print()
        print_center("=============================")
        print_center("=====Apka Guruji Library=====")
        print_center("=============================")
        print_center("1. Manage Books/Issue/Return")
        print_center("2. Manage Members")
        print_center("0. Exit")
        print()

        choice = int(input_center("Enter your choice: "))
        if choice == 1:
            book_menu()
        elif choice == 2:
            membermenu()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to exit)")
    print_center("GoodBye")