import csv
import os
import csv
import datetime

# An Exception class for AgeNotValidError: Age should be greater than or equal to 18.
class AgeNotValidError(Exception):
    pass

# An Exception class for InsufficientBalanceError: If the balance is less than the amount to be withdrawn or transferred InsufficientBalanceError is raised.
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    # BankAccount class with the following methods:
    # 1. __init__(self, AccNo: str, InitialAmount: float, OwnerDetails: dict) -> None: Constructor to initialize the account details.
    # 2. CreateBankStatements(self) -> None: Method to create the bank statements.
    # 3. StoreOwnerDetails(self, filename: str) -> None: Method to store the owner details in a CSV file. 
    # 4. AccountDetails(self) -> None: Method to display the account details.
    # 5. GetBalance(self) -> None: Method to display the account balance.
    # 6. Deposit(self, Amount: float) -> None: Method to deposit the amount.
    # 7. ViableTransaction(self, Amount: float) -> None: Method to check if the transaction is viable.
    # 8. Withdraw(self, Amount: float) -> None: Method to withdraw the amount.
    # 9. Transfer(self, Amount: float, Account: 'BankAccount') -> None: Method to transfer the amount to another account.

    def __init__(self, AccNo: str, InitialAmount: float, OwnerDetails: dict) -> None:
        self.AccNo = AccNo                  # Account Number of the account. str type.
        self.Balance = InitialAmount        # Initial Amount of the account. float type.
        self.OwnerDetails = OwnerDetails    # Owner Details of the account. dict type.
        self.AccType = "Regular"            # Account Type of the account.

        # Check whether the age is greater than or equal to 18.
        if self.OwnerDetails["Age"] < 18:
            raise AgeNotValidError("Age should be greater than or equal to 18.")
        
        # If the age is greater than or equal to 18, then the account is created successfully.
        print("\nCongratulations! Your account has been created successfully! 🥳🥳🥳 🤑🤑🤑")

    def CreateBankStatements(self) -> None:
        try:
            directory = os.path.dirname(os.path.abspath(__file__))                         # Get the directory path of the current file.
            filename = f"{self.AccNo}.csv"                                                 # Create the filename using the account number.
            # Create the full file path by joining the directory path and the filename.
            filepath = os.path.join(directory + '/Account_Statements', filename)
            
            with open(filepath, 'w', newline='') as file:                                  # Open the CSV file in write mode.
                writer = csv.writer(file)                                                  # Create a CSV writer object.
                writer.writerow(['Date-Time', 'Operation', 'To', 'Amount', 'Balance'])     # Write the header row.
               
            print(f"\nBank statements have been created successfully! ✅")
        except Exception as error:
            print(f"\nError occurred while creating the bank statements: {error} ❌")
    
    # Method to store the owner details in a CSV file.
    def StoreOwnerDetails(self, filename: str) -> None:
        try:
            directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory path of the current file.
            # Create the full file path by joining the directory path and the filename.
            filepath = os.path.join(directory, filename)
            with open(filepath, 'w', newline='') as file:           # Open the CSV file in write mode.
                writer = csv.writer(file)                           # Create a CSV writer object.        
                writer.writerow(['Name', 'Age', 'Phone'])           # Write the header row.
                # Write the owner details row.
                writer.writerow([self.OwnerDetails['Name'], self.OwnerDetails['Age'], self.OwnerDetails['Phone']])
            
            print(f"\n{self.OwnerDetails['Name']} details have been stored in the file: {filename} Successfully! ✅")
        except Exception as error:
            print(f"\nError occurred while storing the owner details: {error} ❌")
    

    # Method to display the account details.
    def AccountDetails(self) -> None:
        print("\nAccount Details:")
        print(f"Account No: {self.AccNo}")
        print(f"Account Balance: $ {self.Balance:.2f}")
        print(f"Account Owner Details:")
        print(f"Name: {self.OwnerDetails['Name']}")
        print(f"Age: {self.OwnerDetails['Age']}")
        print(f"Phone: {self.OwnerDetails['Phone']}")
        print(f"Account Type: {self.AccType}")

    # Method to display the account balance.
    def GetBalance(self) -> None:
        print(f"\nAccount No: {self.AccNo}")
        print(f"Account Name: {self.OwnerDetails['Name']}")
        print(f"Account Balance: $ {self.Balance:.2f}")
    
    # Method to deposit the amount.
    def Deposit(self, Amount: float) -> None:
        self.Balance += Amount                                                  # Add the amount to the balance.
        try:
            directory = os.path.dirname(os.path.abspath(__file__))              # Get the directory path of the current file.
            filename = f"{self.AccNo}.csv"                                      # Create the filename using the account number.
            # Create the full file path by joining the directory path and the filename.
            filepath = os.path.join(directory + '/Account_Statements', filename)
            
            with open(filepath, 'a', newline='') as file:                       # Open the CSV file in append mode.
                writer = csv.writer(file)                                       # Create a CSV writer object.
                # Write the deposit operation.
                writer.writerow([datetime.datetime.now(), 'Deposit', 'N/A', f"${Amount:.2f}", f"${self.Balance:.2f}"])
            
            print(f"\n$ {Amount:.2f} has been deposited successfully. ✅")
            self.GetBalance()                                                   # Display the account balance.
        except Exception as error:
            print(f"\nError occurred while depositing the amount: {error} ❌")

    # Method to check if the transaction is viable.
    def ViableTransaction(self, Amount: float) -> None:
        # If the balance is less than the amount to be withdrawn or transferred, then InsufficientBalanceError is raised.
        if self.Balance < Amount:
            raise InsufficientBalanceError("Insufficient Balance.")
        return
    
    # Method to withdraw the amount.
    def Withdraw(self, Amount: float) -> None:
        # Check if the transaction is viable.
        try:
            self.ViableTransaction(Amount)                                      # Check if the transaction is viable.
            self.Balance -= Amount                                              # Subtract the amount from the balance.
            directory = os.path.dirname(os.path.abspath(__file__))              # Get the directory path of the current file.
            filename = f"{self.AccNo}.csv"                                      # Create the filename using the account number.
            # Create the full file path by joining the directory path and the filename.
            filepath = os.path.join(directory + '/Account_Statements', filename)
            
            with open(filepath, 'a', newline='') as file:                       # Open the CSV file in append mode.
                writer = csv.writer(file)                                       # Create a CSV writer object.
                # Write the deposit operation.
                writer.writerow([datetime.datetime.now(), 'Withdraw', 'N/A', f"${Amount:.2f}", f"${self.Balance}"])
            print(f"\n$ {Amount:.2f} has been withdrawn successfully. ✅")
            self.GetBalance()                                                   # Display the account balance.
        # If the transaction is not viable, then InsufficientBalanceError is raised.
        except InsufficientBalanceError as error:
            print(f"\nWithdraw interrupted: {error} ❌")
    
    # Method to transfer the amount to another account.
    def Transfer(self, Amount: float, Account: 'BankAccount') -> None:
        # Check if the transaction is viable.
        try:
            self.ViableTransaction(Amount)                                      # Check if the transaction is viable.
            self.Balance -= Amount                                              # Subtract the amount from the balance.
            Account.Balance += Amount                                           # Add the amount to the balance of the account to which the amount is transferred.
            directory = os.path.dirname(os.path.abspath(__file__))              # Get the directory path of the current file.
            filename = f"{self.AccNo}.csv"                                      # Create the filename using the account number.
            # Create the full file path by joining the directory path and the filename.
            filepath = os.path.join(directory + '/Account_Statements', filename)
            
            with open(filepath, 'a', newline='') as file:                       # Open the CSV file in append mode.
                writer = csv.writer(file)                                       # Create a CSV writer object.
                # Write the deposit operation.
                writer.writerow([datetime.datetime.now(), 'Transfer', f"{Account.AccNo}", f"${Amount:.2f}", f"{self.Balance}"])
            print(f"\n$ {Amount:.2f} has been transferred successfully. ✅")
            self.GetBalance()                                                   # Display the account balance.
        # If the transaction is not viable, then InsufficientBalanceError is raised.
        except InsufficientBalanceError as error:
            print(f"\nTransfer interrupted: {error} ❌")



