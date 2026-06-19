

def factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    print(factors)

factors(int(input("Enter a number: ")))