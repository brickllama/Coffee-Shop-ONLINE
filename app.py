from flask import Flask, render_template
from Menu import Menu

app = Flask(__name__)


@app.route('/')
def home():
    name = 'Nate'
    return render_template("index.html", name=name)


@app.route('/drinks')
def drinks():
    return render_template("drinks.html")


@app.route('/drinks/hot')
def hotdrinks():
    options = Menu.hot_coffees + Menu.teas
    return render_template("hotdrinks.html", options=options)


@app.route('/drinks/cold')
def colddrinks():
    options = Menu.cold_coffees
    return render_template("colddrinks.html", options=options)


@app.route('/food')
def food():
    options = Menu.foods
    return render_template("food.html", options=options)


@app.route('/merchandise')
def merch():
    options = Menu.merchandise
    return render_template("merchandise.html", options=options)



@app.route('/checkout')
def checkout():
    return render_template("checkout.html")


if __name__ == '__main__':
    app.run(debug=True)
