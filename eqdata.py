import os

from datetime import datetime, timezone, timedelta
from pyshorteners import Shortener

class EQData():
    def __init__(self, input):
        self.input = input
        self.properties = self.input['properties']
        self.geometry = self.input['geometry']

        self.coordinates = self.geometry['coordinates']
        self.magnitude = self.properties['mag']
        self.place = self.properties['place']
        self.time = self.properties['time']
        self.url = self.properties['url']

        self.lon, self.lat, self.depth = self.coordinates

    def map_url(self):
        """Returns Google Map URL of given coordinates"""
        lon, lat, _ = self.coordinates()
        url = "http://www.google.com/maps/place/%s,%s" % (lat,lon)
        return url

    def minutes_ago(self):
        """Returns minutes since event"""
        d0 = datetime.fromtimestamp(self.time/1000, tz=timezone(timedelta(hours=8)))
        d1 = datetime.now(tz=timezone(timedelta(hours=8)))
        delta = d1-d0
        return int(delta.total_seconds()/60)

    def ftime(self):
        """Returns formatted time"""
        time = datetime.fromtimestamp(self.time/1000, tz=timezone(timedelta(hours=8)))
        return time.strftime("%I:%M%p")

    def url_shorten(self):
        # shortener = Shortener('Tinyurl')
        shortener = Shortener('Google', api_key=os.environ['API_KEY'])
        return shortener.short(self.url)

    def to_sentence(self):
        """Makes the ugly json readable"""
        sentence = "A magnitude %s earthquake hits %s at %s UTC+8 (%sm ago) - Details %s #earthquakePH" \
        % (self.magnitude, self.place, self.ftime(), self.minutes_ago(), self.url_shorten())

        if len(sentence) > 140:
            sentence = sentence.replace("Philippines", "PH")
        return sentence