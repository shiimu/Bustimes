from callInfo import dumped_data
import time

busses = dumped_data['data']['stop']['stoptimesWithoutPatterns']
print(busses[0:5])
busses.update()
#bus_name = busses.index('shortName')

'''
print(stop_names[0])

def busses():
    i = 0
    bus_Name = stop_times_wrap[i]['headsign']
    bus_Time_L = int(stop_times_wrap[i]['serviceDay']) + int(stop_times_wrap[i]['realtimeArrival']) - time.time()
    bus_Number = stop_times_wrap[i]['trip']['route']['shortName']

    return bus_Name, bus_Time_L,bus_Number

# At first I had all 3 together. But had trouble singleing out any one var. so decided to split to 3 functions.
def bus_sName(number):
    global bus_name
    bus_name = stop_times_wrap[number]['headsign']
    return bus_name
def bus_Time_L(number):
    global norm_left

    stop_day = int(stop_times_wrap[number]['serviceDay'])
    stop_time= int(stop_times_wrap[number]['realtimeArrival'])
    
    bus_time = stop_day + stop_time
    current_time = time.time()
    time_left = bus_time - current_time
    # throws an error if time_left is negative
    if time_left <= 60:
        norm_left = "~0"
    else:    
        norm_left = time.strftime('%M', time.localtime(time_left)) 
        return norm_left
def bus_Number():
    global bus_num

    bus_num = stop_times_wrap['trip']['route']['shortName']

    return bus_num
    


#print(bus(0))
'''