from car import Car
from car_access import Electric_Car

myCar=Car('Honda','CRV',2004)
myCar.desc_car()
myCar.update_odometer(2500)
myCar.read_odometer()
myCar.update_odometer(25001)
myCar.read_odometer()
myCar.increment_miles(555)
myCar.read_odometer()

myEV=Electric_Car('Tesla','Model X','2024')
myEV.desc_car()
myEV.battery_life.desc_battery()
myEV.fillGas()
myEV.battery_life.get_range()
myEV.battery_life.upgrade_battery()
myEV.battery_life.get_range()