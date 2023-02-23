from connect import *
from time import sleep

def read():
	cursor.execute("SELECT * FROM songs")
	query = cursor.fetchall()
	
	if query == []:
		print("The Database is empty.")
		sleep(2)
		return 0
	else:
		print("\nSongs List:")
		for record in query:
			print(record)
		return 1


if __name__ == "__main__":
	read()

# checking the datatype
"""
print(query)
print(type(query))
print(query[0])
print(type(query[0]))
"""