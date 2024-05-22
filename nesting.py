ppl0={'name':'shankar',
      'age':41,
      'sex':'m',}

ppl1={'name':'abee',
      'age':35,
      'sex':'f',}

ppl2={'name':'kin',
      'age':11,
      'sex':'m',}

ppl3={'name':'nik',
      'age':3,
      'sex':'m',}

family=[ppl0,ppl1,ppl2,ppl3]

print(family[2]['age'])


#Make Aliens at runtime
aliens=[]

for _ in range(30):
    alienDict={'color':'green',
               'points':5,
               'speed':'slow',}
    aliens.append(alienDict)

print(len(aliens))

for alien in aliens[:3]:
    alien['color']='yellow'
    alien['points']=10
    alien['speed']='medium'

for alien in aliens[:10]:
    print(alien)


#List in a Dict
pizza={'crust':'thin',
       'size':'medium',
       'toppings': ['mush','onions','jala'],
       }

print(f"You have ordered {pizza['crust']} pizza"
      "with the below toppings")

for eachTop in pizza['toppings']:
    print(eachTop.title())



#fav languages
favLang={'shan':['python'],
         'abee':['c','c#'],
         'kin':['python','java'],
         }

for k,v in favLang.items():
    if len(v)==1:
        print(f"{k.title()} likes the below language")
    else:
        print(f"{k.title()} likes the below languages")
    for eachL in v:
        print(eachL)
    print('\n')









