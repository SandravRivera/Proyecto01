import numpy
import re
import unidecode

def levenshtein_distance(word1: str, word2: str):
    """Returns the Levenshtein distance between two words. 
    The difference is case insensitive and just works in letters.
    
    Code obtained from:
    Gad, A. F. (2021). Implementing The Levenshtein Distance 
    for Word Autocompletion and Autocorrection. Paperspace Blog. 
    https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
    
    Args:
        word1 (str): the first word to compare.
        word2 (str): the second word to compare.

    Returns:
        float: the Levenshtein distance between word1 and word2.
    """
    word1 = normalize_word(word1)
    word2 = normalize_word(word2)
    distances = numpy.zeros((len(word1) + 1, len(word2) + 1))

    for t1 in range(len(word1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(word2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(word1) + 1):
        for t2 in range(1, len(word2) + 1):
            if (word1[t1-1] == word2[t2-1]):
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

    return distances[len(word1)][len(word2)]

def normalize_word(original_word: str):
    """Converts to uppercase and deletes characters that are 
    not alphabetical in a string.

    Args:
        original_word (str): the word before normalize it.

    Returns:
        string: the word after normalize it.
    """

    normalized_word = unidecode.unidecode(original_word)
    normalized_word = re.sub("[^A-Z]", "", original_word, 0,re.IGNORECASE)
    normalized_word = normalized_word.upper()
    if (len(normalized_word) > 0):
        return normalized_word
    else:
        return original_word

def calculate_distance(my_location: str, max_dist_iata: int, max_dist_city: int, cities_weather: dict, iatas_weather: dict):
    """Calculates the Levenshtein distances between the word
    chosen and each element from the group of words to compare.
    Returns a dictionary with subdictionaries, where each
    subdictionary has the words with the same distance.
    It has words with the same distances from the request.

    Code based on:
    Gad, A. F. (2021). Implementing The Levenshtein Distance 
    for Word Autocompletion and Autocorrection. Paperspace Blog. 
    https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
    
    Args:
        my_location (str): the word chosen to compare.
        max_dist_iata (int): the maximum distance permited with IATA codes.
        max_dist_city (int): the maximum distance permited with cities names.
        cities_weather (dict): Cities and their weathers.
        iatas_weather (dict): IATA codes and their weathers.

    Returns:
        dict: the IATA codes and cities grouped in permited distances.
    """
    dict_distance = {}

    for iata in iatas_weather:
        location_distance = int(levenshtein_distance(my_location, iata))
        if (location_distance <= max_dist_iata):
            if not location_distance in dict_distance:
                dict_distance[location_distance] = []
            dict_distance[location_distance].append(iatas_weather[iata])

    for city in cities_weather:
        location_distance = int(levenshtein_distance(my_location, city))
        if (location_distance <= max_dist_city):
            if not location_distance in dict_distance:
                dict_distance[location_distance] = []
            dict_distance[location_distance].append(cities_weather[city])

    return dict_distance
        
def closest_word(level: int, max_distance: int, dict_distance: dict):
    """Return the first string with the smallest distance (key) associated.

    Args:
        level (int): the current distance.
        max_distance (int): the maximum distance possible.
        dict_distance (dict): distances associated with a list of words.

    Returns:
        str: the first string with the smallest distance.
    """
    if(level <= max_distance):
        if level in dict_distance:
                return dict_distance[level][0]
        return closest_word(level+1, max_distance, dict_distance)
    return None

def city_search(my_location: str, cities_weather: dict, iatas_weather: dict):
    """Returns the weather of the required place (IATA code or city).
    If it is not found, uses the place with similar writing.

    Args:
        my_location (str): the given location.
        cities_weather (dict): Cities and their weathers.
        iatas_weather (dict): IATA codes and their weathers.

    Returns:
        str: the weather of the indicated place.
    """
    max_dist_iata = 1
    max_dist_city = 2
    max_distance = max(max_dist_city, max_dist_iata)
    dict_distance = calculate_distance(my_location, max_dist_iata, max_dist_city, cities_weather, iatas_weather)
    return closest_word(0, max_distance, dict_distance)

