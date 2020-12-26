import time, json

data_wrap_4 = []

def refresh_data_4():
    global data_wrap_4
    global stop_times_wrap
    global dumped_data
    data_wrap_4.clear()
    with open('datadump_4.json') as f:
        dumped_data = json.load(f)
        data_wrap_4 = dumped_data['data']
        stop_wrap = data_wrap_4['stop']
        stop_times_wrap = stop_wrap['stoptimesWithoutPatterns']
        # Getting the bus sign.
        return data_wrap_4


# At first I had all 3 together. But had trouble singleing out any one var. so decided to split to 3 functions.
def bus_Name_4(number):
    global bus_name
    bus_name = stop_times_wrap[number]['headsign']
    return bus_name
def bus_Time_Left_4(number):
    global norm_left
    # Getting the departure time
    stop_day = int(stop_times_wrap[number]['serviceDay'])
    stop_time= int(stop_times_wrap[number]['realtimeDeparture'])
    
    bus_time = stop_day + stop_time
    current_time = time.time()
    time_left = bus_time - int(current_time)
    # throws an error if time_left is negative
    # print(time_left)
    try:
        norm_left = time.strftime('%M', time.localtime(time_left)) 
        return norm_left
    except:
        norm_left = '00'
        return norm_left
         
def bus_Number_4(number) :
    global bus_number
    bus_number = stop_times_wrap[number]['trip']['route']['shortName']
    return bus_number
#print(bus(0)) '''