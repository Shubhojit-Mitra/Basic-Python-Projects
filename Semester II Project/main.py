from BankAccount import *

owners = [
    {
        "Name": "Dave",
        "Age": 25,
        "Phone": "9172639472",
    },
    {
        "Name": "John",
        "Age": 30,
        "Phone": "9172908763",
    },
    {
        "Name": "Jane",
        "Age": 35,
        "Phone": "9173845474",
    },
    {
        "Name": "Alice",
        "Age": 28,
        "Phone": "9173847562",
    }
]





if __name__ == "__main__":

    """
    Methods in BankAccount Class:

    1. CreateBankStatements
    2. StoreOwnerDetails
    3. AccountDetails
    4. GetBalance
    5. Deposit
    6. Withdraw
    7. Transfer
    """

    filename = "OwnerDetails.csv"

    acc1 = BankAccount("2937400001", 1000, owners[0])
    acc2 = BankAccount("9462300002", 2000, owners[1])
    acc3 = BankAccount("3349800003", 3000, owners[2])
    acc4 = BankAccount("6875400004", 4000, owners[3])

    acc1.StoreOwnerDetails(filename)
    acc1.CreateBankStatements()

    acc1.Deposit(200)

    acc1.Withdraw(1000)
    # acc1.GetBalance()

    acc1.Transfer(50, acc2)

    # acc2.GetBalance()

    acc3 = RewardsAccount("3349800003", 3000, owners[2])
    acc3.StoreOwnerDetails(filename)
    acc3.CreateBankStatements()


    acc3.AccountDetails()
    # acc1.AccountDetails()

    acc3.Deposit(2000) 

    acc4 = SavingsAccount("6875400004", 4000, owners[3])
    acc4.Deposit(2000)
    acc4.Withdraw(1000)
    



