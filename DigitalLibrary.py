# Variables
bookList = [
    {"bookID" : "whasty", "bookName" : "What Is Your Attachment Style?", "availability" : "Borrowed", "borrowedFor" : "3 days per 5-Feb", "borrowedBy" : "Vi"},
    {"bookID" : "theexi", "bookName" : "The Desire To Simply Not Exist", "availability" : "Borrowed", "borrowedFor" : "5 days per 7-Feb", "borrowedBy" : "Corgi"},
    {"bookID" : "optnih", "bookName" : "Optimistic Nihilism - By Kurzgesagt", "availability" : "Available", "borrowedFor" : "Currently Available", "borrowedBy" : None},
    {"bookID" : "noveff", "bookName" : "Nova Effect - Tragedy Of Good Luck", "availability" : "Available", "borrowedFor" : "Currently Available", "borrowedBy" : None},
    {"bookID" : "anadis", "bookName" : "An Antidote To Dissatisfaction", "availability" : "Available", "borrowedFor" : "Currently Available", "borrowedBy" : None}
    ]

from datetime import date
now = date.today()

# Functions
def fnSubMenu(fn, option):
    while True:
        subMenu = input(f'''
    1. {option}
    2. Back to Main Menu

    Please choose one of the submenu above (1-2): ''')
        if subMenu == "1":
            fn()  
        elif subMenu == "2":
            break
        continue

def fnSubMenu1(fn, option1, option2):
    while True:
        subMenu = input(f'''
    1. {option1}
    2. {option2}
    3. Back to Main Menu

    Please choose one of the submenu above (1-3): ''')
        if subMenu == "1":
            fn()  
        elif subMenu == "2":
            uniqueInput = input("    Enter Book ID of the book you would like to see: ")
            fn(uniqueInput)
        elif subMenu == "3":
            break
        continue

def fnShowBooks(unique = None):
    if unique == None:
        print('''    |   BookID   |              Book Title              |  Availability |     Borrowed For      |  Borrowed By  |''')
        for i in range (len(bookList)):
            print(f'''    |   {bookList[i]['bookID']}   | {bookList[i]['bookName']}\t| {bookList[i]['availability']}\t| {bookList[i]["borrowedFor"]}\t| {bookList[i]["borrowedBy"]}\t\t|    ''')
            continue
    elif unique != None:
        for i in range (len(bookList)):
            if bookList[i]['bookID'] == unique:
                print('''    |   BookID   |              Book Title              |  Availability |     Borrowed For      |  Borrowed By  |''')    
                print(f'''    |   {bookList[i]['bookID']}   | {bookList[i]['bookName']}\t| {bookList[i]['availability']}\t| {bookList[i]["borrowedFor"]}\t| {bookList[i]["borrowedBy"]}\t\t|    ''')
                break
        else:
            print("\n    Book does not exist")
        
def fnAddBooks():
    newBook = input("    Enter new book title (please keep it between 29 - 36 characters): ").title()
    newBookID = input(f"    Enter new Book ID for {newBook}: ").lower()
    for i in range (len(bookList)):
        if newBookID == bookList[i]["bookID"]:
            print("\n    This book is already registered")
            break
    else:
        while True:
            confirmation = input(f"    Are you sure you want to add '{newBook}' to the library? (Y/N): ").capitalize()
            if confirmation == "Y":
                bookList.append({"bookID" : newBookID, "bookName" : newBook, "availability" : "Available", "borrowedFor" : "Currently Available", "borrowedBy" : None})
                break
            elif confirmation == "N":
                print("\n    k then")
                break
            else:
                print("\n    ~~~ Wrong input, please try again. ~~~\n")
                continue
    fnShowBooks()

