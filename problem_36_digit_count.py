def digit_count(num):
    count = sum(ch.isdigit() for ch in str(num))
    print(count)


number = input("Enter a number: ")
digit_count(number)