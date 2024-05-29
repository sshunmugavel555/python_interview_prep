def add_numbers_both_lists(l1,l2):
    """ Add numbers from l1 to their corresponding numbers in l2 and create a list l3 """
    l3=[]
    if len(l1)==len(l2):
        l3=[l1[x]+l2[x] for x in range(len(l1))] #list comprehension
        # for x in range(len(l1)):
        #     l3.append(l1[x]+l2[x])
        print(l3)
    else:
        print(f"Unequal list lengths. Cannot be added ")
    

l1=[1,2,3,4,5,6]
l2=[43,22,3,2,11,100]

add_numbers_both_lists(l1,l2)