class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def buildLPS(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(f"{current.data.name} - {current.data.phone_number}")
            current = current.next

    def display_backward(self):
        current = self.tail
        while current:
            print(f"{current.data.name} - {current.data.phone_number}")
            current = current.prev

    def find(self, name):
        current = self.head
        while current:
            if current.data.name == name:
                return current.data
            current = current.next
        return None

    def delete(self, name):
        current = self.head
        while current:
            if current.data.name == name:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return True
            current = current.next
        return False

# Hash table for exact name lookup
contacts_hash = dict()
# Double linked list for ordered storage
contacts_list = DoubleLinkedList()

# Search by keyword 
def search_by_keyword(keyword):
    results = []
    current = contacts_list.head
    while current:
        if keyword.lower() in current.data.name.lower():
            results.append(current.data)
        current = current.next
    return results

# Search by keyword using KMP algorithm
def kmp_search(text, pattern):
    lps = buildLPS(pattern)
    i = j = 0

    while i < len(text):
        if text[i].lower() == pattern[j].lower():
            i += 1
            j += 1
            if j == len(pattern):
                return True
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

# Menu principal
def menu():
    while True:
        print("\n--- Gestion des Contacts ---")
        print("1. Add a contact")
        print("2. Search by keyword")
        print("3. Search by exact name")
        print("4. Display all contacts (forward)")
        print("5. Display all contacts (backward)")
        print("6. Delete a contact")
        print("7. Search by keyword (KMP Algorithm)")
        print("8. Quit")
        
        option = input("Entrez votre choix: ")

        if option == "1":
            name = input("Name: ")
            phone = input("Phone number: ")
            contact = Contact(name, phone)
            contacts_list.append(contact)
            contacts_hash[name] = contact
            print("Contact added.")

        elif option == "2":
            keyword = input("Keyword: ")
            results = search_by_keyword(keyword)
            if results:
                print("Contacts found:")
                for c in results:
                    print(f"{c.name} - {c.phone_number}")
            else:
                print("No contacts found.")
        elif option == "3":
            name = input("Exact name: ")
            contact = contacts_hash.get(name)
            if contact:
                print(f"Contact found: {contact.name} - {contact.phone_number}")
            else:
                print("No contact found.")

        elif option == "4":
            print("Contacts (forward):")
            contacts_list.display_forward()

        elif option == "5":
            print("Contacts (backward):")
            contacts_list.display_backward()

        elif option == "6":
            name = input("Name of contact to delete: ")
            deleted = contacts_list.delete(name)
            if deleted:
                contacts_hash.pop(name, None)
                print("Contact deleted.")
            else:
                print("Contact not found.")

        elif option == "7":
            print("Search by keyword using KMP Algorithm")
            keyword = input("Keyword: ")
            results = []
            current = contacts_list.head
            while current:
                if kmp_search(current.data.name, keyword):
                    results.append(current.data)
                current = current.next
                
            if results:
                print("Contacts found:")
                for c in results:
                    print(f"{c.name} - {c.phone_number}")
            else:   
                print("No contacts found.")

            break
        
        elif option == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
# Lancer le programme
menu()
