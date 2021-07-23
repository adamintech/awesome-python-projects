import time
import random
 
def RockPaperScissors():
    print("Welcome to the Arena!")
    user_name = input("Brave one, what is your name? ")
    print(f'{user_name.title()} is a strong name, I look forward to watching your battles!')
    opponent_weapon = ['rock','paper','scissors']
    beats = {'scissors':'paper','paper':'rock','rock':'scissors'}
    verbs = {'scissors':'slices & dices','paper':'issues a fine to','rock':'does a hulk smash on'}
    hero_weapon = input('(Type Rock, Paper, or Scissors and then press enter)').lower()
    opponent_weapon = random.choice(opponent_weapon)
    time.sleep(1)
    print('Rock')
    time.sleep(0.5)
    print('Paper')
    time.sleep(0.5)
    print('Scissors')
    time.sleep(0.5)
    print('Shoot')
    if opponent_weapon == hero_weapon:
        print('Your opponent chose ' + opponent_weapon + '. You battle all night, succuming to exhaustion. \
Fans rush the arena and kill you both!')
    elif beats[hero_weapon] == opponent_weapon:
        print(hero_weapon + ' ' + verbs[hero_weapon] + ' ' + opponent_weapon)
        print('Your opponent arrived with only ' + opponent_weapon + '. You easily win!')
    elif beats[opponent_weapon] == hero_weapon:
        print('Your wise opponent brought ' + opponent_weapon + '. You lower your head in shame for the impending doom!')
        print(opponent_weapon + ' ' + verbs[opponent_weapon] + ' ' + hero_weapon)
    play_again = input('Press enter to play again or X to end the game')
    if play_again == "":
        RockPaperScissors()
    else:
        print('Thank you for playing')
 
RockPaperScissors()