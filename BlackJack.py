import random
import math
logo = """
.------.            _     _            _    _            _    
|A_  _ |           | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def compara(score_user,score_computer):
    if score_user>21 and score_computer>21:
        return "You go to much, YOU LOST"
    if score_computer==score_user:
        return "Equal"
    elif score_computer == 0:
        return "YOU LOST"
    elif score_user == 0:
        return "YOU WON"
    elif score_computer>21:
        return "Your opponent go to far, YOU WON"
    elif score_user>21:
        return "You go to far, YOU LOST"
    elif score_user>score_computer:
        return "YOU WON"
    else:
        return "YOU LOST"
def random_card():
    values = ['2','3','4','5','6','7','8','9','10','10','10','10','11']
    #suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    value = random.choice(values)
    #suite = random.choice(suites)
    return value   
def calc_score(cards):
    cards = [ int(x) for x in cards ]
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():
    print(logo)
    cards_user = []
    cards_computer = []
    joc_end = False

    for i in range(2):
        cards_user.append(random_card())
        cards_computer.append(random_card())

    

    while not joc_end:
        score_user = calc_score(cards_user)
        score_computer = calc_score(cards_computer) 
        print(f"Your cards {cards_user}, current score: {score_user}")
        print(f"Computer cards {cards_computer[0]}")
        
        if score_user == 0 or score_computer == 0 or score_user>21:
            joc_end = True
        else:
            mesaj = "Press 'y' for another card, or 'n' to stop: "
            bet_user = input(mesaj)
            if bet_user == 'y':
                 cards_user.append(random_card())
            else:
                joc_end = True
    while score_computer != 0  and score_computer < 17:
        cards_computer.append(random_card())
        score_computer = calc_score(cards_computer)
    print(f"Your final hand: {cards_user}, final score: {score_user}")
    print(f"Computer final hand: {cards_computer}, final score: {score_computer}")
    print(compara(score_user, score_computer))

        



start = "Do you want to play BlackJack ? Press 'y' if you want to play and 'n' if you don't want to play\n"
while(input(start))=='y':
    play_game()
   