def calculator(number):
    a, b = 0, 1

    if number == 1:
        print(a)
    elif number == 2:
        print(b)
    else: 
        for i in range(number - 2):
            c = a + b
            a, b = b, c
        print(c)
    
    
    

value = int(input("Enter an integer: "))
calculator(value)
