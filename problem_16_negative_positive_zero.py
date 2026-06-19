
def determine(value):
    if value < 0:
        print("That value is negative")
    elif value == 0:
        print("That value is 0")
    elif value > 0:
        print("That value is greater than 0")
    else:
        print("The inserted value is not a number")

number = float(input("Enter a value: "))
determine(number)