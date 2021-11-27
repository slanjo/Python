from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
#izvjestaj = novac_masina.report()
is_on = True


while is_on:
    #prompt user "What would you like? (espresso/latte/cappuccino/):"
    item_list = menu.get_items()
    choice = input(print(f"What would you like ({item_list}): ")) 

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report() 
    else:

        choice_instance = menu.find_drink(choice) 
        if coffe_maker.is_resource_sufficient(choice_instance):
            if money_machine.make_payment(choice_instance.cost):
                coffe_maker.make_coffee(choice_instance)
