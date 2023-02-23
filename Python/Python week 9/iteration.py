# iteration.
# Repeating/Looping code.
# For and While loops.

# For-in Loop
"""
2nd parameter is start and end point, and 3rd parameter governs the step/increment (start, end, step) Negative values will count down instead.
"""
for n in range(3, 20, 2):
    print(f"this is the {n}th iteration in the loop")


# for-in with collections

namesList = ["bob", "george", "Oliver", "Master Yi", "Tracer", "Genji", "Mei"]

for name in namesList:
    print(f"The currently selected name is {name}")
    if name == "Tracer":
        break


# While Loop

"""
Building a while statement:

while condition:
    indented-code to loop
    indented-code to loop
    indented-code to loop
    indented-code to loop
    indented-code to loop
outside-code runs outside
outside-code runs outside
outside-code runs outside
outside-code runs outside

"""
# will run indefinitly until the condition is disatisfied
x = 10
while x < 100:
    print("this is a loop")
    x += 10  # x = x + 10


# Iteration
# Repeating/Looping code.
# For and While Loops

# For-In Loop
"""
for index-variable in collection:
	indented-code to repeat/loop
	indented-code to repeat/loop
	indented-code to repeat/loop
	indented-code to repeat/loop

outside-code exits the for loop; is just regular code
outside-code exits the for loop; is just regular code
outside-code exits the for loop; is just regular code
outside-code exits the for loop; is just regular code

"""

"""
# starts from zero
for n in range(10):
	print(f"this is the {n}th iteration in the loop.")



# Picking the starting point with range (start, end)
for n in range(3, 10):
	print(f"this is the {n}th iteration in the loop.")


# a Third Parameter determines the step/increment (start, end, step)
for n in range(10, 13, 3):
	print(f"this is the {n}th iteration in the loop.")


# Negative values will count down instead.
for n in range(10, 5, -1):
	print(f"this is the {n}th iteration in the loop.")
"""

# For-In with collections

namesList = ["Bob", "George", "Oliver", "Master Yi", "Tracer", "Genji", "Mei"]
for name in namesList:
    print(f"The Currently selected name is {name}")
    if name == "Tracer":
        break


# While Loops

"""Building a While Statement

while condition:
	indented-code to loop
	indented-code to loop
	indented-code to loop
	indented-code to loop
	indented-code to loop
outside-code runs
outside-code runs
outside-code runs
outside-code runs

"""
# While Loops will run indefinitely until the condition is disatisfied.
x = 10
while x < 100:  # x = 100
    print(f"this is a loop. x is currently {x}")
    # x = x + 10
    x += 10

print("standard, regular, box standard code.")


# Excercise:
# Using iteration
# Adapt the Age/Passcode program so that the user can make an indefinite number of attempts on the passcode.
# Extension: After the first attempt fails, starting the counting number of atttempts.
