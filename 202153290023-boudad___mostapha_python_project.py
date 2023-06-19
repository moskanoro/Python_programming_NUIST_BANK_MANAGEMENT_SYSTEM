# 202153290023 BOUDAD MOSTAPHA
# 06/19/2023



import os
import pickle
import pathlib

# Bank Account class
class Account:
    def __init__(self):
        self.accNo = 0
        self.name = ''
        self.accType = ''
        self.deposit = 0

    def createAccount(self):
        self.accNo = int(input("Enter the account number: "))
        self.name = input("Enter the account holder name: ")
        self.accType = input("Enter the account type [Business/Student/Retirement]: ")
        self.ph = input("Enter phone number: ")
        self.add = input("Enter Home address: ")
        self.deposit = int(input("Enter the initial amount: "))
        print("\nYour account has been created successfully.")

    def showAccount(self):
        print("Account Number:", self.accNo)
        print("Account Holder Name:", self.name)
        print("Client Phone Number: ", self.ph)
        print("Client Home Address: ", self.add)
        print("Account Type:", self.accType)
        print("Account Balance:", self.deposit)

    def modifyAccount(self):
        print("Account Number:", self.accNo)
        self.name = input("Modify account holder name: ")
        self.accType = input("Modify account type: ")
        self.ph = input("Modify phone number: ")
        self.add = input("Modify Home address: ")
        self.deposit = int(input("Modify account balance: "))

    def depositAmount(self, amount):
        self.deposit += amount
        self.updateAccount()

    def withdrawAmount(self, amount):
        if self.deposit >= amount:
            self.deposit -= amount
            self.updateAccount()
        else:
            print("Insufficient balance in the account")

    def transferAmount(self, account, amount):
        if self.deposit >= amount:
            self.deposit -= amount
            account.deposit += amount
            print("Amount transferred successfully")
        else:
            print("Insufficient balance in the account")

    def updateAccount(self):
        file = pathlib.Path("accounts.data")
        if file.exists():
            with open('accounts.data', 'rb') as infile:
                mylist = pickle.load(infile)

            for i, account in enumerate(mylist):
                if account.accNo == self.accNo:
                    mylist[i] = self

            with open('accounts.data', 'wb') as outfile:
                pickle.dump(mylist, outfile)


# Function to perform login
def login():
    usernames = {
        'admin': 'admin',
        'teller': 'teller',
        'client': 'client'
    }

    username = input("Username: ")
    password = input("Password: ")  

    if username in usernames and password == usernames[username]:
        if username == 'admin':
            adminMenu()
        elif username.startswith('teller'):
            tellerMenu()
        elif username.startswith('client'):
            clientMenu()
    else:
        print("Invalid username or password.")
        login()
        
# Function to change usernames and passwords
def changeCredentials():
    credentials_file = pathlib.Path("credentials.data")
    if credentials_file.exists():
        with open('credentials.data', 'rb') as infile:
            usernames = pickle.load(infile)
    else:
        usernames = {
            'admin': 'admin',
            'teller': 'teller',
            'client': 'client'
        }

    print("\nChange Username and Password")
    print("===============================")
    print("1. Change Admin Username and Password")
    print("2. Change Teller Username and Password")
    print("3. Change Client Username and Password")
    print("4. Back")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        changeUsernamePassword('admin', usernames)
    elif choice == 2:
        changeUsernamePassword('teller', usernames)
    elif choice == 3:
        changeUsernamePassword('client', usernames)
    elif choice == 4:
        return
    else:
        print("Invalid choice")

    with open('credentials.data', 'wb') as outfile:
        pickle.dump(usernames, outfile)

    print("Username and password changed successfully")

# Function to change username and password for a role
def changeUsernamePassword(role, usernames):
    if role in usernames:
        new_username = input("Enter the new username: ")
        new_password = input("Enter the new password: ")
        usernames[role] = new_password
        print("Username and password changed for", role)
    else:
        print("Invalid role")
        
# Function to create a new account
def writeAccount():
    account = Account()
    account.createAccount()

    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)
            mylist.append(account)
        with open('accounts.data', 'wb') as outfile:
            pickle.dump(mylist, outfile)
    else:
        with open('accounts.data', 'wb') as outfile:
            pickle.dump([account], outfile)
    print("Account created successfully")


# Function to deposit or withdraw amount
def depAndWithd(accNum, choice):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)

        found = False
        for account in mylist:
            if account.accNo == accNum:
                found = True
                if choice == 1:
                    amount = int(input("Enter the amount to deposit: "))
                    account.depositAmount(amount)
                    print("Amount deposited successfully")
                elif choice == 2:
                    amount = int(input("Enter the amount to withdraw: "))
                    account.withdrawAmount(amount)
                    print("Amount withdrawn successfully")
                break
        if not found:
            print("Account not found")
    else:
        print("No records to perform deposit or withdrawal")
    input("Press any key to continue...")

