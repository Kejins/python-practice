#months 1-12

def days_months(month_number):
    if month_number == 2:
        print("That month is February and it has 28/29 days.")
    elif month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
        print("That month has 30 days in it.")
    elif month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12:
        print("That month has 31 days in it.")

num = int(input("Enter a month number from 1-12: "))
days_months(num)