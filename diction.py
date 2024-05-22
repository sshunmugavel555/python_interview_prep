""" person={'name':'shankar',
        'age':41,
        'sex':'m',
        'city':'austin'}

print(person['city']) """

""" myDict={}

myDict['name']='shankar'
myDict['age']=41

print(myDict)
myDict['age']=45

print(myDict) """

""" print('before')
alien={'x_coord':1,
       'y_coord':5,
       'speed':'fast',
       'color':'red'}
print(alien)

if alien['speed']=='slow':
    delta=1
elif alien['speed']=='medium':
    delta=5
elif alien['speed']=='fast':
    delta=10
alien['x_coord']+=delta

print('after')
print(alien)

del alien['color']
print(alien) """

books_auth={'Great Exp':'Dickens',
            'Harry Potter':'jk rowling',
            'GoT':'George Martin',
            'Lord of Rings':'JRR Tolkien',
            'GoT':'George Martin',
            'GoT':'George Martin',
            }

""" print(books_auth.get('GoT','no such book found'))
print(books_auth.get('abc'))

print(books_auth) """

#for book,auth in books_auth.items():
 #   print(f"{book} is written by {auth}")
bookL=['GoT','Ponni Selvan','kadalpura','Lord of Rings']


for book in books_auth:
    if book in bookL:
        print(f"{book} is written by {books_auth[book]}")
    else:
        print(f"{book} not in my fav book list")

if 'Ponni Selvan' not in books_auth.keys():
    print(f"You will have to read this book Ponni Selvan")

for book,auth in sorted(books_auth.items()):
    print(f"{book} is written by {auth}")

for book in sorted(books_auth.keys()):
    print(f"{book} is written by {books_auth[book]}")

for authors in sorted(books_auth.values()):
    print(authors.title())




          