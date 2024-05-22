class Restaurant:
    """ Model a Restaurant class """
    def __init__(self,name,cuisine) -> None:
        """ Instance Vars for the restaurant class """
        self.name=name
        self.cuisine=cuisine
        self.number_served=0

    def desc_restaurant(self) -> None:
        """ Describes the current restaurant obj """
        print(f"Welcome to {self.name}")
        print(f"We serve cuisine {self.cuisine}")

    def open_restaurant(self) -> None:
        """ Calls out if the restaurant is closed/open """
        print(f"We are open for dining. We take reservations/walk-ins")

    def set_number_served(self,custCnt) -> None:
        """ Setter method to set the number of customers served by the restaurant """
        if custCnt >= self.number_served:
            self.number_served=custCnt
        else:
            print(f"You cannot roll back on the cust count.")

    def incr_num_served(self,custCnt) -> None:
        """ Increment the customer served counter using user inputs """
        if custCnt > 0:
            self.number_served += custCnt
        else:
            print(f"You cannot roll back on the cust count / negative values prohibited ")

    def show_cust_cnt(self) -> None:
        """ Calls out the total number of customer served so far """
        print(f"Total number of customers served till date - {self.number_served}")


class IceCreamStand(Restaurant):
    """ Ice Cream Stand class that models/inherits from a Restaurant """
    def __init__(self,name,cuisine) -> None:
        """ Init flavors for an ice cream stand """
        super().__init__(name,cuisine)
        self.flavors=['vanilla','coffee','mango','tart']
    
    def show_flavors(self) -> None:
        """ Call out all the flavors in the ice cream stand """
        print('We have the below flavors avbl')
        for eachFlavor in self.flavors:
            print(f"{eachFlavor}")

myIce=IceCreamStand('Arun Ice Cream','Ice Creams')
myIce.show_flavors()



# myRest=Restaurant('Saravana Bavan','South Indian Veg')
# print(myRest.name)
# print(myRest.cuisine)
# print(myRest.number_served)

# myRest.desc_restaurant()
# myRest.open_restaurant()

# myRest.set_number_served(55)
# myRest.show_cust_cnt()
# myRest.set_number_served(550)
# myRest.show_cust_cnt()
# myRest.incr_num_served(55)
# myRest.show_cust_cnt()

