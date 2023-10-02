import numpy
import re
import unidecode
from app.CityDictionaryCreator import create_cities_file
from app.IataListCreator import create_iata_file

def levenshtein_distance(token1, token2):
    """
    Regresa la distancia entre dos palabras obtenida por el 
    algoritmo de Levenshtein. 

    Código obtenido de:
    Gad, A. F. (2021). Implementing The Levenshtein Distance 
    for Word Autocompletion and Autocorrection. Paperspace Blog. 
    https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
    """
    token1 = normalize_word(token1)
    token2 = normalize_word(token2)
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]

def normalize_word(name):
    name_string = str(name)

    new_name = unidecode.unidecode(name_string)
    new_name = re.sub("[^A-Z]", "", name_string, 0,re.IGNORECASE)
    new_name = new_name.upper()
    if (len(new_name) > 0):
        return new_name
    else:
        return name_string

def calculate_distance(my_location, max_dist_iata, max_dist_city, cities_weather, iatas_weather):
    """
    Calcula las distancias de Levenshtein entre la palabra 
    escogida y cada palabra de la lista de las palabras a comparar.
    Regresa un diccionario con subdiccionarios, donde cada uno 
    tiene palabras con la misma distancias resspecto a la pedida.

    Código basado en:
    Gad, A. F. (2021). Implementing The Levenshtein Distance 
    for Word Autocompletion and Autocorrection. Paperspace Blog. 
    https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
    """
    dict_distance = {}

    for iata in iatas_weather:
        location_distance = int(levenshtein_distance(my_location, iata))
        if (location_distance <= max_dist_iata):
            if not location_distance in dict_distance:
                dict_distance[location_distance] = []
#            dict_distance[location_distance].append(iata)
#            dict_distance[location_distance].append([iata, iatas_dict[iata]])
            dict_distance[location_distance].append(iatas_weather[iata])

    for city in cities_weather:
        location_distance = int(levenshtein_distance(my_location, city))
        if (location_distance <= max_dist_city):
            if not location_distance in dict_distance:
                dict_distance[location_distance] = []
#            dict_distance[location_distance].append(city)
#            dict_distance[location_distance].append([city, cities_dict[city]])
            dict_distance[location_distance].append(cities_weather[city])

    return dict_distance
        
def closest_word(level, max_distance, dict_distance):
    if(level <= max_distance):
        if level in dict_distance:
                return level[0]
        return closest_word(level+1, max_distance, dict_distance)
    return None

def city_search(my_location, cities_weather, iatas_weather):
    max_dist_iata = 1
    max_dist_city = 2
    max_distance = max(max_dist_city, max_dist_iata)
    dict_distance = calculate_distance(my_location, max_dist_iata, max_dist_city, cities_weather, iatas_weather)
    return closest_word(0, max_distance, dict_distance)