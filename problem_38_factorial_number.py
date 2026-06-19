def calculator(number):
    output = 1
    for i in range(1, 1 + number):
        output *= i
    print(output)
    

value = int(input("Enter an integer: "))
calculator(value)