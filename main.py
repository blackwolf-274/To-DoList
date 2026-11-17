"""Simple command-line to-do list application.

This script manages user accounts and task records by storing data in JSON files.
Each function handles one part of the program flow, making the app easier to read,
maintain, and extend over time.
"""

import json

# Create a new user account by saving username and password data to users.json.
def create_user(username, password):
    user_data = {
        'username': username,
        'password': password
    }
    with open('users.json', 'w') as file:
        json.dump(user_data, file)

# Check whether the provided username and password match the saved account data.
def login(username, password):
    try:
        with open('users.json', 'r') as file:
            user_data = json.load(file)
            if user_data['username'] == username and user_data['password'] == password:
                print("Login successful!")
                return True
            else:
                print("Invalid username or password.")
                return False
    except FileNotFoundError:
        print("No user found. Please create an account first.\n")

# Display the main dashboard menu and manage the user's task actions.
def dashboard():
    while True:
        print("\nWelcome to your To-Do List Dashboard!")
        print("1. Add tasks")
        print("2. View task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Logout")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Add a single task by appending it to the task list file.
def add_task():
    task = input("Enter the task you want to add: ")
    with open('tasks.json', 'a') as file:
        file.write(task + '\n')
    print("Task added successfully!")

# Read and display all saved tasks from the tasks.json file.
def view_task():
    try:
        with open('tasks.json', 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("No tasks found.")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")

# Replace one existing task using the selected task number.
def update_task():
    view_task()
    try:
        task_number = int(input("Enter the task number you want to update: "))
        with open('tasks.json', 'r') as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_number - 1] = new_task + '\n'
            with open('tasks.json', 'w') as file:
                file.writelines(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")

# Remove a task by its number from the tasks list and rewrite the file.
def delete_task():
    view_task()
    try:
        task_number = int(input("Enter the task number you want to delete: "))
        with open('tasks.json', 'r') as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            with open('tasks.json', 'w') as file:
                file.writelines(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")

# Entry point for the application: show the start menu and route to login or account creation.
def main():
    while True:
        print("Welcome to the To-Do List Application!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            create_user(username, password)
            print("Account created successfully!\n")
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login(username, password):
                print("You can now access your to-do list.\n")
                return dashboard()
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()