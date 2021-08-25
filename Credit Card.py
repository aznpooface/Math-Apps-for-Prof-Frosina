def main():
    while True:
        print("We only take Amex (34,37 len: 15), MasterCard (50 to 56 len:16), Visa (4 len: 16 or 13)")
        credit_card = input("Please Input your Card #: ")
        if credit_card.isnumeric() and len(credit_card) > 12 and len(credit_card)<17:
            break
        print("Credit Cards have 13 to 16 numbers")
    global card_length
    card_length = len(credit_card)
    first_two = int(credit_card[0:2])
    card_list = []
    for element in credit_card:  # Single Integers in list
        card_list.append(int(element))
    valid = luhn(card_list)  # Run Luhn Test
    if not valid:
        print("Did not Pass Luhn: Not Valid")
        return 1
    else:
        # Different Card Types
        if first_two == 34 or first_two == 37 and card_length == 15:
            print("AMEX")
        elif first_two > 50 and first_two < 56 and card_length == 16:
            print("Master Card")
        elif credit_card[0]=="4" and (card_length == 16 or card_length == 13):
            print("Visa")
        else:
            print("Unidentified")
        
def luhn(card):
    parity = card_length % 2
# Initialize Totals 
    odd_index_total = 0
    even_index_total = 0
    grand_total = 0
# Calculations here
    for num in card:
        if parity == 1:
            odd_index_total += num
            parity = 0
            # print("odd",num)
        else:
            doubled = num*2
            if doubled > 9:
                doubled = doubled%10 + 1  # It's 1 because it can never go to 20
            even_index_total += doubled
            # print("even", doubled)
            parity = 1
# Final Tally    
    grand_total += odd_index_total + even_index_total
    # print("even total", even_index_total)
    # print("odd total", odd_index_total)
    # print(grand_total)
    if grand_total % 10 == 0:
        return (True)  # Valid
    else:
        return (False)  # Invalid
    print(card)


main()
input("Press Enter to exit.")