from flask import Flask, render_template, request, jsonify
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
#    return render_template('city.html')
    return render_template('prueba.html')

@app.route('/ticket.html/')
def ticket():
    return render_template('ticket.html')

"""@app.route('/buscar_ciudad', methods=['POST'])
def search_weather_by_city_name():
    city_name = request.form['city-name-input']
    weather_data = searchWeatherWith_NameOfCity(city_name)
    print(city_name)
    print(weather_data)
    if weather_data is not None:
        return jsonify(weather_data)
    else:
        return jsonify({"error": "City not found"}), 404"""

@app.route('/buscar_ciudad', methods=['POST'])
def buscar_ciudad():
    city_name = request.form['city-name-input']
#    data = searchWeatherWith_NameOfCity(city_name)
    data = {
        "name": city_name,
        "weather": 'weather["weather"]',
        "temp": 'weather["temp"]',
        "humidity": 'weather["humidity"]'
    }
    return render_template('prueba1.html', data=data)


if __name__ == '__main__':
#    start()  # Asegúrate de llamar a la función start para cargar los datos
    app.run(debug=True)
