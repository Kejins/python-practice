def triangle (a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c:
            print("This triangle is an equilateral triangle")
        elif a == b and b != c:
            print("This triangle is an isosceles triangle")
        elif a != b and b!= c and c!= a:
            print("This triangle is an scalene triangle")
    else:
        print("That is an invalid triangle")

sidea = float(input("Enter the value of side A: "))
sideb = float(input("Enter the value of side B: "))
sidec = float(input("Enter the value of side C: "))
triangle(sidea, sideb, sidec)