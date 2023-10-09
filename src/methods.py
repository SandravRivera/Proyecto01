import sys
import time
import requests
from flask import jsonify
from iataCities import iata_cities
from levenshtein import city_search

key = "&appid=155505a47faf9082a7ee3d45f7b1ea0b&units=metric" #key of the API
url = "https://api.openweathermap.org/data/2.5/weather?"
cache = {} #Dictionary "IATA" : weather
tickets = {} #Dictionary "ticket": [IATA1, IATA2]
cities = {} #Dictionary "name_of_the_city" : weather

def validLine(raw_line):
    """Method to check if a line in the dataset is valid. 

    Args:
        raw_line (string): the line as a string

    Returns:
        list[string]: a list of the elements of the line
    """
    line = raw_line.split(",")
    if len(line[0])!=16:
        print(f"\nTicket {line[0]} is not valid, must have exactly 16 characters.")
    try:
        line[3] = float(line[3])
        line[4] = float(line[4])
        line[5] = float(line[5])
        line[6] = float(line[6])
    except:
        print(f"\nFormat of latitude or longitude is not valid on line {line}, must have exactly 16 characters.")
    return line


def readData(data_list):
    """Method to read the data from the data_list and to create the cache

    Args:
        data_list (list): A list with the data of the dataset.

    Returns:
        None.
    """
    for raw_line in data_list:
        line = validLine(raw_line) #check if the line is valid
        tickets[line[0]] = [line[1], line[2]]
        
        if not line[1] in cache:
            try:
                url1 = (f"{url}lat={line[3]}&lon={line[4]}{key}") #create the url
                weather = get_weather(url1)
                weather["name"] = iata_cities[line[1]]
                cache[line[1]] = weather
                cities[iata_cities[line[1]]] = weather
                time.sleep(1.05)
            except:
                print(f"\nCould't request the weather information. The input {line} is probably incorrect.")
                sys.exit()
                
        if not line[2] in cache:
            try:
                url2 = (f"{url}lat={line[5]}&lon={line[6]}{key}")
                weather = get_weather(url2)
                weather["name"] = iata_cities[line[2]]
                cache[line[2]] = weather
                cities[iata_cities[line[2]]] = weather
                time.sleep(1.05)
            except:
                print(f"\nCould't request the weather information. The input {line} is probably incorrect.")
                sys.exit()


def searchWeatherWith_ticket(ticket):
    """method to search the weather of the cities included in an airplane ticket

    Args:
        ticket (string): ticket we want to search

    Returns:
        dict: A dictionary with the weather of the cities included in the ticket.
        None if the ticket doesnt exist.
    """
    if(ticket in tickets):
        IATAS = tickets[ticket]
        weather1 = cache[IATAS[0]]
        weather2 = cache[IATAS[1]]
        weather = {
            "name1": weather1["name"],
            "weather1": weather1["weather"],
            "temp1": weather1['temp'],
            "humidity1": weather1['humidity'],
            "name2": weather2["name"],
            "weather2": weather2["weather"],
            "temp2": weather2['temp'],
            "humidity2": weather2['humidity']
        }
        return weather
    else:
        return None
       
            
def searchWeatherWith_NameOfCity(city):
    """method to search the weather of a city with the name of the city

    Args:
        city (string): name of the city

    Returns:
        dict: A dictionary with the weather
        None if the the city is not valid.
    """
    if city in cities:
        return cities[city]
    
    return city_search(city, cities, cache)

    
def get_weather(url1):
    """It makes the API call to get a JSON, extracts and collects the information we want for the weather in 
    a dictionary named weather and return the dictionary.

    Args:
        url1 (string): The url to make the API call

    Returns:
        dict: A dictionary with the data of the weather
    """
    res1 = requests.get(url1) 
    data1 = res1.json()
    weather = {
        "weather": data1['weather'][0]['main'],
        "temp": round(data1['main']['temp']),
        "humidity": data1['main']['humidity']
    }
    return weather


def start():
    """Open the dataset, get a list of the lines from the file, and read the data.
    """
    data_csv = open('src/dataset2.csv')
    data_list = data_csv.readlines()
    data_list.pop(0)
    readData(data_list)
    