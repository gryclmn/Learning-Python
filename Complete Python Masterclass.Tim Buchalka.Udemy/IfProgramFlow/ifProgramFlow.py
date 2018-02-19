parrot = ("Norwegian Blue")

letter = str(input("Enter a character: "))

if letter.lower() not in parrot.lower():
    print("I dont need that letter")
else:
    print("Give me an '{}', Bob".format(letter))
