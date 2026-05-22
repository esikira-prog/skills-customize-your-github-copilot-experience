
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a playable Hangman game in Python. You will practice using strings, loops, conditionals, and user input to manage game logic from start to finish.

## 📝 Tasks

### 🛠️ Create Core Game Setup

#### Description
Set up the game by creating a word list, selecting a secret word, and preparing the variables needed to track progress and attempts.

#### Requirements
Completed program should:

- Store at least 5 possible secret words in a predefined list.
- Randomly select one word at the start of each game.
- Create a display version of the word using underscores (for example: `_ _ _ _`).
- Track guessed letters and the number of incorrect guesses remaining.


### 🛠️ Implement Gameplay Loop

#### Description
Build the main game loop so the player can guess letters, receive feedback, and either win by revealing the word or lose by running out of attempts.

#### Requirements
Completed program should:

- Prompt the player to enter one letter per turn.
- Reveal all matching letter positions when the guess is correct.
- Decrease remaining attempts when the guess is not in the word.
- End the game with a win message when the word is fully guessed.
- End the game with a lose message when attempts reach zero, and show the secret word.
