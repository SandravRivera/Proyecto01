from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pagina1.html/')
def pag1():
    return render_template('pagina1.html')

@app.route('/pagina2.html/')
def pag2():
    return render_template('pagina2.html')

if __name__ == '__main__':
    app.run(debug=True)