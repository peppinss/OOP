import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
if __name__ == "__main__":
    print("Welcome to the coffee machine")
    while True:
        print("What you wanna order?")
        getmenu = Menu()
        getmoney = MoneyMachine()
        makecoffe = CoffeeMaker()
        print(getmenu.get_items())
        choice = input()
        if choice == "off":
            print("Shutdown")
            break
        elif choice == "report":
            makecoffe.report()
            getmoney.report()
        else:
            avable = getmenu.find_drink(choice)
            if avable != None:
                if makecoffe.is_resource_sufficient(avable) and getmoney.make_payment(avable.cost):
                        makecoffe.make_coffee(avable)