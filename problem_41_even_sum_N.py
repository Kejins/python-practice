
def func(n):
    count = 0
    for i in range (n+1):
        if i % 2 ==0:
            count += i
    print(count)

num = int(input("Enter a number: "))
func(num)