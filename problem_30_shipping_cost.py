def shipping(weight, destination):
    destination = shipping_destination.lower()
    if destination == "local":
        base = 3.50
        rate = .75
        cost = base + (weight*rate)
        print(f"The  total cost to ship that item locally is ${cost}")
    elif destination == "regional":
        base = 4.5
        rate = 1
        cost = base + (weight*rate)
        print(f"The  total cost to ship that item regionally is ${cost}")
    elif destination == "national":
        base = 6
        rate = 1.4
        cost = base + (weight*rate)
        print(f"The  total cost to ship that item nationally is ${cost}")
    elif destination == "international":
        base = 12
        rate = 4.3
        cost = base + (weight*rate)
        print(f"The  total cost to ship that item internationally is ${cost}")

measured_weight = float(input("Enter the weight of what you're shipping in lbs: "))
shipping_destination = input("Enter the type of destination you'd like use to ship to: (Options being local, regional, national, and international): ")
shipping(measured_weight, shipping_destination)