import csv

def add_task(task):
    with open('todo.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task])
    print("\nTask successfully added.")

def view_tasks():
    with open('todo.csv', 'r') as file:
        reader = csv.reader(file)
        tasks = list(reader); print()
        if tasks:
            for i, task in enumerate(tasks):
                print(f'{i+1}. {task[0]}')
        else:
            print("\nNo tasks found.")

def delete_task(task):
    with open('todo.csv', 'r') as file:
        reader = csv.reader(file)
        tasks = list(reader)
    
    with open('todo.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        deleted = False
        for i in range(len(tasks)):
            if tasks[i][0] != tasks[task-1][0]:
                writer.writerow(tasks[i])
            else:
                deleted = True
        
        if deleted:
            print(f"\nTask '{task}' deleted.")
        else:
            print(f"\nTask '{task}' not found.")

def main():
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit\n")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("\nEnter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            while True:
                task = input("\nEnter task to delete: ")
                try:
                    task = int(task); break
                except:
                    print("\nInvalid task number. Please try again."); continue
            delete_task(task)
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == '__main__':
    main()