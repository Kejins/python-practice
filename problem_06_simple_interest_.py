invest_or_borrow = input("Are you calculating interest for an investment or a loan? (Enter in all Lowercase) ")

if invest_or_borrow == "investment":
    principal = int(input("Very well! Enter how much money you initially invested (Don't include dollar symbol): "))
    rate = float(input("Enter your annual interest rate (Don't include percent symbol): "))/100
    time = int(input("Enter how many years it has been since the initial investment: "))
    interest = principal*rate*time
    print("The total simple interest that has accumulated is $" + str(interest))
elif invest_or_borrow == "loan":
    principal = int(input("Very well! Enter how much money you initially borrowed (Don't include dollar symbol): "))
    rate = float(input("Enter your annual interest rate (Don't include percent symbol): "))/100
    time = int(input("Enter how many years it has been since the loan date: "))
    interest = principal*rate*time
    print("The total simple interest that has accumulated is $" + str(interest))
else:
    print("Error! Make sure to only type in either investment or loan in all lowercase.")