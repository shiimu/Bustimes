import pymongo
import requests
import json
from pymongo import MongoClient, collection

def queryWeatherApi():
    getSecret()
    # Api address
    url = "https://api.openweathermap.org/data/2.5/weather?lat=60.23787364561019&lon=25.10560957759351&appid="+ key + ""
    # Calling from Api. Queryng only the wanted stuff.
    payload = {"query":'{\n  "weather": {'}
    headers= {"Content-Type" : "application/json"}
    response = requests.get(url, headers=headers, data = json.dumps(payload))
    # Dumping the response in json format
    global dumped_weather
    dumped_weather = response.json()
    #print(dumped_weather)
    weatherToDB()
    #with open('datadump.json', 'w')as json_file:
    #    json.dump(dumped_data, json_file)
    #return
# Add weather to the database
def weatherToDB():
    client = MongoClient('localhost', 27017)
    db = client['weatherInfo']
    collection = db['weatherKelvin']
    collection.insert(dumped_weather)
    
#get the secret from the database
def getSecret():
    global key
    client = MongoClient('localhost', 27017)
    db = client['weatherInfo']
    collection = db['weatherKey']
    keyv = collection.find_one({}) 
    keyvs = keyv['secret']
#    print(keyvs)
    key = keyvs
 
#get weather infro from the database
def weatherFromDB():
    global lastTemp
    client = MongoClient('localhost', 27017)
    db = client['weatherInfo']
    collection = db['weatherKelvin']
    last_weather = collection.find_one({}) 
    lastMain = last_weather['main']
    lastTemp = lastMain['temp']
    toCelsius()

#conversion from Kelvin to Celsius
def toCelsius():
    global tempInInt
    converted_Temps =  lastTemp - 273.15
    tempInInt = int(converted_Temps)
    dropWeather()
#im gonna just drop the collection, because i only need one temperature data at any given time
def dropWeather():
    client = MongoClient('localhost', 27017)
    db = client['weatherInfo']
    collection = db['weatherKelvin']
    if collection.count() != 0:
        collection.drop()
        