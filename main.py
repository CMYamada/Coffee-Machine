from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
operate = True

while operate:
    drink = input("What would you like to drink?: " + Menu.get_items())
    if drink == "off":
        operate = False
    elif drink == "report":
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(drink)
        if maker.is_resource_sufficient(drink) and money.make_payment(drink):
            maker.make_coffee(drink)
