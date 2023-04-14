import random

MODE_PLAYER_VS_PLAYER = 1
MODE_PLAYER_VS_BOT = 2
MODE_BOT_VS_BOT = 3

CHOICES = ['rock', 'paper', 'scissors']

scoreboard = {'Player 1': {'wins': 0, 'draws': 0, 'losses': 0},
              'Player 2': {'wins': 0, 'draws': 0, 'losses': 0}}


def get_player_choice():
    while True:
        print("Enter your choice (rock, paper, scissors):")
        choice = input().lower()
        if choice in CHOICES:
            return choice
        else:
            print("Invalid choice. Please try again.")


def get_bot_choice():
    return random.choice(CHOICES)


def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 'draw'
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
            (player1_choice == 'paper' and player2_choice == 'rock') or \
            (player1_choice == 'scissors' and player2_choice == 'paper'):
        return 'Player 1'
    else:
        return 'Player 2'


def display_scoreboard():
    print("\nScoreboard")
    print("Player 1: Wins - {}, Draws - {}, Losses - {}".format(scoreboard['Player 1']['wins'],
                                                                scoreboard['Player 1']['draws'],
                                                                scoreboard['Player 1']['losses']))
    print("Player 2: Wins - {}, Draws - {}, Losses - {}".format(scoreboard['Player 2']['wins'],
                                                                scoreboard['Player 2']['draws'],
                                                                scoreboard['Player 2']['losses']))


def reset_scoreboard():
    scoreboard['Player 1']['wins'] = 0
    scoreboard['Player 1']['draws'] = 0
    scoreboard['Player 1']['losses'] = 0
    scoreboard['Player 2']['wins'] = 0
    scoreboard['Player 2']['draws'] = 0
    scoreboard['Player 2']['losses'] = 0


def play_game():
    while True:
        print("\nSelect game mode:")
        print("1. Player vs Player")
        print("2. Player vs Bot")
        print("3. Bot vs Bot")
        print("4. Quit")
        mode = input()

        if mode == '1':  # Player vs Player
            print("\nPlayer 1:")
            player1_choice = get_player_choice()
            print("\nPlayer 2:")
            player2_choice = get_player_choice()

        elif mode == '2':  # Player vs Bot
            print("\nPlayer 1:")
            player1_choice = get_player_choice()
            player2_choice = get_bot_choice()
            print("Player 2 chooses: " + player2_choice)

        elif mode == '3':  # Bot vs Bot
            player1_choice = get_bot_choice()
            player2_choice = get_bot_choice()
            print("Player 1 chooses: " + player1_choice)
            print("Player 2 chooses: " + player2_choice)

        elif mode == '4':  # Quit
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please try again.")
            continue

        winner = determine_winner(player1_choice, player2_choice)

        if winner == 'draw':
            print("It's a draw!")
            scoreboard['Player 1']['draws']
        elif winner == 'Player 1':
            print("Player 1 wins!")
            scoreboard['Player 1']['wins'] += 1
            scoreboard['Player 2']['losses'] += 1
        else:
            print("Player 2 wins!")
            scoreboard['Player 1']['losses'] += 1
            scoreboard['Player 2']['wins'] += 1

        display_scoreboard()

        # Check if any player has reached 3 wins
        if scoreboard['Player 1']['wins'] == 3 or scoreboard['Player 2']['wins'] == 3:
            print("Game over!")
            if scoreboard['Player 1']['wins'] == 3:
                print("Player 1 wins the game!")
            else:
                print("Player 2 wins the game!")
            reset_scoreboard()
            continue

        # Ask if the player wants to play another round
        print("\nDo you want to play another round? (yes/no)")
        play_again = input().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break


if __name__ == '__main__':
    play_game()
