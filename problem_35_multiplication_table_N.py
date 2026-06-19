
def table(multiple):
    for i in range(1, 13):
        print(f"{multiple} * {i} = {multiple * i}")

n = float(input("Enter a number: "))
table(n)