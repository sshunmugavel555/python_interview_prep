"""" Car Module that has Classes defined very specific for a car usage 
Has the below Classes 
Car
"""

class Car:
    """ Model a Car class """
    def __init__(self,make,model,year) -> None:
        """ Car's Instance Vars defined """
        self.make=make
        self.model=model
        self.year=year
        self.odo_reading=0

    def desc_car(self) -> None:
        """ Describes the car's attribs """
        print(f"Car's make->{self.make}, model->{self.model}, year->{self.year}")

    def update_odometer(self,miles) -> None:
        """ Set/Update odometer reading """
        if miles >= self.odo_reading:
            self.odo_reading=miles
        else:
            print(f"Tampering/Lowering the mileage on the car is a punishable crime")

    def increment_miles(self,miles) -> None:
        """ Add miles to the current mileage of the car/odometer reading """
        if miles>0:
            self.odo_reading += miles
        else:
            print(f"Miles cannot be negative")

    def read_odometer(self) -> None:
        """ Calls out the odo reading """
        print(f"The current miles on the car is {self.odo_reading} miles")

    def fillGas(self) -> None:
        """ Simulate gas filling of the car """
        print(f"Fill gas at the gas station ")