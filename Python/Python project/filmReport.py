from dbConnect import *
from time import sleep
from readFilm import read
from Reports.byDirector import viewDirector
from Reports.byRating import viewRatings
from Reports.byYear import viewYears
from Reports.byGenre import viewGenre


def report():
    reportUI = """
	Reports menu

	Please Select an Option Below:
		1. View all movies and details
		2. View by Genre
		3. View by Director
		4. View by Rating
                5. View by Year
                6. Back to main menu
	"""
    reportOptions = ["1", "2", "3", "4", "5", "6"]
    reportChoice = ""
    print(reportUI)
    while reportChoice not in reportOptions:
        reportChoice = input(
            "Please select the report you would like to see: ")
        if reportChoice not in reportOptions:
            print(reportChoice, "is not a valid report option")
            sleep(2)
    return reportChoice


if __name__ == "__main__":
    reportMenu = True
    while reportMenu:
        userChoice = report()
        print("you've selected userchoice", userChoice)
    # if elifs to run the chosen module
        if userChoice == "1":
            print("some text")
            read()
            sleep(2)
        elif userChoice == "2":
            viewGenre()
            sleep(2)
        elif userChoice == "3":
            viewDirector()
            sleep(2)
        elif userChoice == "4":
            viewRatings()
            sleep(2)
        elif userChoice == "5":
            viewYears()
            sleep(2)
        else:

            backOption = input(
                "Do you want to return to the main menu? Y/N? ")
            if backOption == "Y" or backOption == "Yes" or backOption == "yes" or backOption == "y":
                print("Returning you to the main menu.")
                sleep(2.5)
                reportMenu = False

            else:
                backOption == "N" or backOption == "n" or backOption == "No" or backOption == "no"
                sleep(2)
