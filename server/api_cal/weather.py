import httplib2
import json

from api_cal.setup import setup

import logging
logger = logging.getLogger("TB")

API_WEATHER_KEY = "ea1b2a690767c4cffc1832b89fe81d68"

class Weather:

    @classmethod
    def w_current_temp(self):
        h = httplib2.Http()

        lt_ln = setup.get_position()

        (heads, resp) = h.request("http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&units=metric&appid=%s" % (lt_ln["lat"],lt_ln["lng"],API_WEATHER_KEY), "GET")
        resp = json.loads(resp)

        return int( round(int(resp['main']['temp'])) )

    @classmethod
    def w_temp_range(self):
        temp = self.w_current_temp()

        temp_min = int(temp/10) * 10
        temp_max = temp_min+10

        temp_dig = int(temp%10)

        if temp_dig <= 5:
            temp_max -= 5
        else:
            temp_min += 5

        return [temp, temp_min, temp_max]
