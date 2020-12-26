import requests
import json
import time
import datetime


# Use HSL:(int) code here to query the right stop
# Api address
url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
# Calling from Api. Queryng only the wanted stuff.
payload = {"query":"{nearest(lat: 60.239, lon: 25.10109, maxDistance: 500, filterByPlaceTypes: DEPARTURE_ROW){edges{node {place {...on DepartureRow {stop {name}stoptimes{serviceDay realtimeDeparture trip { route {shortName}}headsign }}}}}}}}"}
headers= {"Content-Type" : "application/json"}
response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
# Dumping the response in json format
global dumped_data
dumped_data = response.json()
#print(dumped_data)
#    with open('datadump.json', 'w')as json_file:
#        json.dump(dumped_data, json_file)


def sorting(number):
    global nodes_wrap
    nodes_wrap = edges_wrap[number]['node']['place']
    print(nodes_wrap)
sorting(0)
sorting(1)
sorting(2)
sorting(3)
sorting(4)
sorting(5)
sorting(6)
sorting(7)
sorting(8)
sorting(9)
sorting(10)
sorting(11)
sorting(12)

