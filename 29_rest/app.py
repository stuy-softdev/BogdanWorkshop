from flask import Flask
from flask import render_template
import urllib.request

app = Flask(__name__)

@app.route("/")
def index():
    with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=Skfn9O6Ye7xT9ELLDiU33KX9HMhAV9VrELpOElEy') as response:
        return render_template('main.html', image=response.read().get('hdurl'))

    
if __name__ == "__main__":
    app.run(debug=True, port=8008)