# Contact list (dictionary)
contacts = {
    "Amit":"9876543210",
    "Riya":"9123456780"
}

# Add contact
def add_contact(name, number):
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = number
        print(f"{name} added successfully!")

# Search contact
def search_contact(name):
    if name in contacts:
        print(f"Contact Found: {name} -> {contacts[name]}")
    else:
        print("Contact not found!")

# Delete contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully!")
    else:
        print("Contact not found!")

# Show all contacts
def show_contacts():
    if contacts:
        print("\nAll Contacts:")
        for name, number in contacts.items():
            print(name, "->", number)
    else:
        print("No contacts available!")

# Menu
while True:
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)

    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "4":
        show_contacts()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")