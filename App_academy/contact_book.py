contacts = [{
    'name': '',
    'phone': '',
    'email': '',
}]

def add_contact(name, phone, email):
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email
    })

def search_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None

def delete_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            return True
    return False

def view_all():
    result = "These are all your contacts:\n"
    for contact in contacts:
        result += f"  Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}\n"
    return result


while True:
    action = input("Choose an action: 1=add, 2=search, 3=delete, 4=view, or 5=exit: ").lower()
    if action == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")
        email = input("Enter contact email: ")
        add_contact(name, phone, email)
        print(f"Contact {name} added successfully.")
    elif action == '2':
        name = input("Enter contact name to search: ")
        contact = search_contact(name)
        if contact:
            print(f"Contact found: {contact}")
        else:
            print("Contact not found.")
    elif action == '3':
        name = input("Enter contact name to delete: ")
        if delete_contact(name):
            print(f"Contact {name} deleted successfully.")
        else:
            print("Contact not found.")
    elif action == '4':
        if len(contacts) == 1 and contacts[0]['name'] == '':
            print("No contacts available.")
        print(view_all())
    elif action == '5':
        break
    else:
        print("Invalid action. Please try again.")  