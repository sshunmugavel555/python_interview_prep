def make_pizza(size,*toppings):
    
    print(f"Making pizza now of size {size} with the below toppings ")
    for top in toppings:
        print(f"{top}")
    print('\n')


def makeSandwich(*args):
    """ Make a sandwich from arbitrary toppings """
    print(f"Making the below sandwich")
    for arg in args:
        print(f"\t {arg}")
    print('\n')


