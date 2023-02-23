from readSongs import read
from addSongs import insertSongs
from updateSongs import update
from deleteSongs import delete
from time import sleep

def menu():
	menuUI = """
	Welcome to Music Database v1.01

	Please Select an Option Below:
		1. Display Songs in the database
		2. Add a new song to the database
		3. Update an existing Song
		4. Delete a Song.
		5. Exit application.
	"""
	options = ["1", "2", "3", "4", "5"]
	choice = ""
	print(menuUI)
	while choice not in options:
		choice = input("Select an option from the menu: ")
		if choice not in options:
			print(choice, "isnt a valid option.")
			sleep(0.5)
	return choice

if __name__ == "__main__":
	mainProgram = True
	while mainProgram:
		userChoice = menu()
		# if elifs to run the chosen module
		if userChoice == "1":
			read()
		elif userChoice == "2":
			insertSongs()
		elif userChoice == "3":
			update()
		elif userChoice == "4":
			delete()
		else:
			mainProgram = False
	print("Thanks for using this application.")
	input("Press Enter to exit...")