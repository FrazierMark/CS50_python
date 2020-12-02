import cs50
from cs50 import get_int

while True:
    n = get_int("Height: ")
    if (n > 0 and n <= 8):
        break

# for each row
for i in range(0, n):

    # print front spaces
    for s in range(n - 1 - i):
        print(" ", end="")

    # print front #
    for h in range(n - 1 - i, n):
        print("#", end="")

    # print 2 spaces
    print("  ", end="")

    # print end #
    for h in range(n - 1 - i, n):
        print("#", end="")
    # print new line
    print()