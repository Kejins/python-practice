def leap(years):
    if years % 4 == 0:
        print("That is a leap year!")
    elif years % 4 != 0:
        print("That isn't a leap year.")

year = int(input("Enter a year: "))
leap(year)
