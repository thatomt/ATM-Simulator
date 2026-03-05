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

balance = 1000

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        check_balance(balance)
    elif choice == "2":
        balance = deposit(balance)