# Function to transfer amount between accounts
def transfer(from_acc, to_acc, amount):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)

        from_account = None
        to_account = None
        for account in mylist:
            if account.accNo == from_acc:
                from_account = account
            if account.accNo == to_acc:
                to_account = account

        if from_account and to_account:
            from_account.withdrawAmount(amount)
            to_account.depositAmount(amount)
            print("Amount transferred successfully")
        else:
            print("One or both accounts not found")
    else:
        print("No records to perform the transfer")
    input("Press any key to continue...")

# Function to display account details
def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)

        found = False
        for account in mylist:
            if account.accNo == num:
                account.showAccount()
                found = True
                break
        if not found:
            print("Account not found")
    else:
        print("No records to display")
    input("Press any key to continue...")

# Function to display all account details
def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)

        for account in mylist:
            account.showAccount()
            print("===============================")
    else:
        print("No records to display")
    input("Press any key to continue...")

# Function to delete an account
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)

        found = False
        newlist = []
        for account in mylist:
            if account.accNo == num:
                found = True
            else:
                newlist.append(account)

        if found:
            with open('accounts.data', 'wb') as outfile:
                pickle.dump(newlist, outfile)
            print("Account deleted successfully")
        else:
            print("Account not found")
    else:
        print("No records to delete")
    input("Press any key to continue...")

# Function to modify an account
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)

        found = False
        for account in mylist:
            if account.accNo == num:
                account.modifyAccount()
                found = True
                break
        if not found:
            print("Account not found")
        else:
            with open('accounts.data', 'wb') as outfile:
                pickle.dump(mylist, outfile)
            print("Account modified successfully")
    else:
        print("No records to modify")
    input("Press any key to continue...")

# Function to add, modify, or delete tellers
def manageTellers():
    tellers = []
    file = pathlib.Path("tellers.data")
    if file.exists():
        with open('tellers.data', 'rb') as infile:
            tellers = pickle.load(infile)

    while True:
        print("1. Add Teller")
        print("2. Modify Teller")
        print("3. Delete Teller")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            teller = input("Enter the teller name: ")
            tellers.append(teller)
            with open('tellers.data', 'wb') as outfile:
                pickle.dump(tellers, outfile)
            print("Teller added successfully")
       
        elif choice == 2:
            if len(tellers) > 0:
                print("Current Tellers:")
                for i, teller in enumerate(tellers):
                    print(f"{i + 1}. {teller}")

                index = int(input("Enter the index of the teller to modify: ")) - 1
                if 0 <= index < len(tellers):
                    newTeller = input("Enter the modified teller name: ")
                    tellers[index] = newTeller
                    with open('tellers.data', 'wb') as outfile:
                        pickle.dump(tellers, outfile)
                    print("Teller modified successfully")
                else:
                    print("Invalid index")
            else:
                print("No tellers to modify")

        elif choice == 3:
            if len(tellers) > 0:
                print("Current Tellers:")
                for i, teller in enumerate(tellers):
                    print(f"{i + 1}. {teller}")

                index = int(input("Enter the index of the teller to delete: ")) - 1
                if 0 <= index < len(tellers):
                    del tellers[index]
                    with open('tellers.data', 'wb') as outfile:
                        pickle.dump(tellers, outfile)
                    print("Teller deleted successfully")
                else:
                    print("Invalid index")
            else:
                print("No tellers to delete")

        elif choice == 4:
            break

        else:
            print("Invalid choice")
    input("Press any key to continue...")
       
