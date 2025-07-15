# Contact book 
contacts = []
# Add contact
def add_contact():
    print("Add a new contact")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact saved!\n")
# Show all contacts
def show_contacts():
    if not contacts:
        print("No contacts yet.\n")
    else:
        print(" All Contacts:")
        for c in contacts:
            print(f"Name: {c['name']}, Phone: {c['phone']}")
        print()
# Search by name or phone
def search_contact():
    key = input("Search by name or phone: ")
    found = False
    for c in contacts:
        if key.lower() in c["name"].lower() or key in c["phone"]:
            print(" Contact found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}\n")
            found = True
    if not found:
        print("Contact not found.\n")
# Update contact
def update_contact():
    name = input("Enter the name to update: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            print("Enter new details (leave blank to keep same):")
            new_phone = input("New phone: ")
            new_email = input("New email: ")
            new_address = input("New address: ")
            if new_phone:
                c["phone"] = new_phone
            if new_email:
                c["email"] = new_email
            if new_address:
                c["address"] = new_address
            print("Contact updated!\n")
            return
    print("Name not found.\n")
# Delete contact
def delete_contact():
    name = input("Enter the name to delete: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            print("Contact deleted!\n")
            return
    print("Name not found.\n")
# Menu
def menu():
    while True:
        print("==== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")    
        choice = input("Choose (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option.\n")
# Start the program
menu()

