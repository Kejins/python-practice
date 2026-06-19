def vowel_or_consonant(letters):
    letters.lower()
    if letters == "a":
        print("That is vowel")
    elif letters == "e":
        print("That is a vowel")
    elif letters == "i":
        print("That is a vowel")
    elif letters == "o":
        print("That is a vowel")
    elif letters == "u":
        print("That is a vowel")
    else:
        print("That is a consonant")
letter = input("Enter a letter: ")
vowel_or_consonant(letter)