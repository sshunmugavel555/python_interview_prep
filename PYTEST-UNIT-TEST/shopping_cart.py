from typing import List

class ShoppingCart:
    """ Class that models a shopping cart """
    def __init__(self,max_size:int) -> None:
        self.items = []
        self.max_size = max_size

    def add(self,item: str):
        if self.size() < self.max_size:
            self.items.append(item)
        else:
            raise OverflowError("You are adding more than the capacity of the cart!")

    def size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        total_price=0
        for eItem in self.items:
            total_price += price_map.getty(eItem)
        return total_price

