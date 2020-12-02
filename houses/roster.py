import cs50
import sys
import csv
import re
from cs50 import SQL

db = SQL("sqlite:///students.db")

# verifies correct number of arguments
if len(sys.argv) != 2:
    print(f"Usage: python roster.py house")
    exit(1)

# if 3rd arg is Gryffindor, db.execute retrieves names and birth, sorted by last name alphabetical then first alphabetical
if sys.argv[1] == "Gryffindor":
    gryffindor_students = db.execute(
        "SELECT first, middle, last, birth FROM students WHERE house ='Gryffindor' ORDER BY last ASC, first ASC")

    # loops through students and if middle name is empty the first format is used, else use the 'middle' variable
    for student in gryffindor_students:
        if student['middle'] is None:
            print(f"{student['first']} {student['last']}, born {student['birth']}")
        else:
            print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")

# if 3rd arg is Ravenclaw, db.execute retrieves names and birth, sorted by last name alphabetical then first alphabetical
elif sys.argv[1] == "Ravenclaw":
    ravenclaw_students = db.execute(
        "SELECT first, middle, last, birth FROM students WHERE house ='Ravenclaw' ORDER BY last ASC, first ASC")

    # loops through students and if middle name is empty the first format is used, else use the 'middle' variable
    for student in ravenclaw_students:
        if student['middle'] is None:
            print(f"{student['first']} {student['last']}, born {student['birth']}")
        else:
            print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")

# if 3rd arg is Hufflepuff, db.execute retrieves names and birth, sorted by last name alphabetical then first alphabetical
elif sys.argv[1] == "Hufflepuff":
    hufflepuff_students = db.execute(
        "SELECT first, middle, last, birth FROM students WHERE house ='Hufflepuff' ORDER BY last ASC, first ASC")

    # loops through students and if middle name is empty the first format is used, else use the 'middle' variable
    for student in hufflepuff_students:
        if student['middle'] is None:
            print(f"{student['first']} {student['last']}, born {student['birth']}")
        else:
            print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")

# if 3rd arg is Slytherin, db.execute retrieves names and birth, sorted by last name alphabetical then first alphabetical
elif sys.argv[1] == "Slytherin":
    slytherin_students = db.execute(
        "SELECT first, middle, last, birth FROM students WHERE house ='Slytherin' ORDER BY last ASC, first ASC")

    # loops through students and if middle name is empty the first format is used, else use the 'middle' variable
    for student in slytherin_students:
        if student['middle'] is None:
            print(f"{student['first']} {student['last']}, born {student['birth']}")
        else:
            print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")