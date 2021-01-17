import time, json

data_wrap_2 = []

def refresh_data_2():
    global data_wrap_2
    global stop_times_wrap
    global dumped_data
    data_wrap_2.clear()
    try: 
        with open('datadump_2.json') as f:
            dumped_data = json.load(f)
            data_wrap_2 = dumped_data['data']
            stop_wrap = data_wrap_2['stop']
            stop_times_wrap = stop_wrap['stoptimesWithoutPatterns']
            # Getting the bus sign.
            return data_wrap_2
    except:
        return dumped_data

# At first I had all 3 together. But had trouble singleing out any one var. so decided to split to 3 functions.
def bus_Name_2(number):
    global bus_name
    bus_name = stop_times_wrap[number]['headsign']
    return bus_name
def bus_Time_Left_2(number):
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
def bus_Number_2(number) :
    global bus_number
    bus_number = stop_times_wrap[number]['trip']['route']['shortName']
    return bus_number
#print(bus(0)) '''