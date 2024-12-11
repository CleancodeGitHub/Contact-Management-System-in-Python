import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass
class Contact:
    name: str
    age: int
    email: str

class ContactManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.contacts: List[Contact] = []
        self.load_contacts()

    def load_contacts(self) -> None:
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.contacts = [Contact(**contact) for contact in data["contacts"]]
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty contact list.")
        except json.JSONDecodeError:
            print(f"Error reading {self.filename}. Starting with an empty contact list.")

    def save_contacts(self) -> None:
        with open(self.filename, "w") as f:
            json.dump({"contacts": [asdict(contact) for contact in self.contacts]}, f, indent=2)

    def add_contact(self) -> None:
        name = input("Name: ")
        while True:
            try:
                age = int(input("Age: "))
                break
            except ValueError:
                print("Please enter a valid integer for age.")
        email = input("Email: ")
        
        new_contact = Contact(name, age, email)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def display_contacts(self, contacts: List[Contact]) -> None:
        if not contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(contacts, 1):
                print(f"{i}. {contact.name} | Age: {contact.age} | Email: {contact.email}")

    def delete_contact(self) -> None:
        self.display_contacts(self.contacts)
        if not self.contacts:
            return

        while True:
            try:
                index = int(input("Enter the number of the contact to delete: ")) - 1
                if 0 <= index < len(self.contacts):
                    deleted_contact = self.contacts.pop(index)
                    print(f"Deleted contact: {deleted_contact.name}")
                    break
                else:
                    print("Invalid number, out of range.")
            except ValueError:
                print("Please enter a valid integer.")

    def search_contacts(self) -> None:
        search_term = input("Enter a name to search for: ").lower()
        results = [contact for contact in self.contacts if search_term in contact.name.lower()]
        self.display_contacts(results)

    def run(self) -> None:
        print("Welcome to the Contact Management System!")
        
        while True:
            print("\nContact list size:", len(self.contacts))
            command = input("You can 'Add', 'Delete', 'Search', or 'Q' to quit: ").lower()

            if command == "add":
                self.add_contact()
            elif command == "delete":
                self.delete_contact()
            elif command == "search":
                self.search_contacts()
            elif command == "q":
                break
            else:
                print("Invalid command.")

        self.save_contacts()
        print("Thank you for using the Contact Management System. Goodbye!")

if __name__ == "__main__":
    manager = ContactManager("contacts.json")
    manager.run()

# Demonstration of the program
print("Demonstration of the Contact Management System:")
manager = ContactManager("demo_contacts.json")

print("\nAdding contacts:")
manager.contacts = [
    Contact("Alice Smith", 30, "alice@example.com"),
    Contact("Bob Johnson", 25, "bob@example.com"),
    Contact("Charlie Brown", 35, "charlie@example.com"),
    Contact("David Lee", 28, "david@example.com"),
    Contact("Emma Wilson", 33, "emma@example.com"),
    Contact("Frank Miller", 40, "frank@example.com"),
    Contact("Grace Taylor", 22, "grace@example.com"),
    Contact("Henry Davis", 37, "henry@example.com"),
    Contact("Ivy Chen", 31, "ivy@example.com")

]
manager.display_contacts(manager.contacts)

print("\nSearching for 'oh':")
manager.search_contacts()  # Assume user inputs "oh"

print("\nDeleting contact:")
manager.delete_contact()  # Assume user inputs "2"

print("\nFinal contact list:")
manager.display_contacts(manager.contacts)

manager.save_contacts()
print("\nContacts saved to demo_contacts.json")