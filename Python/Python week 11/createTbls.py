from connect import *

tableGen = """
CREATE TABLE songs (
	"SongID" INTEGER NOT NULL UNIQUE,
	"Title" TEXT,
	"Artist" TEXT,
	"Genre" TEXT,
	PRIMARY KEY("SongID" AUTOINCREMENT)
)
"""

cursor.execute(tableGen)