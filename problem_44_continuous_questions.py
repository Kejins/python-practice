
def continuous_questions(answer):
    total = 0
    while answer != 0:
        answer = int(input("Enter a number (0 to stop): "))
        total += answer
    print(total)

continuous_questions(1)