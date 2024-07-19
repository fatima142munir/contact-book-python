# create an empty object to save user's contacts
contact = {}

# use while loop 
while True:
    print("\n******* CONTACT BOOK ********")
    # give options to user
    choice = int(input(" 1.New contact\n 2.Search contact\n 3.Edit contact number\n 4.Delete contact\n 5.Show Contacts\n Please Enter Your Choice\n "))
    # create program according to user's choice
    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter contact number: ")
        contact[name] = phone
    elif choice == 2:
        searchName = input("Enter search contact: ")
        if searchName in contact:
            print(searchName, "'s contact number is ", contact[searchName])
        else:
            print("Search name is not found in contact book")
    elif choice == 3:
        editContact = input("Enter contact name to edit: ")
        if editContact in contact:
            phone = input("Enter number: ")
            contact[editContact] = phone
            print("***Contact Updated***")
            for key in contact:
                print(key, contact.get(key))
        else:
            print("Name is not found in contact book")
    elif choice == 4:
        deleteContact = input("Enter contact to delete")
        if deleteContact in contact:
            contact.pop(deleteContact)
            print("Contact Deleted")
        else:
            print("Name is not found in contact book")
    elif choice == 5:
        print("***Saved Contacts***")
        for key in contact:
            print(key, contact.get(key))
    else:
        break

