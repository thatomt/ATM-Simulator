def check_balance(balance):
    print("Your balance is:", balance)

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount
    
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
        return balance
    return balance - amount
