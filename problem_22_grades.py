def grades(percentage):
    if percentage > 100:
        print("That is not an appropiate score")
    elif percentage == 100 or percentage >= 97:
        print("You get an A+ for that score")
    elif percentage >= 93:
        print("You get an A for that score")
    elif percentage >= 90:
        print("You get an A- for that score")
    elif percentage >= 87:
        print("You get a B+ for that score")
    elif percentage >= 83:
        print("You get a B for that score")
    elif percentage >= 80:
        print("You get a B- for that score")
    elif percentage >= 77:
        print("You get a C+ for that score")
    elif percentage >= 70:
        print("You get a C for that score")
    elif percentage < 70:
        print("You get an F for that score")

score = float(input("Enter your score: "))
grades(score)