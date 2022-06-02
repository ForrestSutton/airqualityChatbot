import requests
import json
from json import dumps
import pandas as pd
from httplib2 import Http
import os


def get_aqi():
    URL =  os.environ.get('DATA_URL')
    r = requests.get(URL)
    j = json.loads(r.text)

    num = j['sensor']['pm2.5']
    return num




def main():
    aqi = get_aqi()
    aqi = float()

    if aqi < 50:
        bot_message = {'text' :' Good air quality AQI under 50' }
    elif aqi > 51 and aqi < 100:
        bot_message = {'text' :' Moderate air quality AQI between 50 and 100' }
    elif aqi > 101 and aqi < 150:
        bot_message = {'text' :'Moderate air quality AQI between 100 and 150' }
    elif aqi > 151 and aqi < 200:
        bot_message = {'text' :'Unhealthy for sensitive groups AQI between 151 and 200' }
    elif aqi > 201 and aqi < 300:
        bot_message = {'text' :'Unhealthy air quality AQI between 201 and 300' }
    else:
        bot_message = {'text' : 'Very unhealthy air quality AQI over 301' }

    url =  os.environ.get('CHATBOT_URL')
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    if aqi > 50:
        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
            )
    else:
        pass

    #print(response)


if __name__ == '__main__':
    main()
