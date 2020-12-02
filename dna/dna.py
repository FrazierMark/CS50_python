import cs50
import sys
import csv
import re
import itertools


def get_consecutive_str(substring):
    """Returns dict with STR and # of times str is repeated."""
    pattern = "(?=((" + re.escape(substring) + ")+))"
    matches = re.findall(pattern, dna_string)

    # if there are matches to pattern found, calculate longest consecutive repeats of pattern
    if matches:
        consecutive_reps = max(len(m[0]) // len(substring) for m in matches)
    # if no matches found, make reps 0
    else:
        consecutive_reps = 0
    # create a dictionary with strs as the key, and repeats as the value
    str_repeats = {'str': substring, 'repeats': consecutive_reps}
    return str_repeats


if len(sys.argv) != 3:
    print(f"Usage: python dna.py data.csv sequence.txt")
    exit(1)


with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)          # pass it the file object as an argument to create a reader object associate with the file 'filename'
    header_row = next(reader)       # creates a list called header_row with each item in the header

    # save profiles in a dictionary w/ the strs as a value/list
    my_dict = {}
    key_names = []
    str_list = []
    for row in reader:
        key_name = row[0]
        key_names.append(key_name)
        strs = row[1:]
        int_strs = list(map(int, strs))     # converting string to ints
        str_list.append(int_strs)           # adds ints to list

    my_dict = dict(zip(key_names, str_list))    # adds key_names list to dic as keys, adds str_list to dic as values

with open(sys.argv[2], 'r') as dna:         # opens the dna txt files and saves it in a list
    reader = csv.reader(dna)
    dna_seq = []
    for row in reader:
        dna = row[:]
        dna_seq.append(dna)

    for i in range(len(dna)):
        dna[i] = dna[i].lower()

    dna_string = ""
    for ele in dna:
        dna_string += ele

# if using the large csv file do the folowing
if sys.argv[1] == "databases/large.csv":

    agatc = get_consecutive_str('agatc')
    ttttttct = get_consecutive_str('ttttttct')
    aatg = get_consecutive_str('aatg')
    tctag = get_consecutive_str('tctag')
    gata = get_consecutive_str('gata')
    tatc = get_consecutive_str('tatc')
    gaaa = get_consecutive_str('gaaa')
    tctg = get_consecutive_str('tctg')

    anon_profile_long = {'repeats': [agatc.get('repeats'), ttttttct.get('repeats'), aatg.get('repeats'),
                                     tctag.get('repeats'), gata.get('repeats'), tatc.get('repeats'),
                                     gaaa.get('repeats'), tctg.get('repeats')]}

    # compare dictionaries to look for match, use .key() method to print name if there is a match
    if anon_profile_long.get('repeats') == my_dict.get('Albus'):
        print(f"Albus")
    elif anon_profile_long.get('repeats') == my_dict.get('Cedric'):
        print(f"Cedric")
    elif anon_profile_long.get('repeats') == my_dict.get('Draco'):
        print(f"Draco")
    elif anon_profile_long.get('repeats') == my_dict.get('Fred'):
        print(f"Fred")
    elif anon_profile_long.get('repeats') == my_dict.get('Ginny'):
        print(f"Ginny")
    elif anon_profile_long.get('repeats') == my_dict.get('Hagrid'):
        print(f"Hagrid")
    elif anon_profile_long.get('repeats') == my_dict.get('Harry'):
        print(f"Harry")
    elif anon_profile_long.get('repeats') == my_dict.get('Hermione'):
        print(f"Hermione")
    elif anon_profile_long.get('repeats') == my_dict.get('James'):
        print(f"James")
    elif anon_profile_long.get('repeats') == my_dict.get('Kingsley'):
        print(f"Kingsley")
    elif anon_profile_long.get('repeats') == my_dict.get('Lavender'):
        print(f"Lavender")
    elif anon_profile_long.get('repeats') == my_dict.get('Lily'):
        print(f"Lily")
    elif anon_profile_long.get('repeats') == my_dict.get('Lucius'):
        print(f"Lucius")
    elif anon_profile_long.get('repeats') == my_dict.get('Luna'):
        print(f"Luna")
    elif anon_profile_long.get('repeats') == my_dict.get('Minerva'):
        print(f"Minerva")
    elif anon_profile_long.get('repeats') == my_dict.get('Neville'):
        print(f"Neville")
    elif anon_profile_long.get('repeats') == my_dict.get('Petunia'):
        print(f"Petunia")
    elif anon_profile_long.get('repeats') == my_dict.get('Remus'):
        print(f"Remus")
    elif anon_profile_long.get('repeats') == my_dict.get('Ron'):
        print(f"Ron")
    elif anon_profile_long.get('repeats') == my_dict.get('Severus'):
        print(f"Severus")
    elif anon_profile_long.get('repeats') == my_dict.get('Sirius'):
        print(f"Sirius")
    elif anon_profile_long.get('repeats') == my_dict.get('Vernon'):
        print(f"Vernon")
    elif anon_profile_long.get('repeats') == my_dict.get('Zacharias'):
        print(f"Zacharias")
    else:
        print(f"No match")


# if using the small csv file do the folling
elif sys.argv[1] == "databases/small.csv":
    agatc = get_consecutive_str('agatc')
    aatg = get_consecutive_str('aatg')
    tatc = get_consecutive_str('tatc')

    anon_profile_short = {'repeats': [agatc.get('repeats'), aatg.get('repeats'), tatc.get('repeats')]}

# compare dictionaries to look for match, use .key() method to print name if there is a match

    if anon_profile_short.get('repeats') == my_dict.get('Alice'):
        print(f"Alice")
    elif anon_profile_short.get('repeats') == my_dict.get('Bob'):
        print(f"Bob")
    elif anon_profile_short.get('repeats') == my_dict.get('Charlie'):
        print(f"Charlie!")
    else:
        print(f"No match")