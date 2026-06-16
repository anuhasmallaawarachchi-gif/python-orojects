tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
      task = input("Enter a new task: ") 
      tasks.append(tasks)
      print("task added succesfully")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove")

        else: 
            for i, task in enumerate(tasks, start =1):
                print(f"{i}.{task}")

        task_num = int(input("Enter task number to remove :"))
        if 1<= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"'{removed}' removed succesfully!")
        else:
            print("Invalid task number.") 

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again")
        
            
