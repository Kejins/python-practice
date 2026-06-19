base_bill = float(input("Enter the base bill: "))
tax = float(input("Enter the tax percentage: "))/100
total = base_bill + (base_bill*tax)
print("The total bill is " + str(total))