def fnDeleteBooks():
    fnShowBooks()
    deleteBook = input("\n    Enter Book ID of the book you would like to delete: ").lower()
    for i in range (len(bookList)):
        if deleteBook == bookList[i]["bookID"]:
            while True:
                confirmation = input(f"    Are you sure you want to delete '{bookList[i]['bookName']}'? (Y/N): ").capitalize()
                if confirmation == "Y":
                    del(bookList[i])
                    print("\n    Book has been deleted")
                    break
                elif confirmation == "N":
                    print("\n    k then")
                    break
                else:
                    print("\n    ~~~ Wrong input, please try again. ~~~\n")
                    continue
            break
    else:
        print("\n    Book does not exist")
    fnShowBooks()

def fnBorrowBooks():
    fnShowBooks()
    borrowBook = input("\n    Enter Book ID of the book you would like to borrow: ").lower()
    for i in range (len(bookList)):
        if borrowBook == bookList[i]["bookID"]:
            if bookList[i]["availability"] == "Available":
                borrowTime = int(input("\n    How long would you like to borrow the book for (days)? "))
                borrowName = input("\n    Who is borrowing this book? ").title()
                while True:
                    confirmation = input(f"    Are you sure you want to borrow '{bookList[i]['bookName']}' for {borrowTime} day(s)? (Y/N): ").capitalize()
                    if confirmation == "Y":
                        bookList[i]["availability"] = "Borrowed"
                        bookList[i]["borrowedFor"] = (f"{borrowTime} days per {now.day}-{now.strftime('%b')}")
                        bookList[i]["borrowedBy"] = borrowName
                        print(f"\n    You just borrowed '{bookList[i]['bookName']}' for {borrowTime} day(s). Make sure to return it in time!")
                        break
                    elif confirmation == "N":
                        print("\n    k then")
                        break
                    else:
                        print("\n    ~~~ Wrong input, please try again. ~~~\n")
                        continue
                break
            else:
                print("\n    Sorry, this book is currently unavailable :(")
                break
    else:
        print("\n    Book does not exist")

def fnReturnBooks():
    fnShowBooks()
    returnBook = input("\n    Enter Book ID of the book you would like to return: ").lower()
    for i in range (len(bookList)):
        if returnBook == bookList[i]["bookID"]:
            if bookList[i]["availability"] != "Available":
                while True:
                    confirmation = input(f"    Are you sure you want to return '{bookList[i]['bookName']}'? (Y/N): ").capitalize()
                    if confirmation == "Y":
                        bookList[i]["availability"] = "Available"
                        bookList[i]["borrowedFor"] = "Currently Available"
                        bookList[i]["borrowedBy"] = None
                        print(f"\n    Thank you for returning '{bookList[i]['bookName']}' in time!")
                        break
                    elif confirmation == "N":
                        print("\n    k then")
                        break
                    else:
                        print("\n    ~~~ Wrong input, please try again. ~~~\n")
                        continue
            else:
                print("\n    This book does not need to be returned.")
            break
    else:
        print("\n    Book does not exist")

# Loop
while True:
    mainMenu = input('''
    ======= Welcome to Digital Library =======
        
    1. Show Book(s)
    2. Add New Book(s)
    3. Delete Existing Book
    4. Borrow Book(s)
    5. Return Book(s)
    6. Exit Digital Library

    Please choose one of the menu from the above options (1-6): ''')

    if mainMenu == "1":
        fnSubMenu1(fnShowBooks, "Show All Books in the Library", "Show Book with Specific Book ID")

    elif mainMenu == "2":
        fnSubMenu(fnAddBooks, "Add New Book to The Library")

    elif mainMenu == "3":
        fnSubMenu(fnDeleteBooks, "Delete Existing Book from The Library") 

    elif mainMenu == "4":
        fnSubMenu(fnBorrowBooks, "Borrow Book from The Library")

    elif mainMenu == "5":
        fnSubMenu(fnReturnBooks, "Return Book to The Library")

    elif mainMenu == "6":
        print('''\n    Thank you for visiting Digital Library!
    The program will now close.''')
        break

    else:
        print('''\n    ~~~ Wrong input, please try again. ~~~''')