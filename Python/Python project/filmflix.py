from readFilm import read
from addFilm import insertFilm
from updateFilm import update
from deleteFilm import delete
from time import sleep


def menu():
    menuUI = """
	Welcome to FilmFlix Database v1.01

	Please Select an Option Below:
		1. Display films in the database.
		2. Add a new film to the database.
		3. Update an existing film.
		4. Delete a film.
        5. Report.
		6. Exit application.
	"""
    options = ["1", "2", "3", "4", "5", "6"]
    choice = ""
    print(menuUI)
    while choice not in options:
        choice = input("Please select an option from the menu: ")
    if choice not in options:
        print(choice, "is not a valid option.")
        sleep(1)
    return choice


if __name__ == "__main__":
    mainProgram = True
    while mainProgram:
        userChoice = menu()
        # if elifs to run the chosen module
        if userChoice == "1":
            read()
            sleep(2)
        elif userChoice == "2":
            insertFilm()
            sleep(2)
        elif userChoice == "3":
            update()
            sleep(2)
        elif userChoice == "4":
            delete()
            sleep(2)
        else:
            mainProgram = False
    print("Thanks for using this application. Goodbye")
    input("Press Enter to exit...")
