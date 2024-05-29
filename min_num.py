def min_number_list(listOfNums):
    """ print the minimum number in a given list of numbers"""
    minNum=listOfNums[0]

    for num in listOfNums:
        if minNum > num:
            minNum = num


    print(minNum)

myList=[55,23,122,34,5,100,22]
min_number_list(myList)