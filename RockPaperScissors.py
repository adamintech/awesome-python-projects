print(
'''*'-.-'*'-.-'*'-.-'*'--'*
    Project: Unit_04 
     Version: 5.0 
  Author: Adam Berman
 Email: uhicfii@gmail.com
  Date: July 22nd, 2021
*'-.-'*'-.-'*'-.-'*'--'*''')
print("." * 25)
print()
print()

#--------------------#

#Type in name and it'll stay through the restarts, cheat code is name: cheater which forces the computer to be rock
import random
import time

user_name = input("Greetings Warrior, what shall we call you?: ").strip().title()
while True:
    actions_array = ["rock", "paper", "scissors"]
    computer_random_choice = random.choice(actions_array)
    if user_name == "Cheater":
        computer_random_choice = "rock"
    else:
        computer_random_choice = random.choice(actions_array)
    #Fantastic, now we have a cheat code for the game. I love this already. 
    print("We're going to play a game of Rock, Paper, Scissors\n")
    user_choice = input(f"Warrior {user_name}, Which choice do you make? (rock, paper, scissors): ").strip().lower()
    print(f"\nWarrior {user_name}, You have chosen to battle with {user_choice}, enter the arena and discover your fate!\n")
    time.sleep(1)
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(0.75)
    print("Shoot!")
    #this is where things will get tedius, hopefully this caffeine works
    #Extra 1 is the first line, this was simple to figure out. If user chooses the same as computer, it doesn't matter what they chose as long as it's equal.
    if user_choice == computer_random_choice:
        message = f'Warrior, you have selected {user_choice}, it clashes with your opponent\'s {computer_random_choice}. You both live to fight another day!'
    elif user_choice == "rock":
        if computer_random_choice == "scissors":
            message = f'Warrior, you have selected the mighty Rock! it smashes your opponents scissors. You win!'
        else:
            message = f'Warrior, you throw your mighty rock at your opponent! Unfortunately, they hide behind the paperwork of buraucracy and fine you $100. You lose!'
    elif user_choice == "paper":
        if computer_random_choice == "rock":
            message = f'Warrior, you dispicably chose to use paper in a fight. Sadly, this has resulted in victory over the mighty rock of your opponent. You win, but did you?'
        else: 
            message = f'Warrior, you foolishly pitted paper against a tailor with scissors. You lose, hang your head in shame!'
    elif user_choice == "scissors":
        if computer_random_choice == "paper":
            message = f'Warrior, you have taken to the art of tailoring and used your scissors to defeat your opponent\'s paper. Congratulations!'
        else:
            message = f'Warrior, your choice of tradesperson\'s tool of a pair of scissors has failed you. Your opponent had a rock, afterall. You lose!'
    print(message)

    restart = input("Press enter to play again or X to end the game: ")
    if restart != "":
        break
print("Thank you for playing.")