from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress


def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                add_task(title, description, due_date)
            except Exception as error:
                print(f"Error: {error}")
        elif choice == "2":
            task_index = input("Enter the index of the task to complete: ")
            try:
                index = int(task_index) - 1
                mark_task_as_complete(index)
            except ValueError:
                print("Error: Please enter a valid integer index.")
            except Exception as error:
                print(f"Error: {error}")
        elif choice == "3":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks.")
            else:
                print("Pending Tasks:")
                for idx, task in enumerate(pending, start=1):
                    print(f"{idx}. {task['title']} - Due {task['due_date']}")
        elif choice == "4":
            progress = calculate_progress()
            if progress == 0:
                print("No working currently")
            else:
                print(f"Progress: {progress}% complete")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
