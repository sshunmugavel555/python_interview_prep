def max_number_list(listOfNums):
    """ print the max number in a given list of numbers"""
    maxNum=listOfNums[0]

    for num in listOfNums:
        if maxNum < num:
            maxNum = num


    print(maxNum)

myList=[55,23,122,34,5,100,22]
max_number_list(myList)