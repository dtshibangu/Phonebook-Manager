''' This program keeps names and email addresses in a dictionary as key value
pairs, displays menu for lookup, adding, changing, deleting, then pickle when
program exits'''

# import pickle module
import pickle

# menu choices
LOOKUP = 1
ADD = 2
DELETE = 3
EDIT = 4
QUIT = 5

def main():
    # get saved info from file
    infile = open( 'address_book.dat','rb' )

    # loads saved data, if file is empty then
    # skips past eof error to fill file 
    try:
        load_data = pickle.load( infile )
    except EOFError:
        load_data = 0 

    #create empty dictionary
    address_book = {}

    # updates address book to saved data when file opens
    address_book.update( dict( load_data ) )  

    # initalize choice
    choice = 0

    while choice != QUIT:
        # get user menu choice
        choice = menu_choice()

        if choice == LOOKUP:
            look_up( address_book )
        elif choice == ADD:
            add( address_book )
        elif choice == DELETE:
            delete( address_book )
        elif choice == EDIT:
            edit( address_book )

    # if finished, opens file in writing mode,
    # saves data through write mode, and prints prompt
    if choice == QUIT:
        outfile = open( 'address_book.dat', 'wb' ) 
        save_data( address_book, outfile )
        print( "Your file is saved." ) 

    # close file
    infile.close()

def menu_choice(): 
    print( "EMAIL ADDRESS BOOK" )
    print( "------------------------------" )
    print( "1. LOOKUP EMAIL" )
    print( "2. ADD EMAIL" )
    print( "3. DELETE EMAIL" )
    print( "4. EDIT EMAIL" )

    # get user choice
    choice = int( input( "Enter your choice: " ) )

    # validate choice
    while choice < LOOKUP or choice > QUIT:
        choice = int( input( "Enter a valid choice: " ) )

    # return your choice
    return choice

# the lookup function returns the email of the person
# entered by the user
def look_up( dictionary ):
    # prompt for name look up or email lookup
    name = input( "Enter name: " )
    print( dictionary.get( name, "Not Found." ) )
    print()

        
# the add function adds a new entry to the address book
def add( dictionary ):
    name = input( "Enter a name: " )
    address = ''
    while "@" not in address:
        address = input( "Enter valid email: " )

    if name not in dictionary: 
         dictionary[ name ] = address
    else:
        print( "That name already exists." )

    print()


# the delete function removes an entry from dictionary
def delete( dictionary ):
    name = input( "Enter name to be deleted: " )

    if name in dictionary:
        del dictionary[ name ]
    else:
        print( "That name is not found." )

    print()


# the edit function allows one to change an email in
# the address book
def edit( dictionary ):
    name = input( "Enter name to edit: "  )
    if name in dictionary:
        # get new email
        email = input( "Enter new email: " )

    # update dictionary
    dictionary[ name ] = email

    print()

# the save_data function stores information from dictionary
# to a data file
def save_data( dictionary, file ):
    pickle.dump( dictionary, file ) 

# call the main function
main()
