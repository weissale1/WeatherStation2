from flask import Blueprint

from .domain.WeatherData import WeatherData
from .db import loadCurrentWeatherData

bp = Blueprint('current_weather', __name__, url_prefix='/current')

@bp.route("/")
def index():
    return CurrentWeather.getCurrentWeather()

class CurrentWeather:
    def getCurrentWeather() -> dict:
        wd: WeatherData = loadCurrentWeatherData()
        return wd.toJson()
 