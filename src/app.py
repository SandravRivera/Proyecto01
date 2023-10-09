from flask import Flask, render_template, request
from methods import start, search_name_city, search_ticket

app = Flask(__name__)

@app.route('/')
def home():
    """Create the home page.

    Returns:
        string: render the home template.
    """
    return render_template('home.html')

@app.route('/city_search/')
def city():
    """Create the page to search the weather by city and IATA code.

    Returns:
        string: render the city_search template.
    """
    return render_template('city_search.html', data = {"mensaje" : ""})

@app.route('/ticket_search/')
def ticket():
    """Create the page to search the weather by ticket.
    Returns:
        string: render the ticket_search template.
    """
    return render_template('ticket_search.html', data = {"mensaje" : ""})

@app.route('/city_weather', methods=['POST'])
def city_weather():
    """Create the page with the result of searching by city.

    Returns:
        string: render a template with the weather for city found.
        string: render a template with error message for city not found.
    """
    city_name = request.form['city-name-input']
    data = search_name_city(city_name)
    if data is not None:
        return render_template('city_weather.html', data=data)
    else:
        return render_template('city_search.html', data={"mensaje" : "City not found, try again."})

@app.route('/ticket_weather', methods=['POST'])
def ticket_weather():
    """Create the page with the result of searching by ticket.

    Returns:
        string: render a template with the weathers for ticket found.
        string: render a template with error message for ticket not found.
    """
    ticket = request.form['ticket-input']
    data = search_ticket(ticket)
    if data is not None:
        return render_template('ticket_weather.html', data=data)
    else:
        return render_template('ticket_search.html', data={"mensaje" : "Ticket not found, try again."})

if __name__ == '__main__':
    start()
    app.run(debug=True)
