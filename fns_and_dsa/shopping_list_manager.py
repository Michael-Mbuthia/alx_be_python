shopping_list = []

# Function to add task"
def add_task():
    task = input("Enter a new task: ")
    shopping_list.append(task)
    print("Task added successfully.")
    
# Function to view tasks"
def view_tasks():
    if len(shopping_list) == 0:
        print("no tasks")
    else: 
        print("List of tasks: ")
        for i, task in enumerate(shopping_list):
            print(f"{i+1}. {task}")
            
# Function to delete task"
def delete_task():
    if len(shopping_list) == 0:
        print("no tasks to delete.")
    else:
        # Displays all tasks
        print("Tasks: ")
        for i, task in enumerate(shopping_list):
            print(f"{i+1}. {task}")
        choice = int(input("Enter the task number to be delete: "))
        
        if 0 < choice <= len(shopping_list):
            del shopping_list[choice-1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
            

def main():

    while True:
        print("====== Task Tracker Application =====")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Quit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thank you for using the Task Tracker Application")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    main()
        
        
            
            


    