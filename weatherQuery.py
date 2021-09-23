import requests
import json

def queryWeatherApi():
    # Api address
    url = "https://api.openweathermap.org/data/2.5/weather?lat=60.23787364561019&lon=25.10560957759351&appid=APIKEY"
    # Calling from Api. Queryng only the wanted stuff.
    payload = {"query":'{\n  "weather": {'}
    headers= {"Content-Type" : "application/json"}
    response = requests.get(url, headers=headers, data = json.dumps(payload))
    # Dumping the response in json format
    global dumped_data
    dumped_data = response.json()
    print(dumped_data)
    #with open('datadump.json', 'w')as json_file:
    #    json.dump(dumped_data, json_file)
    #return