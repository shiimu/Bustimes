import requests
import json
import time
import datetime


# Use HSL:(int) code here to query the right stop
def queryApi(stop_id):
    # Api address
    url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
    # Calling from Api. Queryng only the wanted stuff.
    payload = {"query":"{\n  stop(id: \"" + stop_id + "\") {  name   stoptimesWithoutPatterns{ realtimeDeparture    serviceDay   headsign trip{route{ shortName}}}}}"}
    headers= {"Content-Type" : "application/json"}
    global response
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

    # Dumping the response in json format
    global dumped_data
    dumped_data = response.json()
    #print(dumped_data)
    return dumped_data


'''
# Needs to be added to somewhere else
def checkRepeat():
    called = False
    while called != True:
        queryApi('HSL:1472113')
        print(dumped_data)

        called = True    
        time.sleep(15)
        called = False
        print("bump")

while initiated:
    checkRepeat()

'''


"""
print(response.text)
print(response.status_code) 


# Getting into the right places
# Fix naming conventions into singular
datawrap = dumped_data['data']
stopwrap = datawrap['stop']
stoptimes_wrap = stopwrap['stoptimesWithoutPatterns']
stop_name = stopwrap['name']

# Getting the bus sign from the dictionary
tripWrap = stoptimes_wrap[0]['trip']
routeWrap = tripWrap['route']
busRouteSign = routeWrap['shortName']
busHeadSign = stoptimes_wrap[0]['headsign']
# For testing if i get the right values
print(stop_name)
print(busRouteSign)
print(busHeadSign)
# print(stoptimes_wrap[1]['serviceDay'])
# print(stoptimes_wrap[2]['scheduledArrival'])

# Getting the next incoming bus time in utc
# Its holding the values inside. So doing[1] will give the next busses time
stopDay = int(stoptimes_wrap[0]['serviceDay'])
stopTime= int(stoptimes_wrap[0]['scheduledArrival'])
busTime = stopDay + stopTime
#print(busTime)
strBusTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(busTime))
print(strBusTime)
# Minutes Left
currentTime = time.time()
timeLeft = busTime - currentTime
#print (timeLeft)
if timeLeft <= 60:
    normLeft = "0"
else:    
    normLeft = time.strftime('%M', time.localtime(timeLeft))
print(normLeft + " Minutes Left")


"""