MENU = {
    "espresso": {
        "ingredients": {
            "apa": 50,
            "cafea": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "apa": 200,
            "lapte": 150,
            "cafea": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "apa": 250,
            "lapte": 100,
            "cafea": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "apa": 300,
    "lapte": 200,
    "cafea": 100,
}
def is_enough_money(money_received, drink_cost):
    global profit
    if money_received>=drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is your rest {change}")
        profit += drink_cost
        return True
    else:
        print("Not enough money, your money doesn't return hahaha")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}☕")
def money():
    print("Please insert the coins")
    total = int(input("how much coins of 25 do you want to put? "))*0.25
    total+= int(input("how much coins of 10 do you want to put? "))*0.10
    total+= int(input("how much coins of 5 do you want to put? "))*0.05
    total+= int(input("how much coins of 1 do you want to put? "))*0.01
    return total
def is_resources_s(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item]>=resources[item]:
           print(f"Sorry we dont have enough {item}")
           return False
    return True
is_on = True
while is_on:
    choice = input("What do you want to order ?(espresso\latte\cappuccino)\n")
    if choice =="off":
        print("The coffee machine is off")
        break
    elif choice == "report":
        print(resources, profit)
    else:
        drink = MENU[choice]
        print(drink) 
        if is_resources_s(drink["ingredients"]):
            payment = money()
        if is_enough_money(payment,drink["cost"]):
            make_coffee(choice, drink["ingredients"])
            
        

