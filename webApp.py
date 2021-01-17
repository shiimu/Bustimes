from flask import Flask, render_template, json, jsonify
import time
import requests
from callInfo import queryApi, queryApi_2, queryApi_3, queryApi_4

stop_id = 'HSL:1472113'
stop_id_2 = 'HSL:1472128'
stop_id_3 = 'HSL:1472114'
stop_id_4 = 'HSL:1472148'
app = Flask(__name__)
queryApi_3(stop_id_3), queryApi_4(stop_id_4), queryApi(stop_id),queryApi_2(stop_id_2)

@app.route("/")
def bustimes():
    from sorting import data_wrap, refresh_data, bus_Number, bus_Name, bus_Time_Left
    from sorting_2 import data_wrap_2, refresh_data_2, bus_Number_2, bus_Name_2, bus_Time_Left_2
    from sorting_3 import data_wrap_3, refresh_data_3, bus_Number_3, bus_Name_3, bus_Time_Left_3
    from sorting_4 import data_wrap_4, refresh_data_4, bus_Number_4, bus_Name_4, bus_Time_Left_4
    refresh_data()
    refresh_data_2()
    refresh_data_3()
    refresh_data_4()
    bustimes2()
    #print(refresh_data(),refresh_data_2(),refresh_data_3(),refresh_data_4())
    timeNow = time.strftime('%H:%M', time.localtime(time.time()))    
    return render_template('main.html', timen = timeNow, busK1 = bus_Number(0), busR1 = bus_Name(0), busT1 = bus_Time_Left(0),
                                                         busK2 = bus_Number(1), busR2 = bus_Name(1), busT2 = bus_Time_Left(1),
                                                         busK3 = bus_Number(2), busR3 = bus_Name(2), busT3 = bus_Time_Left(2),
                                                         busK4 = bus_Number(3), busR4 = bus_Name(3), busT4 = bus_Time_Left(3),
                                                         busK5 = bus_Number(4), busR5 = bus_Name(4), busT5 = bus_Time_Left(4),
                                                         busK6 = bus_Number_2(0), busR6 = bus_Name_2(0), busT6 = bus_Time_Left_2(0),
                                                         busK7 = bus_Number_2(1), busR7 = bus_Name_2(1), busT7 = bus_Time_Left_2(1),
                                                         busK8 = bus_Number_2(2), busR8 = bus_Name_2(2), busT8 = bus_Time_Left_2(2),
                                                         busK9 = bus_Number_2(3), busR9 = bus_Name_2(3), busT9 = bus_Time_Left_2(3),
                                                         busK10 = bus_Number_2(4), busR10 = bus_Name_2(4), busT10 = bus_Time_Left_2(4),
                                                         busK11 = bus_Number_3(0), busR11 = bus_Name_3(0), busT11 = bus_Time_Left_3(0),
                                                         busK12 = bus_Number_3(1), busR12 = bus_Name_3(1), busT12 = bus_Time_Left_3(1),
                                                         busK13 = bus_Number_3(2), busR13 = bus_Name_3(2), busT13 = bus_Time_Left_3(2),
                                                         busK14 = bus_Number_3(3), busR14 = bus_Name_3(3), busT14 = bus_Time_Left_3(3),
                                                         busK15 = bus_Number_3(4), busR15 = bus_Name_3(4), busT15 = bus_Time_Left_3(4),
                                                         busK16 = bus_Number_4(0), busR16 = bus_Name_4(0), busT16 = bus_Time_Left_4(0),
                                                         busK17 = bus_Number_4(1), busR17 = bus_Name_4(1), busT17 = bus_Time_Left_4(1),
                                                         busK18 = bus_Number_4(2), busR18 = bus_Name_4(2), busT18 = bus_Time_Left_4(2),
                                                         busK19 = bus_Number_4(3), busR19 = bus_Name_4(3), busT19 = bus_Time_Left_4(3),
                                                         busK20 = bus_Number_4(4), busR20 = bus_Name_4(4), busT20 = bus_Time_Left_4(4))
                                                         
def bustimes2():
    #print(refresh_data(),refresh_data_2(),refresh_data_3(),refresh_data_4())
    return queryApi_3(stop_id_3), queryApi_4(stop_id_4), queryApi(stop_id),queryApi_2(stop_id_2)

if __name__ == "__main__":
    app.run( debug = True )
#stop_id = 'HSL:1472113'
#stop_id_2 = 'HSL:1472128'
#stop_id_3 = 'HSL:1472114'
#stop_id_4 = 'HSL:1472148'
# host = '192.168.1.125',
