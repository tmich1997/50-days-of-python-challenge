# Day 50 Create a Flask App

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", endpoint='home')
def home():
    return render_template('home.html')

@app.route("/about", endpoint='about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

