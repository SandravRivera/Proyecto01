from levenshtein import city_search
from iataCities import iata_cities

####### VER SI IMPORTA LAS CIUDADES Y SU IATA #######
print()
print('IATA CITIES ##########')
print(iata_cities)

####### VER SI FUNCIONA LA BUSQUEDA POR LEVENSHTEIN #######
print()
print('IATA DICT ##########')
iata_dict = {
    "MTY":"clima_Monterrey",
    "AGU":"clima_Aguascalientes",
    "AMS":"clima_Ámsterdam",
    "GDL":"clima_Guadalajara",
    "PHX":"clima_Phoenix",
    'TLC':'clima_Toluca',
    'TRC':'clima_Coahuila'
    }
print(iata_dict)

print()

print('CITY DICT ##########')
city_dict = {
    "Monterrey":"clima_Monterrey",
    "Aguascalientes":"clima_Aguascalientes",
    "Ámsterdam":"clima_Ámsterdam",
    "Guadalajara":"clima_Guadalajara",
    "Phoenix":"clima_Phoenix",
    'Toluca':'clima_Toluca',
    'Coahuila':'clima_Coahuila'
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
location5 = "TMC"  ##### Da preferencia TLC sobre TRC por orden en el diccionario
print(location5, " search: ", city_search(location5, city_dict, iata_dict))
location6 = "1#@%#^$"
print(location6, " search: ", city_search(location6, city_dict, iata_dict))
location7 = "A,g,u,a,sc@a.l#i^e&n*tes"
print(location7, " search: ", city_search(location7, city_dict, iata_dict))