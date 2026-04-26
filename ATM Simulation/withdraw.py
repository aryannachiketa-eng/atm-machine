# withdraw.py

from balance import balance

def withdraw_money():
    global balance
    amount = int(input("\nEnter amount to withdraw: ₹"))
    
    if amount <= balance:
        balance -= amount
        print("₹", amount, "withdrawn successfully.")
        print("Remaining Balance: ₹", balance)
    else:
        print("Insufficient Balance.")