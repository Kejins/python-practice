def divisibility(value):
    if value % 3 == 0 and value % 5 == 0:
        print(f"{value} is divisible by both 3 and 5")
    elif value % 3 == 0 and value % 5 !=0:
        print(f"{value} is divisible by 3 but not divisible by 5")
    elif value % 3 != 0 and value % 5 == 0:
        print(f"{value} is divisible by 5 but not divisible by 3")
    elif value % 3 != 0 or value % 5 != 0:
        print(f"{value} is not divisible by both 3 and 5")
    else:
        print("error")

number = float(input("Enter a value: "))
divisibility(number)