from cs50 import get_string

# prompt user for text using get_string
text = get_string("Text: ").strip()

# initialize variables
num_letters = 0
num_words = 0
num_sentences = 0

# move through string
for i in range(len(text)):

    # if letter is part of alphabet, increase letter counter
    if text[i].isalpha():
        num_letters += 1

    if (i == 0 and text[i] != ' ') or (i != len(text) - 1 and text[i] == ' ' and text[i + 1] != ' '):
        num_words += 1

    # if any of the following appear: " . ? !, increase the sentence counter
    if text[i] == '.' or text[i] == '?' or text[i] == '!':
        num_sentences += 1

L = num_letters / num_words * 100
S = num_sentences / num_words * 100

# compute Coleman-Liau index
# need to round, cause of integer (grade level)

index = round(0.0588 * L - 0.296 * S - 15.8)
if (index < 1):
    print(f"Before Grade 1")
elif (index >= 16):
    print(f"Grade 16+")
else:
    print(f"Grade {index}")

