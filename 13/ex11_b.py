class ATM:
    # Class variable
    total_balance = 0
    
    def __init__(self, balance):
        # Instance variable
        self.balance = balance
        ATM.total_balance += balance
        
    def deposit(self, amount):
        self.balance += amount
        ATM.total_balance += amount
        return amount
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            ATM.total_balance -= amount
            return amount
        else:
            return "Insufficient balance"
atm1 = ATM(1000)
print("ATM Balance", atm1.balance) 
print("ATM Total Balance", ATM.total_balance)
print("ATM Deposit", atm1.deposit(500))
print("ATM Total Balance", ATM.total_balance)
print("ATM Withdraw", atm1.withdraw(700)) 
print("ATM Total Balance", ATM.total_balance)
print("ATM Withdraw", atm1.withdraw(1000)) 
print("ATM Total Balance", ATM.total_balance)
