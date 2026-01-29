# 📇 Contact Management System (Python)

A simple yet efficient **contact management system** built in Python, combining **data structures and algorithms** in a practical way.  
This project demonstrates the usage of **doubly linked lists**, **hash tables (dictionaries)**, and **substring search algorithms** to build a real-world application.

---

## 🚀 Features

- Add contacts (name + phone number)
- Fast lookup by **exact name** using a hash table → **O(1)**
- Search contacts by **keyword (substring matching)**
- Display contacts:
  - Forward order
  - Backward order
- Delete contacts
- Interactive **text-based menu interface**

---

## 🧠 Technical Concepts Used

This project is designed to practice and demonstrate the following concepts:

### 1. Doubly Linked List
Used to store all contacts and allow:

- Forward traversal
- Backward traversal
- Efficient deletion

Each node contains:
- `data` → Contact object
- `next` → reference to next node
- `prev` → reference to previous node

---

### 2. Hash Table (Python Dictionary)
Used for **instant lookup by exact name**.

```python
contacts_hash = {}
This provides:
```

O(1) average time complexity for:

-Search
-Insert
-Delete

3. Substring Search (Naive String Matching)
To find contacts using a keyword, a simple substring search is implemented:

if keyword.lower() in current.data.name.lower():

This allows:

-Partial name matching
-Case-insensitive search

Example:

Keyword: Al
Matches: Alice, Alex, Alfred

🏗️ Project Architecture
```js
contact-management-system/
│
├── main.py
└── README.md
```
Main Components:
-Contact → Data model

-Node → Doubly linked list node

-DoubleLinkedList → Data structure implementation

-contacts_hash → Dictionary for fast access

-menu() → User interaction logic

⚙️ How It Works
Each contact is stored simultaneously in:

A doubly linked list → for ordered display

A hash table (dict) → for fast exact lookup

Both structures reference the same Contact object, ensuring data consistency.

📋 Menu Options

1. Add Contact
2. Search by Keyword
3. Search by Exact Name
4. View All (Forward)
5. View All (Backward)
6. Delete Contact
7. Exit

🖥️ Sample Execution
--- Contact Management System ---
1. Add Contact
2. Search by Keyword
3. Search by Exact Name
4. View All (Forward)
5. View All (Backward)
6. Delete Contact
7. Exit

Enter option: 1
Name: Alice
Phone: 1234567890
Contact added.

Enter option: 2
Search keyword: Al
Match found: Alice - 1234567890
📈 Time Complexity
Operation	Complexity
Add Contact	O(1)
Search by Exact Name	O(1)
Search by Keyword	O(n)
Display (Forward/Backward)	O(n)
Delete Contact	O(n)

🎯 Learning Objectives
This project helps to understand:

Linked list traversal

Bidirectional data navigation

Hash-based fast lookups

Real-world application of string matching

Structuring code using clean architecture

🛠️ Possible Improvements
Implement Trie for ultra-fast prefix search

Implement KMP algorithm for advanced pattern matching

Add file persistence (save/load contacts)

Build a GUI or Web interface

Add autocomplete suggestions

📜 License
This project is open-source and free to use for educational purposes.

👨‍💻 Author
Sylvestre Ibombo Gakosso