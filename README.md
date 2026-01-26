# ☃️ Snowman Meltdown

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Purpose](#project-purpose)

## General info
☃️ **Snowman Meltdown** is a console-based word-guessing game inspired by classic Hangman.  
The player must guess a hidden word letter by letter before the snowman melts completely.

This project was created to practice Python fundamentals and to gain hands-on experience working with Git and GitHub.

## Technologies
Project is created with:
* Python version: 3.14
* Standard Python libraries only (`random`)
* Console-based interface with ASCII art

## Features
* Classic Hangman-style word guessing gameplay
* Snowman-themed ASCII art that changes with each mistake
* Random word selection
* Input validation for user guesses
* Colored console output for better user feedback
* Option to replay the game after finishing

## Setup
1. Clone the repository and navigate into the folder:
```bash
  $ git clone https://github.com/yourusername/snowman-meltdown.git  
  $ cd snowman-meltdown
```
2. Make sure Python is installed:
```bash
  $ python --version
````
4. Run the game:
```bash
  $ python main.py
````
## Usage
🎯 **How to Play**
1. Start the game by running `main.py`.
2. A random word is selected.
3. Guess one letter at a time.
4. Each wrong guess increases the number of mistakes.
5. The snowman melts with every mistake.
6. Guess the full word before the snowman melts completely to win.

The game ends when:
* All letters are guessed correctly → **You win**
* The maximum number of mistakes is reached → **Game over**

After the game ends, you can choose whether to play again.

## Project Purpose
This project is designed as a **learning exercise** to practice:

* Python control flow and loops
* Working with lists and strings
* Game logic implementation
* User input validation
* Using ASCII art in console applications
* Structuring a project with multiple Python files
* Using Git and GitHub for version control
