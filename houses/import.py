import cs50
import sys
import csv
from cs50 import SQL

db = SQL("sqlite:///students.db")

# verifies correct number of arguments
if len(sys.argv) != 2:
    print(f"Usage: python import.py characters.csv")
    exit(1)

# opens CSV document and assigns to an object
with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Reads each row in the object/csv
    # first element takes name and splits it into individual strings
    for row in reader:
        char_name = row[0]
        split_name = char_name.split()

        # identifies if character has 2 names or 3 (middle)
        num_of_names = len(split_name)

        # if character has 2 names, first and last are identified and then INSERTED into database
        if num_of_names == 2:
            full_name = f"{split_name[0]} {split_name[1]}"
            full_name_list = full_name.split()
            first = full_name_list[0]
            last = full_name_list[1]

            house = row[1]
            birth = row[2]

            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       first, None, last, house, birth)

        # if character has 3 names, first, middle, and last are identified and then INSERTED into database
        elif num_of_names == 3:
            full_name = f"{split_name[0]} {split_name[1]} {split_name[2]}"
            full_name_list = full_name.split()
            first = full_name_list[0]
            middle = full_name_list[1]
            last = full_name_list[2]

            house = row[1]
            birth = row[2]

            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       first, middle, last, house, birth)