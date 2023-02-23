LegalAge = 21
passCode = "password123"

userAge = int(input("Please input your age"))

if (userAge >= LegalAge):
    print("Access Granted")
    userpass = input("Now enter the passcode")
    if (userpass == passCode):
        print("Full access granted")
    else:
        attempts = 1
        while attempts <= 3:
            attempts += 1
            print("You have entered the wrong passcode too many times. You have now been temporarily locked out. Please try again later.")
        print("Access Denied")
else:
    print("You are not old enough to use this service.")
