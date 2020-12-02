from cs50 import get_float

while True:
    c = get_float("Change owed: ")
    if (c < 0):
        continue
    
    cents = round(c * 100)
    coins = 0
    
    # when cents are more that 25, subtract 25 cents then increase coin count by 1
    while cents >= 25:
        cents = cents - 25
        coins += 1

    # when cents are more that 10, subtract 25 cents then increase coin count by 1    
    while cents >= 10:
        cents = cents - 10
        coins += 1

    # when cents are more that 5, subtract 25 cents then increase coin count by 1        
    while cents >= 5:
        cents = cents - 5
        coins += 1

    # when cents are more that 1, subtract 25 cents then increase coin count by 1
    while cents >= 1:
        cents = cents - 1
        coins += 1
        
    # print final coin amount
    print(f"{coins}")
    break