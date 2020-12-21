from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def bustimes():
    from callInfo import queryApi
    queryApi('HSL:1472113')
    from sorting import busName, busNumber, busTimeL

    timeNow = time.strftime('%H:%M', time.localtime(time.time()))    
    return render_template('main.html', timen = timeNow, busK1 = busNumber(0), busK2 = busNumber(1),
                                                         busK3 = busNumber(2), busK4 = busNumber(3),
                                                         busK5 = busNumber(4),
                                                         busR1 = busName(0), busR2 = busName(1),
                                                         busR3 = busName(2), busR4 = busName(3),
                                                         busR5 = busName(4),
                                                         busT1 = busTimeL(0), busT2 = busTimeL(1),
                                                         busT3 = busTimeL(2), busT4 = busTimeL(3),
                                                         busT5 = busTimeL(4))  
    
if __name__ == "__main__":
    app.run( debug = True )