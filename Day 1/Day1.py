def main():
    # initialize lists
    list1 = []
    list2 = []

    filename = "input.txt"

    # read input from text file
    with open(filename) as file:
        # iterate line by line
        for line in file:
            # get the numbers for the row
            num1, num2 = line.rstrip().split("   ")
            num1, num2 = int(num1), int(num2)

            # initialize index to insert the number at
            i_insert_num1 = None
            i_insert_num2 = None

            # find the index to insert the number into the list sorted
            for i in range(len(list1)):
                # if the number in this position is greater than the num1
                # update the index to insert it before this number
                if i_insert_num1 == None and list1[i] >= num1:
                    i_insert_num1 = i
                if i_insert_num2 == None and list2[i] >= num2:
                    i_insert_num2 = i

            # if it's the largest number, append to the end, othewise insert 
            if i_insert_num1 is None:
                list1.append(num1)
            else:
                list1.insert(i_insert_num1, num1)

            if i_insert_num2 is None:
                list2.append(num2)
            else:
                list2.insert(i_insert_num2, num2)

    print("Total Distance: ", _get_total_distance(list1, list2))


def _get_total_distance(list1, list2):
    total = 0
    for num_list_1, num_list_2 in zip(list1, list2):
        total += abs(num_list_1 - num_list_2)
    return total


if __name__ == "__main__":
    main()
