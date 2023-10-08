from flask import Flask, render_template, request, jsonify
from methods import start, searchWeatherWith_NameOfCity

app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    start()  # Asegúrate de llamar a la función start para cargar los datos
    return render_template('home.html')

@app.route('/city.html/')
def city():
    data = {"mensaje" : ""}
    return render_template('city_search.html', data=data)

@app.route('/ticket.html/')
def ticket():
    return render_template('ticket.html')

@app.route('/buscar_ciudad', methods=['POST'])
def buscar_ciudad():
    city_name = request.form['city-name-input']
    data = searchWeatherWith_NameOfCity(city_name)
    if data is not None:
        return render_template('city_weather.html', data=data)
    else:
        data = {"mensaje" : "Ciudad no encontrada, intente de nuevo"}
        return render_template('city_search.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
