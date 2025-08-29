#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import os


# In[2]:


def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def user_file(username):
    """Return filename for storing user's tasks"""
    return f"tasks_{username}.txt"


# In[10]:


def register():
   username = input("Enter a new username: ")
   password = input("Enter a new password: ")

   # check if username already exists
   with open("users.txt", "a+") as f:
       f.seek(0)
       for line in f:
           stored_user, _ = line.strip().split("|")
           if stored_user == username:
               print("[error] Username already exists. Try another.")
               return None

   # store new user with hashed password
   with open("users.txt", "a") as f:
       f.write(f"{username}|{hash_password(password)}\n")

   print("[success] Registration successful! Please login.")
   return username


def login():
   username = input("Enter username: ")
   password = input("Enter password: ")

   with open("users.txt", "r") as f:
       for line in f:
           stored_user, stored_pass = line.strip().split("|")
           if stored_user == username and stored_pass == hash_password(password):
               print(f"[success] Welcome, {username}!")
               return username

   print("[error] Invalid username or password.")
   return None


# In[11]:


def add_task(username):
    task_desc = input("Enter task description: ")
    filename = user_file(username)

    # get next task id
    task_id = 1
    if os.path.exists(filename):
        with open(filename, "r") as f:
            lines = f.readlines()
            if lines:
                last_id = int(lines[-1].split("|")[0])
                task_id = last_id + 1

    with open(filename, "a") as f:
        f.write(f"{task_id}|{task_desc}|Pending\n")

    print("[success] Task added successfully!")


def view_tasks(username):
    filename = user_file(username)
    if not os.path.exists(filename):
        print(" No tasks found.")
        return

    with open(filename, "r") as f:
        tasks = f.readlines()

    if not tasks:
        print(" No tasks available.")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        task_id, desc, status = task.strip().split("|")
        print(f"[{task_id}] {desc} - {status}")
    print("------------------")


def mark_completed(username):
    view_tasks(username)
    task_id = input("Enter Task ID to mark as completed: ")

    filename = user_file(username)
    if not os.path.exists(filename):
        print(" No tasks found.")
        return

    tasks = []
    updated = False
    with open(filename, "r") as f:
        for line in f:
            tid, desc, status = line.strip().split("|")
            if tid == task_id:
                tasks.append(f"{tid}|{desc}|Completed\n")
                updated = True
            else:
                tasks.append(line)

    with open(filename, "w") as f:
        f.writelines(tasks)

    if updated:
        print("[success] Task marked as completed!")
    else:
        print("[error] Task ID not found.")


def delete_task(username):
    view_tasks(username)
    task_id = input("Enter Task ID to delete: ")

    filename = user_file(username)
    if not os.path.exists(filename):
        print(" No tasks found.")
        return

    tasks = []
    deleted = False
    with open(filename, "r") as f:
        for line in f:
            tid, desc, status = line.strip().split("|")
            if tid != task_id:
                tasks.append(line)
            else:
                deleted = True

    with open(filename, "w") as f:
        f.writelines(tasks)

    if deleted:
        print("[success] Task deleted successfully!")
    else:
        print("[error] Task ID not found.")


# In[12]:


# ---------- Main Menu ----------
def task_manager(username):
    while True:
        print("\n===== Task Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            mark_completed(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            print("👋 Logged out.")
            break
        else:
            print("[error] Invalid choice. Try again.")


# In[ ]:


# ---------- Main Program ----------
def main():
    if not os.path.exists("users.txt"):
        open("users.txt", "w").close()

    while True:
        print("\n===== Welcome to Task Manager =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                task_manager(user)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




