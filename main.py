import random

def welcome():
    print(r"""
 __        __   _                            _         
 \ \      / /| | ___ ___  _ __ ___   ___  | |_ ___   
  \ \ /\ / / _ \ |/ _/ _ \| ' ` _ \ / _ \ | __/ _ \  
   \ V  V /  _/ | (| () | | | | | |  __/ | || () | 
    \/\/ \||\\/|| || ||\|  \\_/  
                                                      
        Welcome to Rock, Paper, Scissors!
    """)

rock = """
    _______
---'   ____)
      (___)
      (___)
      (__)
---.(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.(___)
"""

options = [rock, paper, scissors]
win = None
userscore = 0
# computer_score = 0
def choose_option():
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
        if user_choice >= 3 or user_choice < 0:
            print("Invalid choice! You lose.")
            return None
        print(f"\nYou chose:\n{options[user_choice]}")
        return user_choice
    except ValueError:
        print("That's not a number! You lose.")
        return None

def decide_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 0 and computer == 2) or \
         (user == 1 and computer == 0) or \
         (user == 2 and computer == 1):
        return "You win!" ,win== True
    else:
        return "You lose!", win== False
    

def score(result):
            if win is True:
                userscore += 1
                print(f"Your score is: {score}")
            # elif result is False:
            #     computer_score += 1
            #     print(f"Computer's score is: {computer_score}")

def play_game():
    welcome()
    while True:
        user_choice = choose_option()
        if user_choice is not None:
            computer_choice = random.randint(0, 2)
            print(f"\nComputer chose:\n{options[computer_choice]}")
            result = decide_winner(user_choice, computer_choice)
            print(f"\n{result}")
            print(f'{score(result[1])} {win}')
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye. 👋")
            break
play_game()
