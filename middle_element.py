def echo_mid_elem(listOfNums):
    """ Print the middle element in a list of numbers """
    if len(listOfNums) % 2 != 0:
        pos=len(listOfNums)//2
        print(listOfNums[pos])
    else:
        print("Even number of elements in list. So, no mid element ")


myList=[1,2,3,4,5,6,7]
echo_mid_elem(myList)