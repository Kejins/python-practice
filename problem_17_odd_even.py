def odd_even(value):
    if value % 2 == 0:
        print("That value is even")
    elif value % 2 == 1:
        print("That value is odd")
    elif value % 2 != 1 or value % 2 != 0:
        print("That value is neither even or odd")

print("Before you begin, note that numbers with decimals cannot be even or odd")
number = float(input("Enter a number: "))
odd_even(number)
