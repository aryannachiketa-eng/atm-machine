# deposit.py

from balance import balance

def deposit_money():
    global balance
    amount = int(input("\nEnter amount to deposit: ₹"))
    
    if amount > 0:
        balance += amount
        print("₹", amount, "deposited successfully.")
        print("Updated Balance: ₹", balance)
    else:
        print("Invalid amount.")