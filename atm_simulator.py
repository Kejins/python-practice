is_running = True

balance = 1000.00
transaction_history = []

while is_running:
    print("1. Check balance \n2. Deposit money \n3. Withdraw money\n4. View transaction history\n5. Exit the program\n")
    print()
    
    try:
        option = int(input("\nSelect an option: "))
    except ValueError: # Makes sure that the input is an integer and not any other data type
        print("Invalid choice. Please enter a number.")
        continue
#Option 1
    if option < 1 or option > 5: #Ensures that the number is only between 1 or 5
        print("Invalid choice. Please select 1-5.")
        continue
    elif option == 1:
        print(f"Your current balance is: ${balance}")
        print()

#Option 2
    elif option == 2:
        deposit = float(input("Enter deposit amount: "))
        if deposit > 0:
            balance = balance + deposit
            print(f"Deposit successful.\nNew balance: ${balance}\n")
            transaction_history.append(f"Deposit: ${deposit}")
        else:
            print("Invalid deposit amount.")
            print()

#Option 3
    elif option == 3:
        withdraw = float(input("Enter a withdrawal amount: "))
        if withdraw > balance:
            print("\nInsufficient balance.")
            print()
        elif withdraw <= 0:
            print("\nInvalid withdrawal amount.")
        else:
            balance -= withdraw
            transaction_history.append(f"Withdrawal: ${withdraw}")
            print("Withdrawal successful")
            print(f"Your new balance is ${balance}")
            print()

#Option 4
    elif option == 4:
        print("\nTransaction History: ")
        if len(transaction_history) == 0:
            print("No transactions yet.")
        else:
            for x in transaction_history:
                print(x)
            print()

#Option 5
    elif option == 5:
        print("Thank you for using the ATM. Goodbye!")
        is_running = False
