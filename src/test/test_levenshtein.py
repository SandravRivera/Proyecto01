import unittest

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")

from levenshtein import normalize_word
from levenshtein import levenshtein_distance
from levenshtein import calculate_distance
from levenshtein import closest_word
from levenshtein import city_search

class TestLevenshtein(unittest.TestCase):

    def test_levenshtein_distance(self):
        string1 = ""
        string2 = ""

        self.assertTrue(levenshtein_distance(string1, string2) == 0)

        string1 = "!.?*4"
        self.assertTrue(levenshtein_distance(string1, string2) == 0)

        string1 = "Monterrey"
        string2 = "a"
        self.assertFalse(levenshtein_distance(string1, string2) == 0)
        
        string2 = "Mon_TERreY3????"
        self.assertTrue(levenshtein_distance(string1, string2) == 0)
        
        string2 = string1
        self.assertTrue(levenshtein_distance(string1, string2) == 0)

        for y in range(len(string1)+1):
            string2 = string1[y:]
            string_list2 = list(string2)        
            for x in range(len(string2)):
                string_list2[x] = "a"
                string2 = "".join(string_list2)
                distance = levenshtein_distance(string1, string2)
                self.assertTrue(distance == 1+y+x)
    

    def test_normalize_word(self):
        string1 = "!.?*"
        self.assertEqual("", normalize_word(string1))

        string1 = "Monterrey"
        string2 = "Monterey"
        self.assertFalse(normalize_word(string1) == normalize_word(string2))
        string2 = "Guadalajara"
        self.assertFalse(normalize_word(string1) == normalize_word(string2))

        expected = "MONTERREY"
        
        string1 = "monterrey"
        string2 = "MontErReY"        
        self.assertEqual(normalize_word(string1), expected)
        self.assertEqual(normalize_word(string2), expected)  
        
        string1 = "\nMo nte\nr rey."        
        self.assertEqual(expected, normalize_word(string1))

    def test_calculate_distance(self):
        IATA_ws = {
            'ACA':'weather1',
            'AGU':'weather2',
            'AMS':'weather3',
            'ATL':'weather4'
        }
        city_ws = {
            'Acapulco':'weather1',
            'Aguascalientes':'weather2',
            'Amsterdam':'weather3',
            'Atlanta':'weather4'
        }        
        IATA_max = 0
        city_max = 0
        
        result = calculate_distance("ATS", IATA_max, city_max, city_ws,
                                    IATA_ws)
        self.assertEqual(result, {})
        result = calculate_distance("ATL", IATA_max, city_max, city_ws,
                                    IATA_ws)
        self.assertEqual(result, {0: ['weather4']})
        
        IATA_max+=1
        result = calculate_distance("ATS", IATA_max, city_max, city_ws,
                                    IATA_ws)
        self.assertTrue(len(result) == 1)
        result_list = None
        try:
            result_list = result.get(1)
        except:
            self.fail("Key for distance 1 not found (max. IATA distance = 1).")
        self.assertTrue(len(result_list) == 2)
        self.assertTrue(('weather3' in result_list) and
                        ('weather4' in result_list))

        IATA_max = 100
        result = calculate_distance("Acapulco", IATA_max, city_max, city_ws,
                                    IATA_ws)
        result_list2 = None
        try:
            result_list = result.get(0)
            result_list2 = result.get(5)
        except:
            self.fail("Key for expected distances 0 or 5 not found.")
        self.assertIn("weather1", result_list)
        self.assertIn("weather1", result_list2)
        

    def test_closest_word(self):
        IATA_ws = {
            'ACA':'weather1',
            'AGU':'weather2',
            'AMS':'weather3',
            'ATL':'weather4'
        }
        city_ws = {
            'Acapulco':'weather1',
            'Aguascalientes':'weather2',
            'Amsterdam':'weather3',
            'Atlanta':'weather4'
        }
        IATA_max = 1
        city_max = 2
        level = 1
        distance_max = 0
        distance_dictionary = calculate_distance("Acapulco", IATA_max,
                                                 city_max, city_ws, IATA_ws)

        result = closest_word(level, distance_max, distance_dictionary)
        self.assertEqual(result, None)
        
        level = 0
        result = closest_word(level, distance_max, distance_dictionary)
        self.assertEqual(result, "weather1")

        distance_max = 1
        level = 1
        distance_dictionary = calculate_distance("ATS", IATA_max,
                                                 city_max, city_ws, IATA_ws)
        weather_list = distance_dictionary.get(1)
        self.assertTrue(len(weather_list) > 1)
        expected = weather_list[0]
        result = closest_word(level, distance_max, distance_dictionary)
        self.assertEqual(result, expected)

    def test_city_search(self):
        IATA_ws = {
            'ACA':'weather1',
            'AGU':'weather2',
            'AMS':'weather3',
            'ATL':'weather4'
        }
        city_ws = {
            'Acapulco':'weather1',
            'Aguascalientes':'weather2',
            'Amsterdam':'weather3',
            'Atlanta':'weather4'
        }

        city_max = 2
        IATA_max = 1

        query = ""
        self.assertEqual(city_search(query, city_ws, IATA_ws), None)
        query = "?-.*3"
        self.assertEqual(city_search(query, city_ws, IATA_ws), None)
        query = "zzzzzzzz"
        self.assertEqual(city_search(query, city_ws, IATA_ws), None)

        query = "Atlanta"
        self.assertEqual(city_search(query, city_ws, IATA_ws), "weather4")
        query = "Atlantis"
        self.assertEqual(city_search(query, city_ws, IATA_ws), "weather4")
        query = "Atlantic City"
        self.assertEqual(city_search(query, city_ws, IATA_ws), None)

        query = "ATS"
        distance_dictionary = calculate_distance(query, IATA_max, city_max,
                                                 city_ws, IATA_ws)
        expected = distance_dictionary.get(1)[0]
        
        self.assertEqual(city_search(query, city_ws, IATA_ws), expected)
    
        

if __name__ == '__main__':
    unittest.main()
