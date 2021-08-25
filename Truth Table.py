# To use this just change the number on line 39 to your desired size


def dec_to_bin(num, places = 0):
# 0 places means it will not add additional places.
    quotient = num
    remainder = ""
    # Magic happens here
    while quotient > 0:
        remainder += str(quotient % 2)
        quotient = quotient // 2
    while len(remainder) < places: # Gives Desired Digits
        remainder += "0"
    remainder = remainder[::-1] # Reverses
    return remainder


def make_truth_table(term):
    big_list = []
    # For printing headers
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = []
    for letter_count in range(term):
        x.append(alphabet[letter_count])
    big_list.append(x)
    print(x)
    # For printing headers
    array_count = 2**term
    for num in range(array_count):
        x = []
        bin_num = dec_to_bin(num, term)
        for i in bin_num:
            x.append(int(i))
        big_list.append(x)
        print(x)
    # currently this function just prints.
    return big_list

terms = int(input("How many terms do you want? (Type in only a positive integer): "))
make_truth_table(terms)
input("Press enter to exit")
