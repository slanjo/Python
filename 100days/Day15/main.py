from os import system
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
#    "water": 40,
#    "milk": 200,
    "coffee": 100,
    "milk": 0,
}


def drink():
    report()


def report_not_enough_resource(ingredient):
    print(f"Sorry there is not enough {ingredient}")


def report():
    print(resources)


def check_resources(choice):
    for resource in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][resource] > resources[resource]:
            print(f'{report_not_enough_resource(MENU[choice]["ingredients"][resource])}')
            print(f'{report_not_enough_resource(resource)}')

def process_request(choice):
    if choice == "latte":
        price = 2.5
        check_resources("latte")
    elif choice == "cappuccino":
        price = 3.0
        print("cappuccino")
    elif choice == "espresso":
        price = 2.0
        print("espresso")


machine_on = True


while machine_on:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "off":
        machine_on = False
    elif selection == "report":
        report()
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        process_request(selection)
