""" x=1
while x<=10:
    print(x)
    x+=1

flg=True
while flg:
    age = input(f"Enter your age - enter Q to quit ")
    if age == 'Q':
        flg=False
    else:
        if int(age)<30:
            print(f"No mid life crisis - not yet")
        else:
            print(f"mid life crisis - enjoy !!") """


""" x=0
while x<20:
    x+=1
    if x%2 == 1:
        print(x) """

""" flg=True
while flg:
    age=input("Enter your age pls | enter Q to quit ")
    if age == 'Q':
        break
    else:
        if int(age)<3:
            fee=0
        elif int(age)<12:
            fee=10
        elif int(age)>12:
            fee=15
        print(f"Your ticket price is {fee}") """

    
""" unconfirm=['Shan','Abee','Nik','Kin']
confirm=[]

while unconfirm:
    unc=unconfirm.pop()
    print(f"Confirming {unc} now")
    confirm.append(unc)

print(unconfirm)
print(confirm) """

#Remove all instances of def from a list

""" myList=['abc','def','ghi','def','xyz','def']
while 'def' in myList:
    myList.remove('def')

print(myList) """

""" poll={}
flg=True

while flg:
    name=input(f"what is your name / Q to quit  ")
    vote=input(f"Which party do you vote for / Q to quit ")

    if name=='Q' or vote=='Q':
        flg=False
    else:
        poll[name]=vote

for k,v in poll.items():
    print(f"{k} votes for {v} ") """

subOrders=['chick','ham','turkey','veggie','ham','ham']
finOrders=[]

print(f"We have run out of HAMS as of now")
while 'ham' in subOrders:
    subOrders.remove('ham')
    
while subOrders:
    curOrder=subOrders.pop()
    print(f"Making {curOrder} sub now!")
    finOrders.append(curOrder)

print(f"The below subs were made")
for eS in finOrders:
    print(eS)



