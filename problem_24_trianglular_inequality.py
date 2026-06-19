def triangle(sidea, sideb, sidec):
    if sidea + sideb > sidec and sidea + sidec > sideb and sideb + sidec > sidea:
        print("That is a valid triangle!")
    else:
        print("That is not a valid triangle.")

a = float(input("Enter the value of one side of the triangle"))
b = float(input("Enter the value of another side of the triangle"))
c = float(input("Enter the value of another side of the triangle"))

triangle(a,b,c)