import sys

# Prompt for a single task (non-empty)
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a task.")

# Prompt for priority with validation loop
while True:
    task_priority = input("Priority (high/medium/low): ").strip().lower()
    if task_priority in ("high", "medium", "low"):
        break
    print("Task priority should be either 'high', 'medium' or 'low'!")

# Prompt for time-bound with validation loop and normalize yes/y -> yes, no/n -> no
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "y"):
        time_bound = "yes"
        break
    if time_bound in ("no", "n"):
        time_bound = "no"
        break
    print("Time-bound should be either 'yes' or 'no'!")

# Use match/case to build base message based on priority
match task_priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        # Defensive fallback (shouldn't occur due to validation)
        print("Unexpected task priority.")
        sys.exit(1)

# Modify message if time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

print(message)