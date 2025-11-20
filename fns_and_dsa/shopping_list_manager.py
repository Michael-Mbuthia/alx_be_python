shopping_list = []

# Function to add task"
def add_item():
    task = input("Enter a new task: ")
    shopping_list.append(task)
    print("Task added successfully.")
    
# Function to view tasks"
def view_list():
    if len(shopping_list) == 0:
        print("no tasks")
    else: 
        print("List of tasks: ")
        for i, task in enumerate(shopping_list):
            print(f"{i+1}. {task}")
            
# Function to delete task"
def remove_item():
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
            

def display_menu():
        print("====== Shopping List =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View list")
        print("4. Exit")
def main():
    shopping_list = [] 
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            view_list()
        elif choice == 4:
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    main()
        
        
            
            


    