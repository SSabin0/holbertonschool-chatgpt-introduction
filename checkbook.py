#!/usr/bin/python3

class Checkbook:
    """
    A simple checkbook class to manage a bank balance.
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Increases the balance by the specified amount.
        """
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Decreases the balance if funds are sufficient.
        """
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            print("Goodbye!")
            break
        elif action.lower() == 'balance':
            cb.get_balance()
        elif action.lower() in ['deposit', 'withdraw']:
            try:
                raw_amount = input("Enter the amount: $")
                amount = float(raw_amount)
                
                if action.lower() == 'deposit':
                    cb.deposit(amount)
                else:
                    cb.withdraw(amount)
                    
            except ValueError:
                # This catches non-numeric inputs like 'test' or 'abc'
                print("Invalid input. Please enter a numeric value (e.g., 10.50).")
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()