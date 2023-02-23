from connect import *
from readSongs import read
from time import sleep

def update():
	if read() == 0:
		print("There are no songs to update.")
		return
	else:
		songID = input("Enter the ID of the Song you'd Like to update: ")

		title = input("Enter the new title: ")
		artist = input("Enter the new artist: ")
		genre = input("Enter the new Genre: ")

		updateSQL = f"""
		UPDATE songs
		SET Title = "{title}", Artist = "{artist}", Genre = "{genre}"
		WHERE SongID = {songID}
		;

		"""
		cursor.execute(updateSQL)
		conn.commit()
		print(f"Song ID: {songID} has been successfully updated.")
		sleep(3)
	

if __name__ == "__main__":
	update()