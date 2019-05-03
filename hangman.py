#!/usr/bin/env python3
"""evelandy/W.G.
Apr. 21 2019 3:16pm
HangMan Game 
Python36-32 
"""

import random

# Word Lists
easy_words = ['java', 'play', 'code', 'bugs', 'crud', 'html', 'data', 'list', 'else', 'elif', 'menu', 'main']
med_words = ['hello', 'world', 'algol', 'basic', 'cobol', 'error', 'noise', 'input', 'react', 'coder']
hard_words = ['python', 'javascript', 'information', 'function', 'choice', 'programming', 'django', 'computer']


def main():
    welcome = "Welcome to Programmer Hangman!"
    deco = "=" * len(welcome)
    print(deco + '\n' + welcome + '\n' + deco)
    menu()


def menu():
    menu = input("To see Instructions press (i)\nTo Play press (p)\nTo Quit press (q)\n: ")
    if menu.lower() == 'q':
        print("Thank you for playing.")
    elif menu.lower() == 'p':
        choice = input("What difficulty would you like to play?\nEasy <= 4 words - press (e)\n"
                       "Medium 5 words - press (m)\nHard >=6 words - press (h)\n: ")
        if choice.lower() == 'e':
            play(easy_words)
        elif choice.lower() == 'm':
            play(med_words)
        elif choice.lower() == 'h':
            play(hard_words)
        else:
            print("I don't understand your response.")
    elif menu.lower() == 'i':
        instructions()
    else:
        print("I don't understand your response.")


def replay(retry):
    if retry.lower() == 'n':
        print("Thanks for playing")
    elif retry.lower() == 'y':
        menu()
    else:
        print("I didn't understand your reply.")


def instructions():
    input("""
    Once the game has started simply press a letter, and if it is in the randomly chosen word it will be displayed in 
    the correct space that is hidden by '*' characters. But in this version you can only choose a letter at a time and 
    only letters, no numbers, spaces or special characters. Later versions will let you enter a whole word if you think 
    you know it, as well as keep points to track your progress in the game. But until then, you have this simple but
    fun version! Now, to go back to the menu and start the game press Enter.\n\n\n\n
    """)
    menu()


def play(type):
    played_chars = []
    invalid_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*',
                          '(', ')', ',', '<', '.', '>', '?', '.', '{', '[', '}', ']', '\\', '|', '~', '`']
    hangman = ('\n======+=\n||    |\n||    \u06dd\n||    +\n||\n||\n||\n||\n||\n||\n===========\n',
               '\n======+=\n||    |\n||    \u06dd\n||  /=+=\\\n||    |\n||\n||\n||\n||\n||\n===========\n',
               '\n======+=\n||    |\n||    \u06dd\n||  /=+=\\\n||  | | |\n||\n||\n||\n||\n||\n===========\n',
               '\n======+=\n||    |\n||    \u06dd\n||  /=+=\\\n||  | | |\n||    Ḁ\n||   | |\n||\n||\n||\n===========\n'
               , '\n======+=\n||    |\n||    \u06dd\n||  /=+=\\\n||  | | |\n||    Ḁ\n||   | |\n||   | |\n||\n'
                 '===========\n')

    word_list = [word for word in type]
    pick = random.choice(word_list)
    correct = 0

    hidden_word = []  # This makes a new list to hold the hidden values for the word
    for item in pick:
        hidden_word.append('*')  # This loops through the list and replaces the letters with the hidden character
    print(hidden_word)  # This will display the hidden characters in the length of the word to be guessed

    # print(hangman[0])
    chances = len(hangman)

    char = [char for char in pick]

    while chances != 0 and "*" in hidden_word:
        choice = input("Pick a letter: ")
        if len(choice) > 1:
            print("Please choose only ONE letter")
            continue
        if choice.lower() in invalid_characters:
            print("Please enter only letters.")
            continue
        if choice.lower() in played_chars:
            print("You have already played that letter")
            continue
        else:
            played_chars.append(choice.lower())

        if choice.lower() in char:
            print("Correct")
            correct += 1
            char.remove(choice)

            for letter in range(len(pick)):  # This loops through the picked word to be guessed
                if choice == pick[letter]:  # This states if the users guess equals a letter in the hidden word
                    hidden_word[letter] = choice  # Replace the hidden character in the hidden lst with the users letter
            if '*' in hidden_word:
                print(hidden_word)  # Prints the updated word with known letters and hidden letters together
            else:
                print("You Win!\nAnswer: {}".format(pick))
                retry = input("Would you like to play another game? (y / n)\n: ")
                replay(retry)
                break

        elif choice.lower() not in char:
            print("Sorry you missed that one.")
            chances -= 1
            print(hangman[(len(hangman) - 1) - chances])  # Adds more to the hangman character on every miss
            print("You have {} guesses left".format(chances))
        if chances == 0:
            print("Hangman, you loose.\nAnswer: {}".format(pick))
            retry = input("Would you like to play another game? (y / n)\n: ")
            replay(retry)


main()
