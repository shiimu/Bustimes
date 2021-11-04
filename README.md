# Bustimes webapp running on Flask using the HSL API for stop times and OpenWeatherMap API for the weather data.
![Pic](https://i.ibb.co/khSyjN7/Bustimes-SS.png)
#### Highly inspired by https://github.com/stetro/digitransit-busstop-sign
## Requirements and how to install!
### Libraries and technologies:
- Flask
- MongoDB
- requests
- pymongo
- json

## Installation:
### Install MongoDB
- Download and install MongoDB Community edition https://www.mongodb.com/try/download/community
### Install libraries:
- In your terminal do:
  - pip install flask
  - pip install requests
  - pip install pymongo
  - pip install json
### Setting up the bus stops and weather data:
- Open webApp.py
  - Change the variables stop_id (1-4) to the desired HSL Bus Stop IDs.
    - Example:</br>
      ![Pic](https://i.ibb.co/71wXmbx/example-img.png)
- Open MongoDB
  - Create a Database called WeatherInfo with the collection WeatherKey
    - Create a document with a string named 'secret' with the value: {YOUR OPENWEATHERMAP API KEY HERE}
    - Example:</br>
    ![Pic](https://i.ibb.co/xSTT57k/DB-Setup-Example.png)

## Running the app
### In you terminal move to the Bustimes folder:
  - cd ../Bustimes
### Run webApp.py
  - python3 webApp.py
## The webApp can be accessed from localhost://8080
