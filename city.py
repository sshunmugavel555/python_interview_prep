def say_city_country(city,country,population=''):
    """ Call out the whole city country & population combo string """
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
