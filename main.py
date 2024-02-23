import os
import subprocess

def create_file(file_name):
    with open(file_name, 'w') as file:
        file.write("# Enter your Python code here")
    file_path = os.getcwd() + '/' + file_name
    os.rename(file_path, file_path + '.py')


def edit_file(file_name):
    while True:
        print("\nChoose your editor: \n1. Nano\n2. Vim\n3. Code\n")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                editor = 'nano'
                break
            elif choice == 2:
                editor = 'vi'
                break
            elif choice == 3:
                editor = 'code'
                break
            else:
                print("\nInvalid choice. Please try again.")
        except: print("\nInvalid choice. Please try again.")
    os.system(f"{editor} {file_name}.py")

def run_file(file_name):
    subprocess.call(['python3', f'{file_name}.py'])

def main():
    while True:
        print("\n1. Create a new Python file")
        print("2. Edit an existing Python file")
        print("3. Run a Python file")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            file_name = input("\nEnter the file name: ")
            create_file(file_name)
        elif choice == '2':
            file_name = input("\nEnter the file name: ")
            edit_file(file_name)
        elif choice == '3':
            file_name = input("\nEnter the file name: "); print()
            run_file(file_name)
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()