# Admin menu
def adminMenu():
    while True:
        print("\t\t\t\t===============================")
        print("\t\t\t\tBy_202153290023_BOUDAD_MOSTAPHA")
        print("\t\t\t\t===============================")
        print("\t\t\t\t           Admin Menu")

        print("1. Create New Account For Client")
        print("2. Deposit Amount for Clients")
        print("3. Withdraw Amount For Clients")
        print("4. Transfer Amount For Clients")
        print("5. Account Details For Clients")
        print("6. Display All Accounts Of Clients")
        print("7. Delete Account For Client")
        print("8. Modify Account For Clients")
        print("9. Manage Tellers [ADD/MODIFY/DELETE]")
        print("10. Change Username and Password [CLIENT/TELLER/CLIENT]")
        print("11. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            writeAccount()
        elif choice == 2:
            accNum = int(input("Enter the account number: "))
            depAndWithd(accNum, 1)
        elif choice == 3:
            accNum = int(input("Enter the account number: "))
            depAndWithd(accNum, 2)
        elif choice == 4:
            from_acc = int(input("Enter the source account number: "))
            to_acc = int(input("Enter the destination account number: "))
            amount = int(input("Enter the amount to transfer: "))
            transfer(from_acc, to_acc, amount)
        elif choice == 5:
            accNum = int(input("Enter the account number: "))
            displaySp(accNum)
        elif choice == 6:
            displayAll()
        elif choice == 7:
            accNum = int(input("Enter the account number: "))
            deleteAccount(accNum)
        elif choice == 8:
            accNum = int(input("Enter the account number: "))
            modifyAccount(accNum)
        elif choice == 9:
            manageTellers()
        elif choice == 10:
            changeCredentials()
        elif choice == 11:
            break
        else:
            print("Invalid choice")
        input("Press any key to continue...")


# Teller menu
def tellerMenu():
    tellers = []
    file = pathlib.Path("tellers.data")
    if file.exists():
        with open('tellers.data', 'rb') as infile:
            tellers = pickle.load(infile)

    if len(tellers) == 0:
        print("No tellers available. PLEASE CREATE A TELLER ACCOUNT IN ADMIN SECTION NB 9 THEN YOU CAN ENTER TO YOUR TELLER ACCOUNT HERE")
        input("Press any key to continue...")
        return

    while True:
        print("\t\t\t\t===============================")
        print("\t\t\t\tBy_202153290023_BOUDAD_MOSTAPHA")
        print("\t\t\t\t===============================")
        print("\t\t\t\t           Teller Menu")

        for i, teller in enumerate(tellers):
            print(f"{i+1}. {teller}")
        print(f"{len(tellers) + 1}. Back")

        choice = int(input("Enter your choice: "))

        if 1 <= choice <= len(tellers):
            selected_teller = tellers[choice - 1]
            print(f"You selected teller: {selected_teller}")
            while True:
                print("\t\t\t\t===============================")
                print("\t\t\t\tBy_202153290023_BOUDAD_MOSTAPHA")
                print("\t\t\t\t===============================")
                print("\t\t\t\t           Teller Options")
                print("1. Create New Account For Client")
                print("2. Deposit Amount for Clients")
                print("3. Withdraw Amount For Clients")
                print("4. Transfer Amount For Clients")
                print("5. Account Details For Clients")
                print("6. Display All Accounts Of Clients")
                print("7. Delete Account For Client")
                print("8. Modify Account For Clients")
                print("9. Exit")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                   writeAccount()
                elif choice == 2:
                     accNum = int(input("Enter the account number: "))
                     depAndWithd(accNum, 1)
                elif choice == 3:
                     accNum = int(input("Enter the account number: "))
                     depAndWithd(accNum, 2)
                elif choice == 4:
                     from_acc = int(input("Enter the source account number: "))
                     to_acc = int(input("Enter the destination account number: "))
                     amount = int(input("Enter the amount to transfer: "))
                     transfer(from_acc, to_acc, amount)
                elif choice == 5:
                     accNum = int(input("Enter the account number: "))
                     displaySp(accNum)
                elif choice == 6:
                     displayAll()
                elif choice == 7:
                     accNum = int(input("Enter the account number: "))
                     deleteAccount(accNum)
                elif choice == 8:
                     accNum = int(input("Enter the account number: "))
                     modifyAccount(accNum)
                elif choice == 9:
                    break
                else:
                    print("Invalid choice")
                input("Press any key to continue...")

        elif choice == len(tellers) + 1:
            break
        else:
            print("Invalid choice")
        input("Press any key to continue...")

# Client menu
def clientMenu():
    while True:
        print("\t\t\t\t===============================")
        print("\t\t\t\tBy_202153290023_BOUDAD_MOSTAPHA")
        print("\t\t\t\t===============================")
        print("\t\t\t\t           Client Menu")
        print("1. Deposit Amount In My Account")
        print("2. Withdraw Amount In My Account")
        print("3. Transfer Amount")
        print("4. My Account Details")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            accNum = int(input("Please Enter Your account number: "))
            depAndWithd(accNum, 1)
        elif choice == 2:
            accNum = int(input("Please Enter Your account number: "))
            depAndWithd(accNum, 2)
        elif choice == 3:
            from_acc = int(input("Enter the source account number: "))
            to_acc = int(input("Enter the destination account number: "))
            amount = int(input("Enter the amount to transfer: "))
            transfer(from_acc, to_acc, amount)
        elif choice == 4:
            accNum = int(input("Please Enter Your account number: "))
            displaySp(accNum)
        elif choice == 5:
            break
        else:
            print("Invalid choice")
        input("Press any key to continue...")


# Main menu
def mainMenu():
    while True:
        print("\t\t\t\tWELCOME TO BANK MANAGEMENT SYSTEM")
        print("\t\t\t\t===============================")
        print("\t\t\t\tBy_202153290023_BOUDAD_MOSTAPHA")
        print("\t\t\t\t===============================")
        print("\t\t\t\t           Main Menu")


        print("1. Admin")
        print("2. Teller")
        print("3. Client")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            user_type = login()
            if user_type == 'admin':
                adminMenu()
            else:
                print("Login failed. Only admins can access the admin menu.")
        elif choice == 2:
            user_type = login()
            if user_type == 'teller':
                tellerMenu()
            else:
                print("Login failed. Only tellers can access the teller menu.")
        elif choice == 3:
            user_type = login()
            if user_type == 'client':
                clientMenu()
            else:
                print("Login failed. Only clients can access the client menu.")
        elif choice == 4:
            break
        else:
            print("Invalid choice")
        input("Press any key to continue...")

# Entry point of the program
if __name__ == "__main__":
    mainMenu()
    login()
    
