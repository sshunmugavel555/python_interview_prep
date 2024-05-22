""" def make_pizza(size,*toppings):
    
    print(f"Making pizza now of size {size} with the below toppings ")
    for top in toppings:
        print(f"{top}")
    print('\n')


make_pizza('cheese')
make_pizza('small','onion','chicken','ham') """

# def build_profile(**user_info):
#     """ Build user profile using arbitrary values - k v pairs"""
#     #user_info['first name']=fn
#     #user_info['last name']=ln

#     return user_info

# userProfile=build_profile(fn='Shan',ln='Shunmu',age=42,sex='male')

# print(userProfile)




def make_car(make,model,**kwargs):
    """ Making a car with arbitrary keyword args """
    kwargs['make']=make
    kwargs['model']=model

    return kwargs

carDict=make_car('subaru','outback',color='red',miles=12345)
print(carDict)