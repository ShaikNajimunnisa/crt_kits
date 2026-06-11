#Digital Wallet Transaction System:
class User:
    def __init__(self, name):
        self.name = name

class Wallet:
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance
        self.transactions = []  # List → Transactions
    
    def add_money(self, amount):
        self.balance += amount
        self.transactions.append(f"Added ₹{amount}")
    
    def transfer_money(self, amount):
        if amount <= self.balance:
            opening = self.balance
            self.balance -= amount
            self.transactions.append(f"Transferred ₹{amount}")
            self.receipt(opening, amount, "SUCCESSFUL")
        else:
            self.receipt(self.balance, amount, "FAILED")
    
    def show_balance(self):
        print(f"Current Balance : ₹{self.balance}")
    
    def receipt(self, opening, transfer, status):
        print("="*50)
        print("          TRANSACTION RECEIPT")
        print("="*50)
        print(f"\nUser Name       : {self.user.name}\n")
        print(f"Opening Balance : ₹{opening}\n")
        print(f"Transfer Amount : ₹{transfer}\n")
        print(f"Current Balance : ₹{self.balance}\n")
        print(f"Status          : {status}\n")
        print("="*50)

# Test Case
u = User("Noah")
w = Wallet(u, 10000)
w.transfer_money(2500)