# A subclass RewardsAccount of the BankAccount class.
# RewardsAccount class with the following methods:
# 1. Deposit(self, Amount: float) -> None: Method to deposit the amount.

# Method Overriding: If the amount deposited is greater than or equal to 1000, then 5% of the amount is added to the balance.
class RewardsAccount(BankAccount):
    def __init__(self, AccNo: str, InitialAmount: float, OwnerDetails: dict) -> None:
        super().__init__(AccNo, InitialAmount, OwnerDetails)                    # Call the constructor of the parent class.
        self.AccType = "Rewards"                                                # Account Type of the account.
        self.DepositBenefits = 0.05                                             # Deposit Benefits of the account.


    def Deposit(self, Amount: float) -> None:
        self.Balance += Amount                                                  # Add the amount to the balance.    
        if Amount >= 1000:                                                      # If the amount deposited is greater than or equal to 1000.
            self.Balance += (Amount * self.DepositBenefits)                     # Add 8% of the amount to the balance.
        try:
            directory = os.path.dirname(os.path.abspath(__file__))              # Get the directory path of the current file.
            filename = f"{self.AccNo}.csv"                                      # Create the filename using the account number.
            # Create the full file path by joining the directory path and the filename.
            filepath = os.path.join(directory + '/Account_Statements', filename)
            
            with open(filepath, 'a', newline='') as file:                       # Open the CSV file in append mode.
                writer = csv.writer(file)                                       # Create a CSV writer object.
                # Write the deposit operation.
                writer.writerow([datetime.datetime.now(), 'Deposit', 'N/A', f"${Amount:.2f}", f"${self.Balance:.2f}"])
            
            print(f"\n$ {Amount:.2f} has been deposited successfully. ✅")
            self.GetBalance()               # Display the account balance.
        except Exception as error:
            print(f"\nError occurred while depositing the amount: {error} ❌")  # Display the account balance.

