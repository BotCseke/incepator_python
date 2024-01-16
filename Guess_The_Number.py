logo = """   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
                                                                                          """
import random

number_calculator = random.randint(0,101)

def play_game():
    number = int(input("Guess a number: "))
    while number != number_calculator:
        if number > number_calculator:
            print(f"{number} is to big")
            number = int(input("Guess a number: "))
        elif number < number_calculator:
            print(f"{number} is to low")
            number = int(input("Guess a number: "))
    print(f"YOU WON\nThe number was {number_calculator}")

print(logo)
q = input("Do you wanna play ? press 'y' for yes and 'n' for no:\n ")
if q =='y':
    play_game()