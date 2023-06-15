def get_computer_choice():
    import random
    variables = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(variables)
    return computer_choice

computer_choice = get_computer_choice()
print(computer_choice)

def get_user_choice():
    variables = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Choose between rock (0), paper(1), or scissors(2)")
        if choice == '0':
            player_choice = 'rock'
        elif choice == '1':
            player_choice = 'paper'
        elif choice == '2':
            player_choice = 'scissors'
        else:
            print("Invalid choise. Please, enter 0, 1 or 2")
            return
        return player_choice

player_choice = get_user_choice()
print(player_choice)