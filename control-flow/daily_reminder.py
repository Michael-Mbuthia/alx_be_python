import sys

# Get user to input task, task priority 
task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate task priority
if task_priority not in ["high", "medium", "low"]:
    print("Task priority should be either 'high', 'medium' or 'low'!")
    sys.exit()
        
# Validate time-bound
if time_bound not in ["yes", "y", "no", "n"]:
    print("Time-bound should be either 'yes' or 'no'!")
    sys.exit()

# Normalize yes/y → yes
if time_bound in ["yes", "y"]:
    time_bound = "yes"

message = ""

# Use match case to Process the Task Based on Priority and Time Sensitivity
match task_priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            message += " that requires immediate attention today!"
        else:
            message += ". Consider completing it when you have free time."

    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
        if time_bound == "yes":
            message += " that requires immediate attention today!"
        else:
            message += ". Consider completing it when you have free time."

    case "low":
        message = f"Note: '{task}' is a low priority task"
        if time_bound == "yes":
            message += " that requires immediate attention today!"
        else:
            message += ". Consider completing it when you have free time."

print(message)