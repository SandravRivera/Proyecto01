from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True)