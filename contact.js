const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function prompt(question) {
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      resolve(answer);
    });
  });
}

class Contact {
  constructor(name, number) {
    this.name = name;
    this.number = number;
  }
}

class Node {
  constructor(contact) {
    this.data = contact;
    this.prev = null;
    this.next = null;
  }
}

class DoubleLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  append(data) {
    const newNode = new Node(data);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
    return true;
  }
  displayForward() {
    let current = this.head;

    while (current) {
      console.log(
        "Name: " + current.data.name + ", Number: " + current.data.number,
      );
      current = current.next;
    }
  }
  displayBackward() {
    let current = this.tail;

    while (current) {
      console.log(
        "Name: " + current.data.name + ", Number: " + current.data.number,
      );
      current = current.prev;
    }
  }

  searchByKeyword(substring) {
    let current = this.head;
    const results = [];
    while (current) {
      if (current.data.name.toLowerCase().includes(substring.toLowerCase())) {
        results.push(current.data);
      }
              current = current.next;

    }
    return results;
  }

  deleteContact(name) {
    let current = this.head;
    while (current) {
      if (current.data.name.toLowerCase() === name.toLowerCase()) {
        if (current.prev) {
          current.prev.next = current.next;
        } else {
          this.head = current.next;
        }
        if (current.next) {
          current.next.prev = current.prev;
        } else {
          this.tail = current.prev;
        }
        return true;
      }
      current = current.next;
    }
    return false;
  }
}

var contacts_hash = new Map();
var contacts_list = new DoubleLinkedList();

displayMenu = function () {
  console.log(`Contact Management System: \n
        1. Add Contact\n
        2. Search by Exact Name\n
        3. Search by Keyword\n
        4. Display Contacts Forward\n
        5. Display Contacts Backward\n
        6. Delete Contact\n
        7. Exit`);
};

async function runProgram() {
  while (true) {
    displayMenu();
    const choice = await prompt("Enter your choice: ");

    switch (choice) {
      case "1":
        const name = await prompt("Enter contact name: ");
        const number = await prompt("Enter contact number: ");
        const newContact = new Contact(name, number);
        contacts_hash.set(name.toLowerCase(), newContact);
        contacts_list.append(newContact);
        console.log("Contact added successfully.");
        break;
      case "2":
        const searchName = (await prompt("Enter name to search: ")).toLowerCase();
        if (contacts_hash.has(searchName)) {
          const contact = contacts_hash.get(searchName);
          console.log("Name: " + contact.name + ", Number: " + contact.number);
        } else {
          console.log("Contact not found.");
        }
        break;
      case "3":
        const substring = await prompt("Enter substring to search: ");
        const results = contacts_list.searchByKeyword(substring);
        if (results.length > 0) {
          results.forEach((contact) => {
            console.log(
              "Name: " + contact.name + ", Number: " + contact.number,
            );
          });
        } else {
          console.log("No contacts found with the given substring.");
        }
        break;
      case "4":
        contacts_list.displayForward();
        break;
      case "5":
        contacts_list.displayBackward();
        break;
      case "6":
        const delName = await prompt("Enter name to delete: ");
        contacts_list.deleteContact(delName);
        contacts_hash.delete(delName.toLowerCase());
        console.log("Contact deleted successfully.");
        break;
      case "7":
        console.log("Exiting program.");
        return;
    }
  }
}

runProgram();
