#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

enum class Choice { ROCK, PAPER, SCISSORS };

// Function to convert choice from int to enum
Choice intToChoice(int choiceInt) {
    switch (choiceInt) {
        case 0:
            return Choice::ROCK;
        case 1:
            return Choice::PAPER;
        case 2:
            return Choice::SCISSORS;
        default:
            return Choice::ROCK;
    }
}

// Function to print enum choice as string
string choiceToString(Choice choice) {
    switch (choice) {
        case Choice::ROCK:
            return "Rock";
        case Choice::PAPER:
            return "Paper";
        case Choice::SCISSORS:
            return "Scissors";
        default:
            return "Unknown";
    }
}

// Function to get player's choice
Choice getPlayerChoice() {
    int choiceInt;
    cout << "Enter your choice (0 - Rock, 1 - Paper, 2 - Scissors): ";
    cin >> choiceInt;
    return intToChoice(choiceInt);
}

// Function to get bot's choice
Choice getBotChoice() {
    int choiceInt = rand() % 3;
    return intToChoice(choiceInt);
}

// Function to determine the winner
int determineWinner(Choice playerChoice, Choice botChoice) {
    if (playerChoice == botChoice) {
        return 0;  // Draw
    } else if ((playerChoice == Choice::ROCK && botChoice == Choice::SCISSORS) ||
               (playerChoice == Choice::PAPER && botChoice == Choice::ROCK) ||
               (playerChoice == Choice::SCISSORS && botChoice == Choice::PAPER)) {
        return 1;  // Player wins
    } else {
        return 2;  // Bot wins
    }
}

int main() {
    // Seed the random number generator
    srand(time(0));

    int gameMode;
    cout << "Welcome to Rock-Paper-Scissors game!" << endl;
    cout << "Select a game mode (1 - Player vs Player, 2 - Player vs Bot, 3 - Bot vs Bot): ";
    cin >> gameMode;

    Choice player1Choice, player2Choice;
    int winner;

    switch (gameMode) {
        case 1:
            // Player vs Player mode
            player1Choice = getPlayerChoice();
            player2Choice = getPlayerChoice();
            winner = determineWinner(player1Choice, player2Choice);
            break;
        case 2:
            // Player vs Bot mode
            player1Choice = getPlayerChoice();
            player2Choice = getBotChoice();
            winner = determineWinner(player1Choice, player2Choice);
            break;
        case 3:
            // Bot vs Bot mode
            player1Choice = getBotChoice();
            player2Choice = getBotChoice();
            winner = determineWinner(player1Choice, player2Choice);
            break;
        default:
            cout << "Invalid game mode. Exiting..." << endl;
            return 0;
    }

    // Print the results
    cout << "Player 1 choice: " << choiceToString(player1Choice) << endl;
    cout << "Player 2 choice: " << choiceToString(player2Choice) << endl;
    if (winner == 0) {
        cout << "It's a draw!" << endl;
    } else if (winner == 1) {
cout << "Player 1 wins!" << endl;
} else {
cout << "Player 2 wins!" << endl;
}
return 0;
}