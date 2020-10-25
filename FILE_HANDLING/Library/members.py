"""

It provides all the functionalities to work with the members table

"""

from member import create_member,print_header
from datafile import DataFile
from datetime import datetime,timedelta

memberTable = DataFile("members.dat")


MEMBERSHIP_END_CHECK_DURATION=10*24*3600


def add_member():
    members = memberTable.get_records()
    if len(members) == 0:
        memberid = 0
    else:
        memberid = members[len(members)-1].memberid + 1
    member = create_member(memberid)
    memberTable.add_record(member)
    print("Operation Successful")


def get_and_print_member_list_by_name():
    members = memberTable.get_records()
    results = []
    if len(members) == 0:
        print("No Members found")
    else:
        name = input("Enter the name: ")
        words = name.split()

        for member in members:
            for word in words:
                if word.lower() in member.name.lower():
                    results.append(member)
        if len(results) == 0:
            print("No matching record")
        else:
            print(len(results), " matching records")
            print_header()
            for member in results:
                member.print_all()
    return results


def get_and_print_member_by_id():
    members = memberTable.get_records()
    found = False
    position = -1
    if len(members) == 0:
        print("No Members found")
    else:
        memberid = int(input("Enter the member id: "))
        for member in members:
            position+=1
            if memberid == member.memberid:
                found = True
                break
        if not found:
            print("No matching record")
        else:
            members[position].print_full()
    return members, found, position


def get_and_print_member_list_by_address():
    members = memberTable.get_records()
    results = []
    if len(members) == 0:
        print("No Members found")
    else:
        address = input("Enter the address: ")
        words = address.split()

        for member in members:
            for word in words:
                if word.lower() in member.address.lower():
                    results.append(member)
        if len(results) == 0:
            print("No matching record")
        else:
            print(len(results), " matching records")
            print_header()
            for member in results:
                member.print_all()
    return results


def get_and_print_member_list_by_phone():
    members = memberTable.get_records()
    results = []
    if len(members) == 0:
        print("No Members found")
    else:
        phone = input("Enter the phone: ")
        for member in members:
            if phone in member.phone:
                results.append(member)
        if len(results) == 0:
            print("No matching record")
        else:
            print(len(results), " matching records")
            print_header()
            for member in results:
                member.print_all()
    return results


def get_and_print_member_list_ending_soon():
    members = memberTable.get_records()
    results = []
    if len(members) == 0:
        print("No Members found")
    else:
        today = datetime.now()
        for member in members:
            if (member.expiry - today).total_seconds() <= MEMBERSHIP_END_CHECK_DURATION:
                results.append(member)
        if len(results) == 0:
            print("No matching record")
        else:
            print(len(results), " matching records")
            print_header()
            for member in results:
                member.print_all()
    return results


def edit_member_details():
    members,found,position = get_and_print_member_by_id()
    if found:
        member = members[position]
        print("Input new values (leave blank to keep previous value)")
        name = input("Enter new name: ")
        if len(name)>0:
            member.name = name
        address = input("Enter new address: ")
        if len(address)>0:
            member.address = address
        phone = input("Enter new phone: ")
        if len(phone)>0:
            member.phone = phone
        memberTable.overwrite(members)
        print("Operation Successful")


def delete_member():
    members, found, position = get_and_print_member_by_id()
    member = members[position]
    if found:
        print("Delete ", member.name , " (Y/N) : ")
        deleteconfirm = input()
        if deleteconfirm.lower() == 'y':
            members.remove(member)
            memberTable.overwrite(members)
            print("Operation Successful")
        else:
            print("Operation Canceled")


def member_menu():
    while True:
        print()
        print("==============================")
        print("==========Member Menu=========")
        print("==============================")
        print()
        print("1. Add Member")
        print("2. Show Member Details by name")
        print("3. Show Member Details by id")
        print("4. Show Member Details by address")
        print("5. Show Member Details by phone number")
        print("6. Show Members Whose Membership ending in 10 days")
        print("7. Edit Member Details")
        print("8. Delete Member")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_member()
        elif choice == 2:
            get_and_print_member_list_by_name()
        elif choice == 3:
            get_and_print_member_by_id()
        elif choice == 4:
            get_and_print_member_list_by_address()
        elif choice == 5:
            get_and_print_member_list_by_phone()
        elif choice == 6:
            get_and_print_member_list_ending_soon()
        elif choice == 7:
            edit_member_details()
        elif choice == 8:
            delete_member()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")