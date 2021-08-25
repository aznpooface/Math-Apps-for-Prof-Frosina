list1 = [1,2,5,6,6,6,1,2,3,4,4,4]
list2 = []
list3 = [1,1,1,3,3,3,2,2,2,4,4,4]

def get_mode(listy):
    popular_list = []
    highest_counter = 0
    for num in listy:
        counter = 0
        for num2 in listy:
            if num == num2:
                counter +=1
        if counter > highest_counter:
            highest_counter = counter
            popular_list = [num]
        if counter == highest_counter and num not in popular_list:
            popular_list.append(num)
    print("modes are: ", popular_list)
    

get_mode(list3)

input("Press Enter to Exit")