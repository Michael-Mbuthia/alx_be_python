# Get user to input task, task priority 
task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ").lower()
time_bound  = input("Is it time-bound? (yes/no): ").lower()

# Initialize task reminder
message = ""

# Use match case to Process the Task Based on Priority and Time Sensitivity
match task_priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        print("Task priority should be either 'high', 'medium' or 'low'!")
        exit()
         
# use if statement tomodifynthetask if time is bound
if time_bound == "yes" or time_bound == "y":
    message += "that requires immediate attention today!"
elif time_bound == "no" or time_bound == "n":
    message += ". Consider completing it when you have free time"
else:
    print("Time-bound should be either 'yes' or  'no'!")
    exit()
        
print(f"{message}")   