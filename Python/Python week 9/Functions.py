# Functions
# functions are similar to subroutines

"""Building a Function

def indentifier():
    block-code
    block-code
    block-code
    block-code
    return value

Functions will end with a return statement

"""


# def myfunction():
#     return 10


# myfunction()

# myNum = myfunction()  # 10
# print(myNum)

# myString = input("Enter a String") # (Whatever the user typed in, before pressing enter)

"""Parameterised Function

def identifier(param):   # Input

    block-code
    block-code           # Process  
    block-code

    return value          # Output  

"""


# def plus10(x):
#     x += 10
#     return x


# myInt = plus10(90)  # plus10(90) = 100
# print(myInt)


def multiply(x, y):
    x = x * y
    return x


multiply(2, 4)
print(multiply(2, 4))


def squared(x):
    x = x * x
    return x


mySquareNum = squared(6)
print(mySquareNum)


def powerfunc(x, y):
    x = x ** y
    return x


print(powerfunc(2, 3))


def sumOfAll(num, num1, num2, num3, num4):
    x = num + num1 + num2 + num3 + num4
    return x


print(sumOfAll(15, 30, 20, 10, 5))


def sumList(list):
    summed = 0
    for nums in list:
        summed = summed + nums
    return summed


myList = [100, 50, 50, 20]
print(sumList(myList))


def findLargest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print(findLargest(myList))

# Build a function that takes in a list of numbers, finds the number of even numbers in it.


def countEvenNumbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count


myNums = [12, 34, 53, 11, 49, 7, 30, 45, 44, 80, 12]

print(countEvenNumbers(myNums))


# Scoping


# Global makes a variable global

def mysub():
    global y  # This makes y global and able to be accessed outside of this subroutine
    y = 100
    print("Subroutine prints:", x)
    print("Subroutine prints:", y)
    # Code Block
    # Code Block
    # Code Block
    # Code Block
    # Code Block


x = 100

mySub()
print(f"Me, Printing: {x}")
# Will throw an error because y has been declared locally and we are calling it globally.
print(f"Me, Printing: {y}")
