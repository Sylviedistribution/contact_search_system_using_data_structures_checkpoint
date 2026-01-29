class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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

# Recherche par sous-chaîne
def search_by_keyword(keyword):
    results = []
    current = contacts_list.head
    while current:
        if keyword.lower() in current.data.name.lower():
            results.append(current.data)
        current = current.next
    return results

# Menu principal
def menu():
    while True:
        print("\n--- Gestion des Contacts ---")
        print("1. Ajouter un contact")
        print("2. Rechercher par mot-clé")
        print("3. Rechercher par nom exact")
        print("4. Afficher tous les contacts (avant)")
        print("5. Afficher tous les contacts (arrière)")
        print("6. Supprimer un contact")
        print("7. Quitter")
        
        option = input("Entrez votre choix: ")

        if option == "1":
            name = input("Nom: ")
            phone = input("Téléphone: ")
            contact = Contact(name, phone)
            contacts_list.append(contact)
            contacts_hash[name] = contact
            print("Contact ajouté.")

        elif option == "2":
            keyword = input("Mot-clé: ")
            results = search_by_keyword(keyword)
            if results:
                print("Contacts trouvés:")
                for c in results:
                    print(f"{c.name} - {c.phone_number}")
            else:
                print("Aucun contact trouvé.")

        elif option == "3":
            name = input("Nom exact: ")
            contact = contacts_hash.get(name)
            if contact:
                print(f"Contact trouvé: {contact.name} - {contact.phone_number}")
            else:
                print("Aucun contact trouvé.")

        elif option == "4":
            print("Contacts (avant):")
            contacts_list.display_forward()

        elif option == "5":
            print("Contacts (arrière):")
            contacts_list.display_backward()

        elif option == "6":
            name = input("Nom du contact à supprimer: ")
            deleted = contacts_list.delete(name)
            if deleted:
                contacts_hash.pop(name, None)
                print("Contact supprimé.")
            else:
                print("Contact non trouvé.")

        elif option == "7":
            print("Au revoir!")
            break

        else:
            print("Option invalide.")

# Lancer le programme
menu()
