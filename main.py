from camera_rps import camera_rps


def play_game():
    """
        Function that allows to play the RPS game through the camera_rps class.
        The function will loop until 3 turn victories are reached.
        There is no control to stop the flow, hence the turn will progress until one player reaches 3 wins.

        Parameters: - 
        Returns: - 
    """
    # initilize the number of computer and user wins to zero
    computer_wins = 0
    user_wins = 0
    # create an instance of the class camera_rps called game
    game = camera_rps()
    while True:
        # get the player choice through the camera
        player_choice = game.get_prediction()
        # get the computer choice by randomly selecting a c lass
        computer_choice = game.get_computer_choice()

        user_win, computer_win = game.get_winner(computer_choice, player_choice)

        user_wins += user_win
        computer_wins += computer_win

        # checks if one between the player and the computer has reached three turn victories,
        # otherwise continutes the loop
        if computer_wins == 3:
            print("Computer wins the game")
            break
        elif user_wins == 3:
            print("You win, congrats!")
            break
        else:
            print(f"User score: {user_wins}\nComputer score: {computer_wins}")
            print('Play another turn')

    return


play_game()
