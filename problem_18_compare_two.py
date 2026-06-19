def compare(value1, value2):
    if value1 > value2:
        print(f"{value1} is greater than {value2}")
    elif value2 > value1:
        print(f"{value2} is greater than {value1}")

v1 = float(input("Enter a number: "))
v2 = float(input("Enter another number: "))
compare(v1, v2)