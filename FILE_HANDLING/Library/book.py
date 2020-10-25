from myprint import print_bar


class Book:
    def __init__(self,bookid, title,subject,author,available,issuedto,issuedate,returndate):
        self.bookid = bookid
        self.title = title
        self.subject = subject
        self.author = author
        self.available = available
        self.issuedto = issuedto
        self.issuedate = issuedate
        self.returndate = returndate

    def print_all(self):
        print(str(self.bookid).ljust(3),
              self.title[0:15].ljust(15),
              self.subject[0:15].ljust(15),
              self.author[0:15].ljust(15),
              str(self.available).ljust(10),
              str(self.issuedto).ljust(10),
              (self.issuedate.strftime("%d-%b-%y") if not self.available else "None").ljust(10),
              (self.returndate.strftime("%d-%b-%y") if not self.available else "None").ljust(10))

    def print_full(self):
        print_bar()
        print("Book #",self.bookid)
        print("Title: ", self.title)
        print("Subject: ", self.subject , " Author: " , self.author)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Issued to member#", self.issuedto,
                  " on ", self.issuedate.strftime("%d-%b-%y"),
                  " returns on ", self.returndate.strftime("%d-%b-%y"))
        print_bar()


def create_book(bookid):
    title = input("Enter the book title: ")
    subject = input("Enter the subject: ")
    author = input("Enter the author: ")
    available = True
    issuedto = None
    issuedate = None
    returndate = None
    return Book(bookid,title,subject,author,available,issuedto,issuedate,returndate)


def print_header():
    print("="*100)
    print("id".ljust(3),
          "title".ljust(15),
          "subject".ljust(15),
          "author".ljust(15),
          "available".ljust(10),
          "issued to".ljust(10),
          "issuedate".ljust(10),
          "returndate".ljust(10))
    print("="*100)