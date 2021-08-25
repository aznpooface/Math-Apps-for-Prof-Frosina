# Convert base 10           &&      Convert to base 10
# float/int to string               string to float
# truncates right of point          rounds right of point

# The difference between truncating and rounding will lead to errors if both
# functions are used. Can mitigate problem by increasing placements.
# Only goes from base 2 to base 16.

# For anybody literate in python, this is an incredibly useless module. There's built in
# functions for the popular Math module.

def convert_base_10(dec_num, base=2, points=6):
    # Truncates point values. Does not do numbers past base 16.
    # Returns String
    # I could possibly create a function to make a dictionary past 16
    if type(dec_num) is not int and type(dec_num) is not float and\
            type(dec_num) is not float:
        return ("Error: Give me an int, float, or long for the decimal number")
    if type(base) is not int:
        return ("Error: Give me an integer 2 to 16 inclusive for base")
    if base < 1 or base > 16:
        return ("Error: Give me an integer 2 to 16 inclusive for base")

    hexd_alpha = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    # dictionary to convert num to hexd char
    dec_num_int = int(dec_num)  # Left of point
    dec_num_float = dec_num - dec_num_int  # Right of point
    converted_int = ""  # string for left of point
    converted_float = ""  # string for right of point
    point_count = 0  # Initializer for decimal points

    while dec_num_int != 0:  # convert left of point
        remainder = dec_num_int % base
        if remainder > 9:  # for Hex
            remainder = hexd_alpha[remainder]
        converted_int += str(remainder)
        dec_num_int = dec_num_int // base

    while point_count != points:  # convert right of point
        point_count += 1
        dec_num_float *= base
        if dec_num_float >= 1:
            point_num_int = int(dec_num_float)
            dec_num_float -= point_num_int
            if point_num_int > 9:  # for Hex
                point_num_int = hexd_alpha[point_num_int]
            converted_float += str(point_num_int)
        else:
            converted_float += str(0)

    converted_int = converted_int[::-1] + str(".")  # Reverse a string; add "."
    full_number = converted_int + converted_float  # left and right in one
    return full_number  # This is a string because of base 11 - 16


def convert_to_10(number_string, base=2, point=6):
    # Rounds the final number. Returns Float.
    if type(number_string) != str:
        return ("Input: (type = String) (char = 0-9, ., A-F, a-f)")
    power_left = 0
    power_right = 1
    total = 0
    hexd = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    if "." in number_string:
        split_number = number_string.split(".")
        left_number = split_number[0]
        right_number = split_number[1]
    else:
        left_number = number_string
        right_number = ""

    for num in left_number:  # Adds Left to total
        if left_number[-1].upper() in hexd:  # If hex, dec equiv = constant
            constant = hexd[left_number[-1].upper()]
        else:
            constant = int(left_number[-1])
        total += base ** power_left * constant
        left_number = left_number[:-1]
        power_left += 1  # Increase power to match placement

    for num in right_number:  # Adds Right to total
        if right_number[0].upper() in hexd:  # If hex, convert
            constant = hexd[right_number[0].upper()]
        else:
            constant = int(right_number[0])  # If not, don't.
        total += 1 / (base ** power_right) * constant
        right_number = right_number[1:]
        power_right += 1

    return (total)

while True:
    which = input("Are you converting to base 10?(y/n): " )
    if ("y" in which.lower()):
        base = int(input("Which base convert from? (eg. 1 for unary, 2 for binary ... 16 for hexd): "))
        if base > 16:
            print("Error, base higher than 16")
            input("press return to exit")
            break
        elif base < 1:
            print("Error, cannot go lower than 1")
            input("press return to exit")
            break
        num = input("What number? (eg. F2134F for hexd): ")
        places = int(input("How many decimal places?: "))
        print(convert_to_10(num, base, places))
        input("press return to exit")
        break
    elif ("n" in which.lower()):
        base = int(input("Which base convert to? (eg. 2 for binary ... 16 for hexd): "))
        num = float(input("What decimal number? (eg. 123.523):  "))
        places = int(input("How many decimal places?: "))
        print(convert_base_10(num, base, places))
        input("press return to exit")
        break 