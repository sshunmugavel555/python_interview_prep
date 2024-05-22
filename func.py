def sayHello(user):
    """ Function says Hello"""
    print(f"Hello {user.title()}!")

user='Shankar'
sayHello(user)

def myPet(petBreed,petName):
    """ Welcome my Pet - Pass Breed and Name of your Pet """

    print(f"I am a {petBreed.title()}")
    print(f"My name is {petName.title()}")


#myPet(petName='Mitra',petBreed='poodle')
#myPet('doggie')

def makeShirt(size='large',text='I love Python'):
    """ Make a Tee shirt of a given size and text written over it"""
    print(f"Making the below Tee")
    print(f"Size {size} and text {text}")

makeShirt()
makeShirt('medium')
makeShirt('small','I love C#')

def sayFullName(fn,ln,mn=''):
    """ Compute a full name from the first,last and middle names and return the full name """
    if mn:
        return fn.title()+' '+mn.title()+' '+ln.title()
    else:
        return fn.title()+' '+ln.title()
    

while True:
    fn=input("Enter your first name / Q to quit ")
    ln=input("Enter your last name / Q to quit ")
    if fn=='Q' or ln=='Q':
        break
    else:
        fullName=sayFullName(fn,ln)
        print(fullName)








print(sayFullName('shankar','shunmugavel','s'))
print(sayFullName('abee','tan'))

#Return a Dict
def retNameDict(fn,ln,mn=None):
    """ Compute a full name dict from the first,last and middle names and return the full name dict"""
    fnDict={}
    fnDict['fn']=fn
    fnDict['mn']=mn
    fnDict['ln']=ln
    return fnDict

d=retNameDict('shankar','shunmugavel')

for k,v in d.items():
    print(f"{k} --> {v}")


    




