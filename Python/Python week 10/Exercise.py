from random import random, randint

fullName = input("Please enter your full name.")

twoNames = fullName.split()

firstN = twoNames[0]
lastN = twoNames[1]

# print(firstN, lastN)

fInitial = firstN[0]
linitial = lastN[0]

print(f"Hey {fInitial}. {linitial}")

userRandomNum = str(randint(1000, 9999))

print(firstN + linitial + str(userRandomNum))

userName = firstN + fInitial + "#" + userRandomNum
