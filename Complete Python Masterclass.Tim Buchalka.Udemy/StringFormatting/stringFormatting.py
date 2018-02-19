age = 24
print("My age is " + str(age) + " years")

print("""My age is {0} years 
and your is {1}""".format(age, 30))

print("There are {0} days in {1}".format(31, "january"))

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

