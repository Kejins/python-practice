def three_digit(num):
    hundred = num // 100
    ten = (num // 10) % 10
    one = num % 10
    return hundred + ten + one

number = int(input("Enter a three digit number: "))


answer = three_digit(number)
print(answer)