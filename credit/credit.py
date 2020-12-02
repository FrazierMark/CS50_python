from cs50 import get_int


while True:
    # prompt user for credit card number
    cc = get_int("Number: ")
    if (cc <= 0):
        continue

    sum_of_n1 = 0
    sum_of_n2_products = 0

    cc_num_test_1 = cc
    cc_num_test_2 = cc

    # calculate checksum
    while cc_num_test_1 > 0:
        # get last num in cc
        n1 = cc_num_test_1 % 10

        # add last num in cc
        sum_of_n1 += n1

        # subtract last num in counter
        cc_num_test_1 -= n1

        # subtract last num from cc sequence
        cc_num_test_1 //= 10

        # isolates last digi and set n2
        n2 = cc_num_test_1 % 10

        # if digit is more than 9 when multiplied, add digits individually
        if (n2 * 2) > 9:
            n2_t2 = n2 * 2
            sum_of_n2_products += n2_t2 % 10
            sum_of_n2_products += n2_t2 // 10

        # else multiplydigit by 2 then add the sum of 2 products
        else:
            sum_of_n2_products += (n2 * 2)

        cc_num_test_1 -= n2
        cc_num_test_1 //= 10

    # distinguish cc company
    # validate number's length
    if (sum_of_n1 + sum_of_n2_products) % 10 == 0:

        if cc_num_test_2 >= 340000000000000 and cc_num_test_2 < 350000000000000 or cc_num_test_2 >= 370000000000000 and cc_num_test_2 < 380000000000000:
            print(f"AMEX")

        elif cc_num_test_2 >= 5100000000000000 and cc_num_test_2 < 5600000000000000:
            print(f"MASTERCARD")

        elif cc_num_test_2 >= 4000000000000 and cc_num_test_2 < 5000000000000 or cc_num_test_2 >= 4000000000000000 and cc_num_test_2 < 5000000000000000:
            print(f"VISA")

        elif cc_num_test_2 <= 3999999999999 or cc_num_test_2 >= 5600000000000000 or cc_num_test_2 >= 350000000000000 and cc_num_test_2 < 369999999999999:
            print(f"INVALID")

    else:
        print(f"INVALID")
    break