import random
word_list = ["sarmale","spaghete","chiftele","ciorba","ciolan","macaroane","covrigi","piftie","paste","pizza","shawarma","hamburger"]
random_word = random.choice(word_list)
print(len(random_word))  
n=0
lives = 5
word=[]
end_of_game = False
word_range = len(random_word)
while n<word_range:
    word.extend("_")
    n+=1
print(word)
while not end_of_game:
    guess = input("\nGuess a letter.\n").lower()
    for position in range(word_range):
        letter = random_word[position]
        if letter == guess:
            word[position]=guess
    print(word)
    if guess not in word:
        lives -=1
    if lives == 4:
        print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif lives == 3:
        print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif lives == 2:
        print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
    elif lives == 1:
        print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif lives == 0:
        print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
    if "_" not in word:
        print("YOU WIN")
        break
    elif lives == 0:
        print("YOU ARE A LOSER")
        print(random_word)
        break