# A subclass SavingsAccount of the RewardsAccount class.
# SavingsAccount class with the following methods:
# 1. Withdraw(self, Amount: float) -> None: Method to withdraw the amount.

# Method Overriding: If the amount is withdrawn, then 2% of the amount is subtracted from the balance as a withdrawal fee.
class SavingsAccount(RewardsAccount):
    def __init__(self, AccNo: str, InitialAmount: float, OwnerDetails: dict) -> None:
        super().__init__(AccNo, InitialAmount, OwnerDetails)    # Call the constructor of the parent class.
        self.AccType = "Savings"                                # Account Type of the account.
        self.DepositBenefits = 0.08                             # Deposit Benefits of the account.
        self.WithdrawFee = 0.02                                 # Withdrawal Fee of the account.

    def Withdraw(self, Amount: float) -> None:
        # Check if the transaction is viable.
        try:
            self.ViableTransaction(Amount)                                      # Check if the transaction is viable.
            self.Balance -= Amount                                              # Subtract the amount from the balance.
            self.Balance -= (Amount * self.WithdrawFee)                         # Subtract the withdrawal fee from the balance.
            directory = os.path.dirname(os.path.abspath(__file__))              # Get the directory path of the current file.
            filename = f"{self.AccNo}.csv"                                      # Create the filename using the account number.
            # Create the full file path by joining the directory path and the filename.
            filepath = os.path.join(directory + '/Account_Statements', filename)
            
            with open(filepath, 'a', newline='') as file:                       # Open the CSV file in append mode.
                writer = csv.writer(file)                                       # Create a CSV writer object.
                # Write the deposit operation.
                writer.writerow([datetime.datetime.now(), 'Withdraw', 'N/A', f"${Amount:.2f}", f"${self.Balance}"])
            print(f"\n$ {Amount:.2f} has been withdrawn successfully. ✅")
            self.GetBalance()                                                   # Display the account balance.
        # If the transaction is not viable, then InsufficientBalanceError is raised.
        except InsufficientBalanceError as error:
            print(f"\nWithdraw interrupted: {error} ❌")




