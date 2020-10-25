from book import createbook,printheader
from datafile import DataFile
from datetime import datetime
from members import getandprintmemberbyid
from dateutil.relativedelta import relativedelta


bookTable = DataFile("books.dat")

BOOK_ISSUE_PERIOD = 7


def addbook():
    books = bookTable.getRecords()
    if len(books) == 0:
        bookid = 0
    else:
        bookid = books[len(books)-1].bookid + 1
    book = createbook(bookid)
    bookTable.addRecord(book)
    print("Operation Successful")


def getandprintbookbyid():
    books = bookTable.getRecords()
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
            books[position].printfull()
    return books, found, position


def getandprintbooklist():
    books = bookTable.getRecords()
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
                printheader()
                for book in results:
                    book.printall()
    return results


def searchbook():
    books = bookTable.getRecords()
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
                printheader()
                for book in results:
                    book.printall()


def searchbooksissuedbymember():
    books = bookTable.getRecords()
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
                printheader()
                for book in results:
                    book.printall()


def showbooksissuedbydate():
    books = bookTable.getRecords()
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
                printheader()
                for book in results:
                    book.printall()


def showbookstobereturnedtoday():
    books = bookTable.getRecords()
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
                printheader()
                for book in results:
                    book.printall()


def issuebook():
    books,found,position = getandprintbookbyid()
    if found:
        book = books[position]
        if not book.available:
            print("The book is not available")
            return
        members,found,position = getandprintmemberbyid()
        if found:
            member = members[position];
            if found:
                member.printall()
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


def returnbook():
    books,found,position = getandprintbookbyid()
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


def deletebook():
    books, found, position = getandprintbookbyid()
    if found:
        print("Delete the record (Y/N) : ")
        issueconfirm = input()
        if issueconfirm.lower() == 'y':
            books.pop(position)
            bookTable.overwrite(books)
            print("Operation Successful")
        else:
            print("Operation Canceled")


def bookmenu():
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
            addbook()
        elif choice == 2:
            getandprintbookbyid()
        elif choice == 3:
            searchbook()
        elif choice == 4:
            searchbooksissuedbymember()
        elif choice == 5:
            showbooksissuedbydate()
        elif choice == 6:
            showbookstobereturnedtoday()
        elif choice == 7:
            issuebook()
        elif choice == 8:
            returnbook()
        elif choice == 9:
            deletebook()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")
