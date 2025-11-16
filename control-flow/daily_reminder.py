# Get user to input task, task priority 
task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ").lower()
time_bound  = input("Is it time-bound? (yes/no): ").lower()

# Use match case to Process the Task Based on Priority and Time Sensitivity
match task_priority:
    case "high":
        if time_bound == "yes" or  "y":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no" or "n":
            print(f"Reminder: '{task}' is a high priority task!")
        else:
            print("Time bound is either 'yes' or 'no'")
    case "medium":
        if time_bound == "yes" or "y":
            print(f"Note: '{task}' is a medium priority task that requires attention!")
        elif time_bound == "no" or "n":
            print(f"Note: '{task}' is a medium priority task.")
        else:
            print("Time bound is either 'yes' or 'no'")
    case "low":
        if time_bound == "yes" or "y":
            print(f"Note: '{task}' is a low priority task that requires attention!")
        elif time_bound == "no" or "n":
            print(f"Note '{task}' ia a low priority task. Consider completing it when you have a free time.")
        else:
            print("Time bound is either 'yes' or 'no'")