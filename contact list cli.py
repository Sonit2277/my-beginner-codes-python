contacts = {}
def add_contact(name, phone):
    contacts[name] = phone
def get_contact(name):    
     return contacts.get(name, "Contact not found")
def delete_contact(name):    
    if name in contacts:
        del contacts[name]
        return "Contact deleted"
    else:
        return "Contact not found"

def list_contacts():
    return contacts                                                                                                                        
while True:
    print("\n1. Add  2. Search  3. Delete  4. View All  5. Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        add_contact(name, phone)
        print("Contact added.")
    elif choice == "2":
        name = input("Name: ")
        print(get_contact(name))
    elif choice == "3":
        name = input("Name: ")
        print(delete_contact(name))
    elif choice == "4":
        print(list_contacts())
    elif choice == "5":
        break