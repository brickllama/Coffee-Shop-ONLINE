from flask import Flask, render_template

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
    return render_template("hotdrinks.html")


@app.route('/drinks/cold')
def colddrinks():
    return render_template("colddrinks.html")


@app.route('/food')
def food():
    return render_template("food.html")


@app.route('/merchandise')
def merch():
    return render_template("merchandise.html")



@app.route('/checkout')
def checkout():
    return render_template("checkout.html")


if __name__ == '__main__':
    app.run(debug=True)
