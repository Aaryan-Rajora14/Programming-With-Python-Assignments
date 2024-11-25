# 9. Write a program that simulates a simple banking system where the user can:
'''Check balance
Deposit money
Withdraw money
The program should validate the inputs and ensure sufficient balance for withdrawals.
'''

balance = 11000
while True:
    print("\nWelcome to the Simple Banking System")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    ch = int(input("Enter your choice:"))
    if ch == 1:
        print(f"Your current balance is {balance}")
        
    elif ch == 2:
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print((f"You have deposited {amount} successfully"))
        
    
    elif ch == 3:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print(f"You have withdrawn {amount} successfully")
    
    elif ch==4:
        print("Thank You for Using ATM")
        break
    else:
        print("Invalid options")