from flask import Flask, render_template, session, request
from Menu import Menu

app = Flask(__name__)
app.secret_key = 'pineapple'


@app.route('/')
def home():
    name = 'Nate'
    date = Menu.date
    return render_template("index.html", name=name, date=date)


@app.route('/drinks')
def drinks():
    return render_template("drinks.html")


@app.route('/drinks/hot')
def hotdrinks():
    options = [i for i in Menu.items if i[1] == Menu.category['hot_coffee'] or i[1] == Menu.category['teas']]
    return render_template("hotdrinks.html", options=options)


@app.route('/drinks/cold')
def colddrinks():
    options = [i for i in Menu.items if i[1] == Menu.category['cold_coffee']]
    return render_template("colddrinks.html", options=options)


@app.route('/food')
def food():
    options = [i for i in Menu.items if i[1] == Menu.category['food']]
    return render_template("food.html", options=options)


@app.route('/merchandise')
def merch():
    options = [i for i in Menu.items if i[1] == Menu.category['merch']]
    return render_template("merchandise.html", options=options)


@app.route('/checkout')
def checkout():
    date = Menu.date
    time = Menu.time
    card = Menu.blurred_card
    payment_network = Menu.payment_network
    items = [i for i in Menu.items if str(i[0]) in session['cart'] ]
    return render_template("checkout.html", items=items, date=date,
                           time=time, card=card,
                           payment_network=payment_network)


@app.route('/addcart', methods=['GET', 'POST'])
def addcart():
    if 'cart' not in session:
        session['cart'] = []
    session['cart'] += request.values.getlist('items')
    items = [i for i in Menu.items if str(i[0]) in session['cart'] ]
    print(session['cart'])
    return render_template("cart.html", items=items)


@app.route('/emptycart')
def emptycart():
    session['cart'] = []
    return render_template("cart.html", items=session['cart'])


if __name__ == '__main__':
    app.run(debug=True)
