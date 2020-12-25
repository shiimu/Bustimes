from flask import Flask, render_template, json, jsonify
import time
import requests
from callInfo import queryApi
app = Flask(__name__)

global stop_id
stop_id = 'HSL:1472113'
queryApi('HSL:1020453')
@app.route("/")
def bustimes():
    from sorting import bus_Number, bus_Name, bus_Time_L

    timeNow = time.strftime('%H:%M', time.localtime(time.time()))    
    return render_template('main.html', timen = timeNow, busK1 = bus_Number(0) , busR1 = bus_Name(0), busT1 = bus_Time_L(0)), queryApi(stop_id)

if __name__ == "__main__":
    app.run( debug = True )
