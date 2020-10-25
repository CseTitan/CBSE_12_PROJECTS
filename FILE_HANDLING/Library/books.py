from book import create_book, print_header
from datafile import DataFile
from datetime import datetime
from members import getandprintmemberbyid
from dateutil.relativedelta import relativedelta


bookTable = DataFile("books.dat")

BOOK_ISSUE_PERIOD = 7


def add_book():
    books = bookTable.get_records()
    if len(books) == 0:
        bookid = 0
    else:
        bookid = books[len(books)-1].bookid + 1
    book = create_book(bookid)
    bookTable.add_record(book)
    print("Operation Successful")


def get_and_print_book_by_id():
    books = bookTable.get_records()
    found = False
    position = -1
    if len(books) == 0:
        print("No Record found")
    else:
        bookid = int(input("Enter the id: "))
        for book in books:
            position+=1
            if bookid == book.bookid:
                found = True
                break
        if not found:
            print("No matching record")
        else:
            books[position].print_full()
    return books, found, position


def get_and_print_book_list():
    books = bookTable.get_records()
    results = []
    if len(books)== 0:
        print("No books found")
    else:
        str = input("Enter the topic: ")
        words = str.split()
        
        for book in books:
            for word in words:
                if word in book.title.lower() or word in book.subject.lower() or word in book.author.lower():
                    results.append(book)
        if len(results)==0:
                print("No matching book")
        else:
                print(len(results) ," matching books")
                print_header()
                for book in results:
                    book.print_all()
    return results


def search_book():
    books = bookTable.get_records()
    if len(books)== 0:
        print("No books found")
    else:
        str = input("Enter the topic: ")
        words = str.split()
        results = []
        for book in books:
            for word in words:
                if word in book.title.lower() or word in book.subject.lower():
                    results.append(book)
        if len(results)==0:
                print("No matching book")
        else:
                print(len(results) ," matching books")
                print_header()
                for book in results:
                    book.print_all()


def search_books_issued_by_member():
    books = bookTable.get_records()
    if len(books) == 0:
        print("No records found")
    else:
        memberid = int(input("Enter the id: "))
        results = []
        for book in books:
            if book.issuedto == memberid:
                results.append(book)
        if len(results) == 0:
                print("currently no books issued to this member")
        else:
                print(len(results), " matching books")
                print_header()
                for book in results:
                    book.print_all()


def show_books_issued_by_date():
    books = bookTable.get_records()
    if len(books)== 0:
        print("No books found")
    else:
        day = int(input("Enter the day of month: "))
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))
        issuedate = datetime(year,month,day)
        results = []
        for book in books:
            if book.issuedate.date() == issuedate.date():
                results.append(book)
        if len(results) == 0:
                print("no matching records")
        else:
                print(len(results), " matching books")
                print_header()
                for book in results:
                    book.print_all()


def show_books_to_be_returned_today():
    books = bookTable.get_records()
    if len(books)== 0:
        print("No books found")
    else:
        today = datetime.today()
        results = []
        for book in books:
            if book.returndate.date() == today.date():
                results.append(book)
        if len(results) == 0:
                print("No matching records")
        else:
                print(len(results), " matching books")
                print_header()
                for book in results:
                    book.print_all()


def issue_book():
    books,found,position = get_and_print_book_by_id()
    if found:
        book = books[position]
        if not book.available:
            print("The book is not available")
            return
        members,found,position = getandprintmemberbyid()
        if found:
            member = members[position];
            if found:
                member.print_all()
                print("Issue the book \"", book.title , "\" to " , member.name," (Y/N) : ")
                issueconfirm = input()
                if issueconfirm.lower() == 'y':
                    book.issuedto = member.memberid
                    book.issuedate = datetime.now()
                    book.available = False
                    book.returndate = book.issuedate + relativedelta(days=7)
                    bookTable.overwrite(books)
                    print("Operation Successful")
                else:
                    print("Operation Canceled")


def return_book():
    books,found,position = get_and_print_book_by_id()
    if found:
        book = books[position]
        if book.available:
            print("The book is already in the library")
            return
        book.issuedto = None
        book.issuedate = None
        book.available = True
        book.returndate = None
        bookTable.overwrite(books)
        print("Operation Successful")


def delete_book():
    books, found, position = get_and_print_book_by_id()
    if found:
        print("Delete the record (Y/N) : ")
        issueconfirm = input()
        if issueconfirm.lower() == 'y':
            books.pop(position)
            bookTable.overwrite(books)
            print("Operation Successful")
        else:
            print("Operation Canceled")


def book_menu():
    while True:
        print()
        print("============================")
        print("==========Book Menu=========")
        print("============================")
        print()

        print("1. Add Book")
        print("2. get book details by id")
        print("3. Search books")
        print("4. Show Books issued by a member")
        print("5. Show Books issued on specific date")
        print("6. Show Books that should be returned today")
        print("7. Issue A book")
        print("8. Return a book")
        print("9. Delete Book")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book()
        elif choice == 2:
            get_and_print_book_by_id()
        elif choice == 3:
            search_book()
        elif choice == 4:
            search_books_issued_by_member()
        elif choice == 5:
            show_books_issued_by_date()
        elif choice == 6:
            show_books_to_be_returned_today()
        elif choice == 7:
            issue_book()
        elif choice == 8:
            return_book()
        elif choice == 9:
            delete_book()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")
