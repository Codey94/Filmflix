# File handling in python

# Read and write

# File modes
# reading (r)
# writing (w) Will OVERWRITE files entirely
# appending (a) will append to the end of the file
# Plus sign

# Open(filepath, openmode)

myfile = open
(r"D:\Code projects\DFE 3\Python\someData.txt", "r")

# Be sure to close the file when done to prevent memory leakage.

# Reading Files
"""
read() - Will read the rest of the file, as one big string
readline() - Will read line by line. Cursor starts from the top.
readlines() - Will the read the fill as a list of lines.
seek() - Will reposition the cursor.
close() - Will close the file.

"""

# myfile.readlines()
# myfile.readline()
# myfile.seek(0)
# myFileData = myfile.read()


# Writing to files
# myfile.write("my written data that will end up in the file. Have a nice day")

# myList = ["\nline1", "\nline2" "\nline3"]
# myfile.write("")

# Excercise 1:# Write a program that reads a number from a file and adds it to another number in a variable, printing the sum. 

# Exercise 2: Write a program that prompts the user to enter some text, and then saves that text to a file.


# Exercise 3: Write a program that opens a big file and reads its content. The program should count the number of lines in the file and print the count to the console.

myFileCount = open(r"D:\Code projects\DFE 3\Python\countFile.txt" "r")

myFileData = MyFileCount.read()

lineCount = len(myFileData)

print(lineCount)
