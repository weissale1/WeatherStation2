from flask import Blueprint
from datetime import datetime

from .domain.WeatherData import WeatherData

bp = Blueprint('current_weather', __name__, url_prefix='/current')

@bp.route("/")
def index():
    return CurrentWeather.getCurrentWeather()

class CurrentWeather:
    def getCurrentWeather() -> dict:
        w = CurrentWeather._loadCurrentWeatherData()
        return CurrentWeather._formatWeatherDataToJson(w)
    
    def _loadCurrentWeatherData() -> WeatherData:
        return WeatherData(datetime.now(), 20.0, 40.0)
    
    def _formatWeatherDataToJson(wd: WeatherData) -> dict:
        return {
            'timestamp': wd.timestamp.isoformat(timespec="seconds"),
            'temp': wd.temp,
            'humid': wd.humid
        }