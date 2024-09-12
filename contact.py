import json
import os

contacts_file = 'contacts.json'
contacts = {}

def load_contacts():
    global contacts
    if os.path.exists(contacts_file):
        with open(contacts_file, 'r') as file:
            contacts = json.load(file)
    else:
        contacts = {}

def save_contacts():
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, email, phone):
    if name in contacts:
        print("Contact already exists.")
        return
    contacts[name] = {"email": email, "phone": phone}
    save_contacts()
    print(f"Contact '{name}' added successfully.")

def update_contact(name, email=None, phone=None):
    if name not in contacts:
        print("Contact not found.")
        return
    if email:
        contacts[name]["email"] = email
    if phone:
        contacts[name]["phone"] = phone
    save_contacts()
    print(f"Contact '{name}' updated successfully.")

def delete_contact(name):
    if name not in contacts:
        print("Contact not found.")
        return
    del contacts[name]
    save_contacts()
    print(f"Contact '{name}' deleted successfully.")

def search_contact(name):
    if name in contacts:
        print(f"Contact name '{name}':")
        print(f"Email: {contacts[name]['email']}")
        print(f"Phone: {contacts[name]['phone']}")
    else:
        print("Contact not found.")

def view_contact():
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print(f"\nContact name '{name}':")
        print(f"Email: {details['email']}")
        print(f"Phone: {details['phone']}")

def count_contact():
    print(f"Number of contacts: {len(contacts)}")

def main():
    load_contacts()
    while True:
        print("\nContact Management System:")
        print("1. Add contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. Search contact")
        print("5. View all contacts")
        print("6. Count contacts")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            add_contact(name, email, phone)

        elif choice == "2":
            name = input("Enter name: ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            phone = input("Enter new phone (leave blank to keep unchanged): ")
            update_contact(name, email if email else None, phone if phone else None)

        elif choice == "3":
            name = input("Enter name: ")
            delete_contact(name)

        elif choice == "4":
            name = input("Enter name: ")
            search_contact(name)

        elif choice == "5":
            view_contact()

        elif choice == "6":
            count_contact()

        elif choice == "7":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

