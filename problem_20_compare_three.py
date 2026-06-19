def compare(value1, value2, value3):
    if value1 > value2 and value1 > value3:
        print(f"{value1} is the greatest value")
    elif value2 > value1 and value2 > value3:
        print(f"{value2} is the greatest value")
    elif value3 > value1 and value3 > value2:
        print(f"{value3} is the greatest value")
    else:
        print("error")

v1 = float(input("Enter a number: "))
v2 = float(input("Enter another number: "))
v3 = float(input("Enter another number: "))
compare(v1, v2, v3) 