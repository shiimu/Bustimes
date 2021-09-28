import time, json

data_wrap = []

def refresh_data():
    global data_wrap
    global stop_times_wrap
    global dumped_data
    data_wrap.clear()
    try:
        with open('datadump.json') as f:
            dumped_data = json.load(f)
            data_wrap = dumped_data['data']
            stop_wrap = data_wrap['stop']
            stop_times_wrap = stop_wrap['stoptimesWithoutPatterns']
            # Getting the bus sign.
            return data_wrap
    except:
        print("Error! datadump.json is empty!")
# At first I had all 3 together. But had trouble singleing out any one var. so decided to split to 3 functions.
def bus_Name(number):
    global bus_name
    bus_name = stop_times_wrap[number]['headsign']
    return bus_name
def bus_Time_Left(number):
    global norm_left
    # Getting the departure time
    stop_day = int(stop_times_wrap[number]['serviceDay'])
    stop_time= int(stop_times_wrap[number]['realtimeDeparture'])
    
    bus_time = stop_day + stop_time
    current_time = time.time()
    time_left = bus_time - int(current_time)
    # throws an error if time_left is negative
    # print(time_left)
    norm_left = time.strftime('%M', time.localtime(time_left))
    if time_left > 3600:
        norm_left = time.strftime('%H:%M', time.localtime(bus_time)) 
        return norm_left
    elif time_left < 0:
        norm_left = '00'
        return norm_left
    return norm_left     
def bus_Number (number) :
    global bus_number
    bus_number = stop_times_wrap[number]['trip']['route']['shortName']
    return bus_number
#print(bus(0)) '''
