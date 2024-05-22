""" alien_color='abc'

if alien_color == 'green':
    score=5
elif alien_color == 'yellow':
    score=10
elif alien_color == 'red':
    score=15
else:
    score=25

print(score) """

""" req_toppings=['cheese','mushrooms','sausage','anchovies']
avbl_toppings=['cheese','mushrooms','peppers','onions','spinach','chicken','pepporoni']

for eachR in req_toppings:
    if eachR in avbl_toppings:
        print(f"Adding {eachR} to the pizza now!")
    else:
        print(f"Sorry we ran out of {eachR}")

print(f"We made your customised pizza!") """

""" userNames=[]
if userNames:
    for eachUser in userNames:
        if eachUser == 'admin':
            print(f"Hello! {eachUser}, Welcome to the club!! Wanna see a Status Report")
        else:
            print(f"Hello! {eachUser}, Welcome to the club!!")
else:
    print(f"We need some users to begin with!") """

""" currUsers=['shan','abee','nik','kin','yoyo','admin']
newUsers=['abc','def','xyz','nik','ABEE','zzz']

print(f"Administering Userids now---")
for eachN in newUsers:
    if eachN.lower() in currUsers:
        print(f"Your userid {eachN} is already taken. Please choose a new one!!")
    else:
        print(f"{eachN} userid is avbl") """

ordL=list(range(1,10))
for eachN in ordL:
    if eachN==1:
        print(f"{eachN}st")
    elif eachN==2:
        print(f"{eachN}nd")
    elif eachN==3:
        print(f"{eachN}rd")
    else:
        print(f"{eachN}th")
    print("\n")
    
          

