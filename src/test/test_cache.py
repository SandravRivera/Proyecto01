import unittest
import requests
import sys
import time
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")

import methods

from methods import *

from iataCities import iata_cities
from levenshtein import city_search


class TestCache(unittest.TestCase):
    
    def test_validLine(self):
        
        ticket = ""
        ticket_list = None
        
        ticket_list = validLine(ticket)
        self.assertEqual(ticket_list, None)
        
        ticket = "a"        
        ticket_list = validLine(ticket)
        self.assertEqual(ticket_list, None)
        
        ticket = "aaaaaaaaaaaaaaaa,bbb,ccc,d,e,f,g"
        validLine(ticket)
        self.assertEqual(ticket_list, None)
        
        
        ticket = "C3NZsz5xBt82F4NJ,GDL,MEX,20.5218,-103.311,19.4363,-99.0721"
        list = ["C3NZsz5xBt82F4NJ","GDL","MEX",20.5218,-103.311,19.4363,
                -99.0721]
        self.assertEqual(list, validLine(ticket))

        
    def test_readData(self):

        methods_cache = methods.cache
        methods_tickets = methods.tickets
        methods_cities = methods.cities

        methods.cache = {}
        methods.tickets = {}
        methods.cities = {}

        ticket1 = ""
        ticket2 = "a"
        ticket3 = "aaaaaaaaaaaaaaaa,bbb,ccc,d,e,f,g"
        data_list_test = [ticket1, ticket2, ticket3]
        try:
            readData(data_list_test)
        except:
            pass
        self.assertEqual(methods.cache, {})
        self.assertEqual(methods.tickets, {})
        self.assertEqual(methods.cities, {})
        
        
        ticket1 = "ejcwGA8AcLcWQ72g,GDL,MEX,20.5218,-103.311,19.4363,-99.0721"
        ticket2 = "nB6WtNW8vKrWHzyC,GDL,MEX,20.5218,-103.311,19.4363,-99.0721"
        data_list_test = [ticket1, ticket2]
        expected_cache_dict = {
            "GDL" : "GDL-weather",
            "MEX" : "MEX-weather"
            }
        expected_tickets_dict = {
            "ejcwGA8AcLcWQ72g" : ["GDL", "MEX"],
            "nB6WtNW8vKrWHzyC" : ["GDL", "MEX"]
            }
        try:
            readData(data_list_test)
        except:
            self.fail("Failed to read valid tickets.")
        self.assertEqual(methods.tickets, expected_tickets_dict)
        self.assertEqual(len(methods.cache), 2)
        self.assertEqual(len(methods.cities), 2)
        self.assertIn("GDL", methods.cache)
        self.assertIn("MEX", methods.cache)
        self.assertIn("Guadalajara", methods.cities)
        self.assertIn("Ciudad de México", methods.cities)

        data_list_test = [ticket1, ticket3, ticket2]
        try:
            readData(data_list_test)
        except:
            self.fail("Failed to skip non valid line")
        self.assertEqual(methods.tickets, expected_tickets_dict)
        self.assertEqual(len(methods.cache), 2)
        self.assertEqual(len(methods.cities), 2)        
        self.assertIn("GDL", methods.cache)
        self.assertIn("MEX", methods.cache)
        self.assertIn("Guadalajara", methods.cities)
        self.assertIn("Ciudad de México", methods.cities)

        methods.cache = methods_cache
        methods.tickets = methods_tickets
        methods.cities = methods_cities


    def test_searchWeatherWith_ticket(self):
        
        ticket1 = "ejcwGA8AcLcWQ72g,GDL,MEX,20.5218,-103.311,19.4363,-99.0721"
        number1 = "ejcwGA8AcLcWQ72g"

        methods_cache = methods.cache
        methods_tickets = methods.tickets
        methods_cities = methods.cities
        
        methods.cache = {}
        methods.tickets = {}
        methods.cities = {}
        
        self.assertEqual(searchWeatherWith_ticket(number1), None)
        
        ticket_list_test = [ticket1]
        readData(ticket_list_test)
        weather_dict = searchWeatherWith_ticket(number1)
        self.assertFalse(weather_dict == None)
        
        expected_keys = ["name1", "weather1", "temp1", "humidity1", "name2",
                         "weather2", "temp2", "humidity2"]
        
        weather1_cache_dict = methods.cache.get("GDL")
        weather2_cache_dict = methods.cache.get("MEX")
        
        for i in range(4):
            self.assertIn(expected_keys[i], weather_dict)
            limit = len(expected_keys[i])-1
            self.assertEqual(weather_dict.get(expected_keys[i]),
                             weather1_cache_dict.get(expected_keys[i][0:limit]))

        for i in range(4, 8):
            self.assertIn(expected_keys[i], weather_dict)
            limit = len(expected_keys[i])-1
            self.assertEqual(weather_dict.get(expected_keys[i]),
                             weather2_cache_dict.get(expected_keys[i][0:limit]))
        

        methods.cache = methods_cache
        methods.tickets = methods_tickets
        methods.cities = methods_cities
        

    def test_searchWeatherWith_NameOfCity(self):

        methods_cache = methods.cache
        methods_tickets = methods.tickets
        methods_cities = methods.cities
        
        methods.cache = {}
        methods.tickets = {}
        methods.cities = {}
        
        city = "Guadalajara"
        self.assertEqual(searchWeatherWith_NameOfCity(city), None)
        
        ticket1 = "ejcwGA8AcLcWQ72g,GDL,MEX,20.5218,-103.311,19.4363,-99.0721"
        ticket_list_test = [ticket1]
        readData(ticket_list_test)

        weather_dict = searchWeatherWith_NameOfCity(city)
        self.assertFalse(weather_dict == None)
        
        expected_keys = ["name", "weather", "temp", "humidity"]
        
        weather_cache_dict = methods.cache.get("GDL")
        
        for i in range(4):
            self.assertIn(expected_keys[i], weather_dict)
            self.assertEqual(weather_dict.get(expected_keys[i]),
                             weather_cache_dict.get(expected_keys[i]))

        
        methods.cache = methods_cache
        methods.tickets = methods_tickets
        methods.cities = methods_cities


    def test_get_weather(self):
        test_url = (f"{methods.url}lat=20.5218&lon=-103.311{methods.key}")
        
        weather_dict = get_weather(test_url)
        self.assertTrue(len(weather_dict) == 3)
        
        expected_keys = ["weather", "temp", "humidity"]
        
        for i in range(3):
            self.assertIn(expected_keys[i], weather_dict)
            self.assertFalse(weather_dict.get(expected_keys[i]) == None)



if __name__ == '__main__':
    unittest.main()
