from flask import Flask, render_template
import time

app = Flask(__name__)
# use js to refresh api calls over a period.
@app.route("/")
def bustimes():
    from CallApi import busRouteSign, normLeft, busHeadSign
    busK = busRouteSign
    busR = busHeadSign
    busT =  normLeft
    timeNow = time.strftime('%H:%M', time.localtime(time.time()))    
    return render_template('main.html', timen = timeNow, busK1 = busK, busR1 = busR, busT1 = busT)

if __name__ == "__main__":
    app.run( debug = True )