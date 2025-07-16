task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input(" Priority (high, medium, low): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(task + " is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(task + " is a low priority task. Consider completing it when you have free time.") 
    case "medium":
            print(task + " is a medium priority task that requires immediate attention today!")
    case "low":
        if time_bound == "yes":
            print(task + " is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(task + " is a high priority task. Consider completing it when you have free time.") 
    case _:
        print("Invalid priority level entered. Please enter 'high', 'medium', or 'low'.") 