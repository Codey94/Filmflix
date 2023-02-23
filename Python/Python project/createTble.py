from dbConnect import *

tableGen = """
CREATE TABLE Films (
	"FilmID" INTEGER NOT NULL UNIQUE,
	"Title" TEXT,
	"Artist" TEXT,
	"Genre" TEXT,
	PRIMARY KEY("FilmID" AUTOINCREMENT)
)
"""

cursor.execute(tableGen)
