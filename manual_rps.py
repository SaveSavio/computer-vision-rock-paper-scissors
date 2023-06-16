def get_computer_choice():
    import random
    variables = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(variables)
    return computer_choice

def get_user_choice():
    variables = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Choose between rock (0), paper(1), or scissors(2)")
        if choice == '1':
            player_choice = 'rock'
        elif choice == '2':
            player_choice = 'paper'
        elif choice == '3':
            player_choice = 'scissors'
        else:
            print("Invalid choise. Please, enter 1, 2 or 3")
            return
        return player_choice
    
def get_winner(computer_choice, player_choice):
    if player_choice == computer_choice:
        print("It's a tie")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lost!")

def play():
    computer_choice = get_computer_choice()
    player_choice = get_user_choice()
    get_winner(computer_choice, player_choice)