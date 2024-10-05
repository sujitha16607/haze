# Contact Book Program

# Initialize an empty contact book
contact_book = {}

# Function to add a contact
def add_contact(name, phone_number):
    contact_book[name] = phone_number
    print(f"Contact '{name}' added successfully.")

# Function to search for a contact
def search_contact(name):
    if name in contact_book:
        print(f"Name: {name}, Phone Number: {contact_book[name]}")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Function to display all contacts
def display_contacts():
    if contact_book:
        print("Contact Book:")
        for name, phone_number in contact_book.items():
            print(f"Name: {name}, Phone Number: {phone_number}")
    else:
        print("Contact book is empty.")

# Main program loop
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            add_contact(name, phone_number)
        elif choice == '2':
            name = input("Enter the name to search: ")
            search_contact(name)
        elif choice == '3':
            name = input("Enter the name to delete: ")
            delete_contact(name)
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()