from flask import Flask, render_template
from sensor import measure

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api/sensor/')
def sensor():
    return measure()

@app.route('/stand/')
def stand(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')   
