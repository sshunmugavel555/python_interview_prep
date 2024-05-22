class Dog:
    """ Dog class that handles attributes and actions performed by any dog """
    def __init__(self,name,breed) -> None:
        """ initialize a dog class's instance vars """
        self.name=name
        self.breed=breed

    def sit(self):
        """ simulate a dog sit """
        print(f"{self.name} is sitting now")

    def wagTail(self):
        """ simulate a dog wag tail """
        print(f"{self.name} is wagging its tail now")

    def bark(self):
        """ simulate a dog bark """
        print(f"I am a {self.breed} bow wow. My name is {self.name} bow wow !!")

myDog = Dog('Jimmy','pomeranian')
print(myDog.name)
print(myDog.breed)
myDog.sit()
myDog.bark()
myDog.wagTail()

dog1=Dog('tommy','German Shep')
dog2=Dog('Julie','Alsation')

dog1.bark()
dog2.bark()



    