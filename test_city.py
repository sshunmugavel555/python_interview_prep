from city import say_city_country

def test_by_giving_city_country_combo():
    """ Test the function by providing both city and country strings """
    combo=say_city_country('santiago','chile')
    assert combo=='Santiago, Chile'

def test_by_giving_city_country_popu_combo():
    """ Test the function by providing both city,country and popu strings """
    combo=say_city_country('santiago','chile',50000000)
    assert combo=='Santiago, Chile - population 50000000'