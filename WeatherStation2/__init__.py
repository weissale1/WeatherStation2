from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

# a simple page that says hello
    from . import CurrentWeather
    app.register_blueprint(CurrentWeather.bp)

    return app