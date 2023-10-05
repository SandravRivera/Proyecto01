from flask import Flask, render_template, request, jsonify
import requests
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

# Ruta para buscar datos climáticos por nombre de ciudad
@app.route('/buscar_ciudad')
def searchWeatherWith_NameOfCity():
    city_name = request.args.get('city')  # Obtener el nombre de la ciudad desde la solicitud
    weather_data = get_weather_by_city_name(city_name)  # Llamar a la función para obtener el clima
    return jsonify(weather_data)

# Función para obtener datos climáticos de OpenWeather API
def get_weather_by_city_name(city_name):
    api_key = "&appid=155505a47faf9082a7ee3d45f7b1ea0b&units=metric"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        weather_data = {
            "name": data['name'],
            "temp": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "wind": data['wind']['speed']
        }

        return weather_data

    except Exception as e:
        print("Error al obtener datos climáticos:", e)
        return {"error": "No se pudo obtener la información del clima"}

if __name__ == '__main__':
    app.run(debug=True)