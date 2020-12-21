from callInfo import dumped_data
import time

data_wrap = dumped_data['data']
stop_wrap = data_wrap['stop']
stop_times_wrap = stop_wrap['stoptimesWithoutPatterns']
stop_name = stop_wrap['name']

# Getting the bus sign.
trip_wrap = stop_times_wrap[0]['trip']
route_wrap = trip_wrap['route']
short_name_wrap = route_wrap['shortName']
# Getting the arrival time
stopDay = int(stop_times_wrap[0]['serviceDay'])
stopTime= int(stop_times_wrap[0]['scheduledArrival'])
busTime = stopDay + stopTime

def bus(number):
    bus_num = stop_times_wrap[number]['trip']['route']['shortName']
    bus_name = stop_times_wrap[number]['headsign']
    stop_day = int(stop_times_wrap[number]['serviceDay'])
    stop_time= int(stop_times_wrap[number]['scheduledArrival'])
    
    bus_time = stop_day + stop_time
    current_time = time.time()
    time_left = bus_time - current_time
    
    if time_left <= 60:
        norm_left = "~0"
    else:    
        norm_left = time.strftime('%M', time.localtime(time_left))

    print(bus_num, bus_name, norm_left)

print(bus(0))