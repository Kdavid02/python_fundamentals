# 11-1 (city_functions.py is called for exercise14.py)
# 11-2 modify the functions, so it uses a 3rd parameter. it should fail. then make it so it is optional.
# write a second test called test_city_country_population()
# that calls your function with the values 'santiago' 'chile' and population=5000000
def cit_country(city, country, populations=0):
    return f"{city}, {country}"

    city_text = f"{city.title()}, {country.title}"
    if population:
        city_text += f" population {population}"
    return city_text
