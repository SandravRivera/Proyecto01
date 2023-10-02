from levenshtein import city_search

print()
print('IATA DICT ##########')
iata_dict = {
    "MTY":"clima_Monterrey",
    "AGU":"clima_Aguascalientes",
    "AMS":"clima_Ámsterdam",
    "GDL":"clima_Guadalajara",
    "PHX":"clima_Phoenix"
    }
print(iata_dict)

print()

print('CITY DICT ##########')
city_dict = {
    "Monterrey":"clima_Monterrey",
    "Aguascalientes":"clima_Aguascalientes",
    "Ámsterdam":"clima_Ámsterdam",
    "Guadalajara":"clima_Guadalajara",
    "Phoenix":"clima_Phoenix"
    }
print(city_dict)

print()

print('SEARCH ##########')
location1 = "motereey"
print(location1, " search: ", city_search(location1, city_dict, iata_dict))
location2 = "agu"
print(location2, " search: ", city_search(location2, city_dict, iata_dict))
location3 = "xalapa"
print(location3, " search: ", city_search(location3, city_dict, iata_dict))
location4 = "MTZ"
print(location4, " search: ", city_search(location4, city_dict, iata_dict))
print()