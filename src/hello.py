from flask import Flask, render_template, request
from methods import start, searchWeatherWith_NameOfCity, searchWeatherWith_ticket

app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/city.html/')
def city():
    return render_template('city_search.html', data = {"mensaje" : ""})

@app.route('/ticket.html/')
def ticket():
    return render_template('ticket_search.html', data = {"mensaje" : ""})

@app.route('/city_weather', methods=['POST'])
def city_weather():
    city_name = request.form['city-name-input']
    data = searchWeatherWith_NameOfCity(city_name)
    if data is not None:
        return render_template('city_weather.html', data=data)
    else:
        return render_template('city_search.html', data={"mensaje" : "Ciudad no encontrada, intente de nuevo"})

@app.route('/ticket_weather', methods=['POST'])
def ticket_weather():
    ticket = request.form['ticket-input']
    data = searchWeatherWith_ticket(ticket)
    if data is not None:
        return render_template('ticket_weather.html', data=data)
    else:
        return render_template('ticket_search.html', data={"mensaje" : "Ticket no encontrado, intente de nuevo"})

if __name__ == '__main__':
    start()
    app.run(debug=True)
