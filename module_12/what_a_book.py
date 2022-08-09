import sys
import mysql.connector
from mysql.connector import errorcode


""" database config object """
config = {
    "user":"whatabook_user",
    "password": "MySQL8IsGreat!",
    "host":"127.0.0.1",
    "database":"whatabook",
    "raise_on_warnings":True
}
# Method to show menu options
def show_menu():
    print("Welcome to WhatABook Store \n")
    print("----- Main Menu -----")
    print("1: View Books \n")
    print("2: View Store Location \n")
    print("3: My Account \n")
    try:
        user_input = int(input('<Enter: 1 for book listing>: '))

        return user_input
    except ValueError:
        print("\n  Invalid number entered, program terminated...\n")

        sys.exit(0)

# Method to show book listing
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("\n  -- DISPLAYING ALL BOOK LISTING --")
    
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

# Method to show locations
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locations: "+ location[1] +"\n")

# Method to validate user id input
def validate_user():
    try:
        user_id = int(input('\nEnter your customer id <Example Enter 1 for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer id, program is terminating...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number, program is terminating...\n")

        sys.exit(0)
#Method to show customer account menu
def show_account_menu():
    try:
        print("\n -- CUSTOMER MENU --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        customer_account_option = int(input('<Example enter: 1 for wishlist>: '))

        return customer_account_option
    except ValueError:
        print("\n  Invalid number, program is terminating...\n")

        sys.exit(0)

# Method to show customer wishlist 
def show_wishlist(_cursor, user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
    
    wishlist = _cursor.fetchall()

    print("\n-- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

#Method to shows books to add to wishlist
def show_books_to_add(_cursor, user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))


    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

#Method to add the select book to wishlist
def add_book_to_wishlist(_cursor, user_id, book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id))
 

try:
    #Initiate connection to database
    db = mysql.connector.connect(**config) 

  
    cursor = db.cursor()
    
    #Get user input from main menu
    selected_user_input = show_menu() 
  
    while selected_user_input != 4:

        if selected_user_input == 1:
            show_books(cursor)

        if selected_user_input == 2:
            show_locations(cursor)

        if selected_user_input == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

    
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                if account_option == 2:

                    show_books_to_add(cursor, my_user_id)

                   
                    book_id = int(input("\n Enter the id of the book you want to add: "))
                    
                    
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() 

                    print("\n Book id: {} was added to your wishlist!".format(book_id))

                
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                
                account_option = show_account_menu()
        
    
        if selected_user_input < 0 or selected_user_input > 4:
            print("\n  Invalid option, please retry...")
            
        
        selected_user_input = show_menu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
   

    db.close()