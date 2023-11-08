import random as rd
from datetime import datetime


class Menu:
    blurred_card: str = ''
    payment_network: str = ''
    date: str = ''
    time: str = ''
    business = "Nate's Coffee Shop"
    # date and time
    date = datetime.today()
    date = date.strftime("%m/%d/%y")
    time = datetime.now()
    time = time.strftime("%H:%M")

    # card details
    digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    payment_network = ['VISA', 'MasterCard', 'AMEX', 'Discover']
    credit_card = ''
    for d in range(16):
        credit_card += str(rd.choice(digit))
    blurred_card = f"{'X' * 4} {'X' * 4} {'X' * 4} {credit_card[12:16]}"
    payment_network = rd.choice(payment_network)

    hot_coffees = [
        ('Americano', 3.95),
        ('Brewed Coffee', 2.95),
        ('Cappuccino', 4.95),
        ('Espresso', 2.75),
        ('Latte', 3.45),
        ('Macchiato', 2.85),
        ('Mocha', 5.45)
    ]
    teas = [
        ('Black Tea', 3.45),
        ('Earl Grey', 3.45),
        ('Peppermint Tea', 3.45),
        ('Chai Tea', 3.45),
        ('Matcha Tea Latte', 5.25)
    ]
    cold_coffees = [
        ('Cold Brew', 4.45),
        ('Iced Americano', 3.95),
        ('Iced Coffee', 3.95),
        ('Iced Shaken Espresso', 4.45),
        ('Iced Latte', 4.95),
        ('Iced Macchiato', 5.65),
        ('Iced Mocha', 5.65)
    ]
    seasonal_beverages = [
         'Christmas Drink or something'
    ]
    foods = [
        ('Bagel', 2.65),
        ('Everything Bagel', 2.65),
        ('Cream Cheese', 0.95),
    ]
    merchandise = [
        ('Sloth T-shirt', 15.00),
        ('Reusable Cup', 5.00),
        ('4pk Metal Straws', 4.25),
        ('Sloth Plushie', 25.00)
    ]
    shopping_cart = []

    def select_items(prompt, options):
        for i, (name, price) in enumerate(options):
            print(f'{i + 1}\t{name:<20} ${price:.2f}')
        print('P to checkout. ')
        choice = input(f'Which {prompt} would you like? ')
        try:
            choice = int(choice) - 1
            if choice + 1 <= len(options):
                Menu.shopping_cart.append(options[choice])
                for i in Menu.shopping_cart:
                    print(f"{i[0]:<28} ${i[1]:.2f}")
        except ValueError:
            if 'p' in choice.lower():
                return False
            print('It has to be a number')

    def payments(shopping_cart):
        choice = int(input('Are you ready to checkout?\n'
                           + '1) Yes\n2) No\nChoice: '))
        try:
            if choice == 1:
                if len(shopping_cart) >= 1:
                    subtotal = 0
                    for i in shopping_cart:
                        subtotal += i[1]
                    tax = 0.1125 * subtotal  # 11.25%
                    grand_total = subtotal + tax
                    print('\n', Menu.business.center(31) + '\n')
                    for name, price in shopping_cart:
                        print(f'{name:<25} ${price:.2f}')
                    print(f"{'**'*16}\n{'Subtotal':<25} ${subtotal:.2f}")
                    print(f"{'Tax':<25} ${tax:.2f}")
                    print(f"{'Total':<25} ${grand_total:.2f}\n{'**'*16}")
                    print(f"{Menu.blurred_card:<20} {Menu.payment_network}")
                    print(f"APPROVED - PURCHASE\nAMOUNT: ${grand_total:.2f}")
                    print(f"{Menu.date:<26} {Menu.time}\n{'**'*16}")
                    exit()
                else:
                    exit()
        except ValueError:
            print('It must be')

    def menu():
        try:
            answer = int(input('1) Drinks\n2) Food\n3)'
                               ' Merchandise\n4) Cart\nChoice: '))
            if answer == 1:
                try:
                    answer = int(input('1) Hot Beverages\n2)'
                                       + ' Cold Beverages\nChoice: '))
                    if answer == 1:
                        print('Our hot beverages are:')
                        if Menu.select_items('hot beverage', Menu.hot_coffees
                                             + Menu.teas) is False:
                            return Menu.payments(Menu.shopping_cart)
                    elif answer == 2:
                        print('Our cold beverages are:')
                        if Menu.select_items('cold beverage',
                                             Menu.cold_coffees) is False:
                            return Menu.payments(Menu.shopping_cart)
                    else:
                        print('You must choose between 1 and 2')
                except ValueError:
                    print('You must enter a number!')
            elif answer == 2:
                print('Our food items are:')
                if Menu.select_items('food item', Menu.foods) is False:
                    return Menu.payments(Menu.shopping_cart)
            elif answer == 3:
                if Menu.select_items('merchandise', Menu.merchandise) is False:
                    return Menu.payments(Menu.shopping_cart)
            elif answer == 4:
                Menu.payments(Menu.shopping_cart)
            else:
                print('You must enter a value between 1 and 4!')
        except ValueError:
            print('You must enter a number!')

        Menu.menu()
