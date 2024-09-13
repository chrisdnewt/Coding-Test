import random

def get_game_type():
    # Choose game type
    game = int(input("What Game Would You Like to Play?\n Simple [0], Repeat Previous Move [1], or Rock Paper Scissors Lizard Spock [2]  "))

    while game not in [0,1,2]:
        game = int(input("Not a recognised game type, please enter 0, 1, or 2 for Simple [0], Repeat Previous Move [1], or Rock Paper Scissors Lizard Spock [2] "))
    
    # Define choices if playing rock paper scissors
    if game in [0,1]:
        choices = ['Rock', 'Paper', 'Scissors']
    # Define choices if playing rock paper scissors lizard spock
    elif game == 2:
        choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    return choices, game

def get_player_choice(choices):
    player_prompt = "Make your choice from " + ", ".join(choices) + ": "
    player_choice = input(player_prompt).lower() # get player choice and change to lowercase
    choices_lc = [x.lower() for x in choices] # convert all choices to lowercase
    while player_choice not in choices_lc: # make sure player choice is legal
        player_prompt = "Not a recognised choice, please choose from: " + ", ".join(choices) + " "
        player_choice = input(player_prompt).lower()
    return player_choice

def get_computer_choice(choices):
    computer_choice = choices[random.randint(0, len(choices)-1)]
    print("The Computer Chose", computer_choice)
    return computer_choice.lower()

def decide_winner(choice1, choice2): # find winner
    # define which elements each choice beats
    matchup_dict = {
        'rock':     ['scissors', 'lizard'],
        'paper':    ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard':   ['paper', 'spock'],
        'spock':    ['rock', 'scissors']
    }

    if choice1 == choice2:
        result = 0 # tie
    elif choice2 in matchup_dict[choice1]:
        result = 1 # choice1 wins
    else:
        result = 2 # choice1 loses
    return result

def play_game(prev_choice=False):
    player_choice = get_player_choice(choices)
    if not prev_choice:
        computer_choice = get_computer_choice(choices)
    else:
        computer_choice = prev_choice
        print("The Computer Chose", computer_choice)
    result = decide_winner(player_choice, computer_choice)
    result_messages = ['Tie! Would you like to play again? [y/n] ', 'You Won! Would you like to play again? [y/n] ', 'You Lost. Would you like to play again? [y/n] ']
    repeat = input(result_messages[result]).lower()
    while repeat not in ['y', 'n', 'yes', 'no']:
        repeat = input('Answer not recognised. Please enter y if you would like to continue playing, n if you would not. ').lower()
    return repeat, player_choice

choices, game = get_game_type()
repeat, prev_choice = play_game()
while repeat in ['y', 'yes']:
    if game == 1:
        repeat, prev_choice = play_game(prev_choice)
    else:
        repeat, prev_choice = play_game()
print('Thanks for playing')
