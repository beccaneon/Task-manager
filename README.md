# Task-manager
A Python-based Task Manager with user authentication using file handling. Allows users to register, login, and manage their personal tasks (add, view, complete, delete).
# Task Manager with User Authentication

## 📌 Project Overview
This project is a simple **Task Manager** built in Python.  
It includes **user authentication** (registration & login) and allows each user to manage their own tasks.  
Data is stored persistently using **file handling**.

## 🎯 Features
- 🔐 **User Authentication**  
  - Registration with unique usernames  
  - Passwords stored as SHA256 hashes  
  - Secure login system  

- 📝 **Task Management**  
  - Add new tasks  
  - View all tasks (with ID, description, status)  
  - Mark tasks as Completed  
  - Delete tasks  

- 💾 **File Handling**  
  - `users.txt` stores usernames & hashed passwords  
  - `tasks_<username>.txt` stores each user’s tasks separately  

## 🛠️ Technologies Used
- Python 3
- `hashlib` (for password hashing)
- `os` (for file handling checks)

## 🚀 How to Run
1. Clone this repository or download the files.
2. Run the program:
   ```bash
   python task_manager.py
