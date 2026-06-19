def function(words):
    count = 0
    for i in words:
        if i.lower() in "aeiou":
            count += 1
    print(count)


word = input("Enter a word: ")
function(word)