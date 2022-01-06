# -*- coding: utf-8 -*-
from flask import Flask, render_template


# Creamos un objeto llamado app de tipo FLASK
app = Flask(__name__)

# Página raiz
@app.route('/')
def home():
    return  render_template('home.html')

# Página about
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)