"""" Car Accessories Module that has Classes defined very specific for a car usage 
Has the below Classes 
Electric_Car
Battery """

from car import Car

class Electric_Car(Car):
    """ An Electric Car Class inherited/modeled out of a parent Car Class """
    def __init__(self, make, model, year) -> None:
        """ Initialize attributes of a the child class """
        super().__init__(make, model, year)
        self.battery_life=Battery()
    
    def fillGas(self) -> None:
        """ Method over-ride in child class """
        print(f"Electric Car does not have a gas tank you fool !!")

class Battery:
    """ Model a Battery as a class - Used in Electric vehicles """
    def __init__(self,battery_life=40) -> None:
        self.battery_life=battery_life
    
    def desc_battery(self) -> None:
        """ Calls out life of the battery """
        print(f"Battery life is -> {self.battery_life} kwh")

    def upgrade_battery(self) -> None:
        """ Simulate Battery Upgrade """
        if self.battery_life <65 :
            self.battery_life=65


    def get_range(self) -> None:
        """ Get the range in miles the electric car can cover """
        if self.battery_life==20:
            print(f"You can only go 100 miles with one full charge")
        elif self.battery_life==40:
            print(f"You can only go 200 miles with one full charge")
        elif self.battery_life > 40:
            print(f"You can anywhere you want. Dont bother abt mileage")