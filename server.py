from distutils.log import debug
from unicodedata import name
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dojo")
def dojo():
    return "Dojo"

# @app.route("/say/<nombre>")
# def say_name1(nombre):
#     return "Hola " + nombre

@app.route("/say/<name>")
def say_name2(name):
    return render_template('index.html',nombre=str(name))       


@app.route("/repeat/<veces>/<palabra>")
def repeat_palabra(veces, palabra):
    return render_template('repeat.html', veces=int(veces), palabra=str(palabra))


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug = True)