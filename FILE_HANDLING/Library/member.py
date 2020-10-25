from datetime import datetime
from dateutil.relativedelta import relativedelta
from myprint import printbar

MEMBERSHIP_PERIOD=3


class Member:
    def __init__(self,memberid,name,address,phone,joining,expiry):
        self.memberid = memberid 
        self.name = name
        self.address = address
        self.phone = phone
        self.joining = joining
        self.expiry = expiry

    def printall(self):
        print(str(self.memberid).ljust(3),
              self.name[0:15].ljust(15),
              self.address[0:15].ljust(15),
              self.phone.ljust(15),
              self.joining.strftime("%d-%b-%y").ljust(15),
              self.expiry.strftime("%d-%b-%y").ljust(15))

    def printfull(self):
        printbar()
        print("Member #",self.memberid)
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Phone: ",self.phone)
        print("Joined on ", self.joining.strftime("%d-%b-%y"),
                  " membership ends on ", self.expiry.strftime("%d-%b-%y"))
        printbar()


def createmember(memberid):
    name = input("Enter the name: ");
    address = input("Enter the address: ")
    phone = input("Enter the phone: ")
    joining = datetime.now()
    expiry = joining + relativedelta(months=MEMBERSHIP_PERIOD)
    return Member(memberid,name,address,phone,joining,expiry)


def printheader():
    print("="*80)
    print("id".ljust(3),
          "name".ljust(15),
          "address".ljust(15),
          "phone".ljust(15),
          "joining".ljust(15),
          "expiry".ljust(15))
    print("="*80)
