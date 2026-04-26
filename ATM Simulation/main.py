# main.py

from balance import display_balance
from deposit import deposit_money
from withdraw import withdraw_money
from statement import mini_statement

while True:
    print("\n====== ATM MACHINE ======")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Mini Statement")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_balance()

    elif choice == 2:
        deposit_money()

    elif choice == 3:
        withdraw_money()

    elif choice == 4:
        mini_statement()

    elif choice == 5:
        print("Thank you for using Axis ATM.")
        break

    else:
        print("Invalid Choice. Please try again.")