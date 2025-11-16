# Get user to input task, task priority 
task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate task priority
if task_priority not in ["high", "medium", "low"]:
    print("Task priority should be either 'high', 'medium' or 'low'!")
    exit()
        
# Validate time-bound
if time_bound not in ["yes", "y", "no", "n"]:
    print("Time-bound should be either 'yes' or 'no'!")
    exit()

# Initialize task reminder
message = ""

# Use match case to Process the Task Based on Priority and Time Sensitivity
match task_priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
        # Check time sensitivity within match case
        if time_bound == "yes" or time_bound == "y":
            message += " that requires immediate attention today!"
        else:
            message += ". Consider completing it when you have free time."
            
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
        # Check time sensitivity within match case
        if time_bound == "yes":
            message += " that requires immediate attention today!"
        else:
            message += ". Consider completing it when you have free time."
            
    case "low":
        message = f"Note: '{task}' is a low priority task"
        # Check time sensitivity within match case
        if time_bound == "yes":
            message += " that requires immediate attention today!"
        else:
            message += ". Consider completing it when you have free time."
            
    case _:
        print("Task priority should be either 'high', 'medium' or 'low'!")
        exit()
        
print(f"{message}")