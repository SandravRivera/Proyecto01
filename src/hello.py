from flask import Flask, render_template, request, jsonify
import requests
from methods import start, searchWeatherWith_NameOfCity 

app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/city.html/')
def city():
    return render_template('city.html')

@app.route('/ticket.html/')
def ticket():
    return render_template('ticket.html')

@app.route('/buscar_ciudad')
def search_weather_by_city_name():
    city_name = request.args.get('city')
    weather_data = searchWeatherWith_NameOfCity(city_name) 
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
