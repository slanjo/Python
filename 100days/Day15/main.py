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
    "milk": 200,
    "coffee": 100,
#    "milk": 0,
}
profit = 0


def drink():
    report()


def report_not_enough_resource(ingredient):
    print(f"Sorry there is not enough {ingredient}")


def report(stanje, money):
    for i in stanje:
        print(f"{i}: {stanje[i]}")
    print(f"Money: ${money}")


def check_resources(choice):
    for resource in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][resource] > resources[resource]:
            print(f'{report_not_enough_resource(resource)}')
            return -1
        else:
            resources[resource] -= MENU[choice]["ingredients"][resource]
    return resources[resource]


def process_coins(cost):
    print("Please insert coins.")
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickels = 0.05 * int(input("How many nickles?: "))
    pennies = 0.01 * int(input("How many pennies?: "))
    total = quarters + dimes + nickels + pennies
    if total > cost:
        print(f"Here is ${total - cost} in change.")
        return cost
    elif total == cost:
        print("No change this transaction")
        return cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def process_request(choice):

    if choice == "latte":
        resource_check = check_resources("latte")
    elif choice == "cappuccino":
        resource_check = check_resources("cappuccino")
    elif choice == "espresso":
        resource_check = check_resources("espresso")
    if resource_check != -1:
        test = process_coins(MENU[choice]["cost"])
        return test
    else:
        return -1

#   TODO insert a call to remove required resources from resources dict


machine_on = True
transaction_profit = 0
while machine_on:

    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "off":
        machine_on = False
    elif selection == "report":
        report(resources, profit)
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        transaction_profit = process_request(selection)
        if transaction_profit != -1:
            print(f"Here is your {selection}")
            profit += transaction_profit

