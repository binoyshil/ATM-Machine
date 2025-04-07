from datetime import date

class ATM:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

# A function for checking balance 

    def check_balance(self):
        print(f"\nYour current balance is: ${self.balance}")


# Function for bank statements 

    def mini_statement(self):
        print("\n--- Mini Statement ---")
        if len(self.transactions) == 0:
            print("No transactions yet.")
        else:
            for t in self.transactions[-5:]:
                print(t)
# Function for withdraw money . 


    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            timestamp = date.today()
            self.transactions.append(f"Withdrawn ${amount} on {timestamp}")
            print(f"${amount} withdrawn successfully.")
            
#Function to change the pin . 

    def change_pin(self):
        current = input("Enter current PIN: ")
        if current == self.pin:
            new_pin = input("Enter new PIN: ")
            confirm = input("Confirm new PIN: ")
            if new_pin == confirm:
                self.pin = new_pin
                print("PIN changed successfully.")
            else:
                print("PINs do not match.")
        else:
            print("Incorrect current PIN.")
            
# Function for the main menu. 

    def main_menu(self):
        while True:
            print("\n====== MAIN MENU ======")
            print("1. Check Balance")
            print("2. Mini Statement")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.mini_statement()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")



#Now, Login into your account . 

account_number = "123456"
account_pin = "1234"
user_balance = 5000

entered_acc = input("Enter your account number: ")
entered_pin = input("Enter your PIN: ")

if entered_acc == account_number and entered_pin == account_pin:
    atm = ATM(account_number, account_pin, user_balance)
    atm.main_menu()
else:
    print("Incorrect account number or PIN.")
