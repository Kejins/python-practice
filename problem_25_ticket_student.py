def ticket(age, student_status):
    if age <= 12:
        price = 10
        print(f"The price of your ticket is {price}")
    elif age >= 13 and age <=17:
        price = 15
        print(f"The price of your ticket is {price}")
    elif age >= 18 and student_status == "y":
        price = 15
        print(f"The price of your ticket is {price}")
    elif age >= 18 and age <= 64:
        price = 25
        print(f"The price of your ticket is {price}")
    elif age < 64:
        price = 15
        print(f"The price of your ticket is {price}")

ages = int(input("Enter your age: "))
student = input("Are you a student? (y or n) ")
ticket(ages, student)