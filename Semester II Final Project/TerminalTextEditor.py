# Importing the required dependencies
import os           # OS module for running terminal commands
import subprocess   # Subprocess module for running terminal commands

# FileDoesNotExistsError Exception is raised when a file does not exist
class FileDoesNotExistsError(Exception):
    pass


# TerminalTextEditor Class with the following methods
# 1. __init__(self, filename: str, fileType: str) -> None: Initialize the object with filename and filetype
# 2. get_extension(self) -> str: returns the extension of the file depending on the file type
# 3. CreateFile(self) -> None: Creates a new file depending on the file type. Also Adds a comment to the file
# 4. EditFile(self, editor: str) -> None: Editing the file through the terminal based on the editor of user's choice
# 5. DeleteFile(self) -> None: Deletes the file or raise an exception if the file does not exist

class TerminalTextEditor:
    # Initializing a TerminalTextEditor Object with filename and fileType as string attributes
    def __init__(self, filename: str, fileType: str) -> None:
        self.filename = filename                    # filename input from the user
        self.fileType = fileType                    # file type input from the user
        self.extension = self.get_extension()       # get_extension method used to get the extension based on the file type
    
    # method used to get the extension based on fileType of the Object
    def get_extension(self) -> str:
        if self.fileType == 'textfile': return '.txt'
        elif self.fileType == 'python programming': return '.py'
        elif self.fileType == 'C programming': return '.c'
        else: return '.txt'                         # Returns .txt extension by default if fileType not specified
        
    # Method to create a new file with filename and extension
    def CreateFile(self) -> None:
        try:
            # Creating new file with 'Write' mode and writing a first line comment
            with open(self.filename, 'w') as file:
                if self.extension == '.txt':
                    file.write("Write something here...")
                elif self.extension == '.py':
                    file.write("# Write your code here...")
                elif self.extension == '.c':
                    file.write("// Write your code here...")
            # Success Message
            print(f"File '{self.filename}' Successfully created..! ✅")
            # Changing the extension of the file as per filetype
            file_path = os.getcwd() + '/' + self.filename                   # Getting yhe path of the file
            os.rename(file_path, file_path + self.extension)                # Extension changed
        except IOError as error:
            print(f"Error creating file '{self.filename} ❌ : {error}")     # Exception handled
        
    # Method to edit an existing file with text editor of choice
    def EditFile(self, editor: str) -> None:
        try:
            # runs terminal command to open a text editor of choice and edit the file
            os.system(f"{editor} {self.filename}{self.extension}")
        except Exception as error:        # Exception raised if file does not exist
            raise FileDoesNotExistsError(f"Error finding file '{self.filename}{self.extension}' ❌ : {error}")

    # Method to delete a file
    def DeleteFile(self) -> None:
        try:
            # Deletes the file if exists
            os.remove(self.filename + self.extension)
            print(f"File '{self.filename}' Successfully deleted..! ✅")
        except OSError as error:    # Exception raised if the file does not exist
            raise FileDoesNotExistsError(f"Error deleting file '{self.filename}{self.extension}' ❌ : {error}")


# TerminalPythonEditor class implementation, a child class of the TerminalTextEditor class
# Concept of inheritance used by TerminalPythonEditor  
# TerminalPythonEditor class with the following methods:  
# 1. __init__(self, filename: str, fileType: str) -> None: Initialize the object with filename and filetype
# 2. RunPythonFile(self) -> None: Runs the python file in the terminal

class TerminalPythonEditor(TerminalTextEditor):
    # Initialize the object with filename and filetype
    def __init__(self, filename: str, fileType: str) -> None:
        super().__init__(filename, fileType)

    # Method to run the python file in the terminal
    def RunPythonFile(self) -> None:
        subprocess.call(['python3', f'{self.filename}.py'])     # Subprocess call to run python3 filename.py


# TerminalCProgramEditor class implementation, a child class of the TerminalTextEditor class
# Concept of inheritance is used by the TerminalCProgramEditor
# Concept of Method Overriding is used to override the DeleteFile method
# TerminalCProgramEditor class with the following methods:
# 1. __init__(self, filename: str, fileType: str) -> None: Initialize the object with filename and filetype
# 2. RunCProgramFile(self) -> None: Runs the C program in the terminal
# 3. DeleteFile(self) -> None: Deletes the C file and the Output file if exists (Method Overriding)

class TerminalCProgramEditor(TerminalTextEditor):
    # Initialize the object with filename and filetype
    def __init__(self, filename: str, fileType: str) -> None:
        super().__init__(filename, fileType)

    # Method to run the C program in the terminal
    def RunCProgramFile(self) -> None:
        subprocess.call(['gcc', f'{self.filename}.c'])      # Subprocess to compile the C program using gcc
        os.system('./a.out')                                # executes the a.out file from os.system

    # Method to delete the C program file
    def DeleteFile(self) -> None:
        try:
            os.remove(self.filename + self.extension)                       # Deletes the C program file
            if os.path.exists('a.out'): os.remove('a.out')                  # Deletes the output file if exists
            print(f"File '{self.filename}' Successfully deleted..! ✅")     # Success message
        except OSError as error:
            # Raise exception if file does not exist
            raise FileDoesNotExistsError(f"Error deleting file '{self.filename}{self.extension}' ❌ : {error}")

    

if __name__ == '__main__':
    filename = "testingText"

    fileObject = TerminalPythonEditor(filename, fileType='python programming')
    # fileObject.CreateFile()
    # fileObject.EditFile('nano')
    # fileObject.RunPythonFile()
    # fileObject.DeleteFile()


