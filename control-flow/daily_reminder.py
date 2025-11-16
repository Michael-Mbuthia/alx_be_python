# Get user to input task, task priority 
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate priority
if priority not in ["high", "medium", "low"]:
    print("Task priority should be either 'high', 'medium' or 'low'!")
    exit()
        
# Validate time-bound
if time_bound not in ["yes", "y", "no", "n"]:
    print("Time-bound should be either 'yes' or 'no'!")
    exit()

# Normalize time_bound to 'yes' or 'no'
if time_bound in ["y"]:
    time_bound = "yes"
elif time_bound in ["n"]:
    time_bound = "no"

# Use match case to Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
            
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
            
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            
    case _:
        print("Task priority should be either 'high', 'medium' or 'low'!")
        exit()