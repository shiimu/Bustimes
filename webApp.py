from flask import Flask, render_template
import time
app = Flask(__name__)

@app.route("/")
def bustimes():
    from CallApi import busRouteSign, normLeft, busHeadSign

    busK = busRouteSign
    busR = busHeadSign
    busT =  normLeft
    busK2 = busRouteSign
    busR2 = busHeadSign
    busT2 =  normLeft
    busK3 = busRouteSign
    busR3 = busHeadSign
    busT3 =  normLeft
    busK4 = busRouteSign
    busR4 = busHeadSign
    busT4 =  normLeft
    timeNow = time.strftime('%H:%M', time.localtime(time.time()))    
    return render_template('main.html', timen = timeNow, busK1 = busK, busR1 = busR, busT1 = busT,
                                                     busK22 = busK2, busR22 = busR2, busT22 = busT2,
                                                     busK33 = busK3, busR33 = busR3, busT33 = busT3,
                                                     busK44 = busK4, busR44 = busR4, busT44 = busT4)

if __name__ == "__main__":
    app.run( debug = True )