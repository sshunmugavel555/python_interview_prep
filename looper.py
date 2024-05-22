""" fruits=['apple','banana','strawberry','guava','oranges']

for eachF in fruits:
    print(f"My Fav fruit is {eachF.title()}")
print('*******************************')

myL=[]
for x in range(1,10):
    myL.append(x)

print(myL)

oddL=list(range(1,11,2))
evenL=list(range(2,11,2))
print(oddL)
print(evenL)

#first 10 square numbers
cubL=[]
for x in range(1,11):
    cubL.append(x**3)

print(cubL)

#Using list comprehensions
sqL=[ x**2 for x in range(1,11)]
print(sqL) """


""" milL=list(range(1,1000001))
print(min(milL))
print(max(milL))
print(sum(milL))

oddN=list(range(1,21,2))
print(oddN)

mul3=list(range(3,31,3))
print(mul3) """

""" laptops=['dell','apple','hpe','ibm','toshiba']
lapCopy=laptops
lapCopy.append('abc') """
#laptops.pop()

""" print(laptops)
print(lapCopy) """
""" for laptop in laptops[-3:]:
    print(laptop) """

coord=(5,10)
#coord[0]=55

coord=(55,100)
for eachC in coord:
    print(eachC)


singT=(3,)



