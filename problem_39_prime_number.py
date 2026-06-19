from sympy import isprime
def prime(n):
    if isprime(n) == True:
        print(f"{n} is a prime number!")
    elif isprime(n) == False:
        print(f"{n} is not a prime number.")
    else:
        print("Error. Please try again")

num = int(input("Enter a number: "))
prime(num)
