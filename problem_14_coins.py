#Given an amount of money, determine how many quarters, dimes, nickels, and pennies it contains.

def coin_calculator(dollar):

    single_value = dollar*100

    quarters = single_value // 25
    single_value %=25

    dimes = single_value // 10
    single_value %= 10

    nickels = single_value // 5
    single_value %= 5

    pennies = single_value

    print("Quarters: " + str(quarters) + " Dimes: " + str(dimes) + " Nickels: " + str(nickels) + " Pennies: " + str(pennies))

dollar = float(input("Enter how much money you'd like to convert: "))
coin_calculator(dollar)