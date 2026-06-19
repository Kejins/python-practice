def divisibility(number):
    if number % 7 == 0:
        print(f"{number} is a multiple of 7")
    elif number % 7 != 0:
        print(f"{number} is not a multiple of 7")

num = float(input("Enter a number: "))
divisibility(num)