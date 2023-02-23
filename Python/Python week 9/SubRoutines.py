"""Building a subroutine

def identifier():
    block-code
    block-code
    block-code
    block-code
    block-code
Normal outside - not part of the subroutine
Normal outside - not part of the subroutine
Normal outside - not part of the subroutine

Subroutine innvocation
We need to invoke subroutines

"""


def greeting():
    print("Hello, World!")
    print("Welcome to python programming")
    print("Have a nice day \n")


greeting()  # Invoking (calling) the subroutine.

"""Building a subroutine with parameters

def identifier(parameter1, parameter2, parameter3, ..., parameterN):
    block-code
    block-code
    block-code
    block-code
    block-code
Normal outside - not part of the subroutine
Normal outside - not part of the subroutine
Normal outside - not part of the subroutine

Subroutine Innvocation
We need to invoke subroutines

"""


def greeting2(name):
    print("Hello, World!")
    print(f"Welcome {name}. This is python programming")
    print("Have a nice day! \n")


greeting2("Bob Johnson")
