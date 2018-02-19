name = str(input("What is your name? "))

age = int(input("What is your age? "))

if 17 < age < 31:
    print("Welcome to the holiday {}!".format(name))
elif age < 18:
    print("We apologize, you are not allowed on this trip.")
    print("{}, please come back in {} years.".format(name, 18 - age))
else:
    print("We apologize, you are not allowed on this trip.")
