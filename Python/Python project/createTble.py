from dbConnect import *

tableGen = """
CREATE TABLE Films (
	"FilmID" INTEGER NOT NULL UNIQUE,
	"Title" TEXT,
	"Director" TEXT,
	"Genre" TEXT,
    "Year" INT,
    "Rating" INT,
	PRIMARY KEY("FilmID" AUTOINCREMENT)
)
"""

cursor.execute(tableGen)
