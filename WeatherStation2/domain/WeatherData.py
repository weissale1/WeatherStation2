import json

class WeatherData:
    def __init__(self, timestamp, temp, humid):
            self.timestamp = timestamp
            self.temp = temp
            self.humid = humid

    def toJson(self):
          return json.dumps(self)