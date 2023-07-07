"""
File: hangman.py
Name: 陳大再
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    """
    guess()


def guess():
    answer = random_word()
    tmp_answer = ""
    n_turns = N_TURNS
    for _ in answer:
        tmp_answer += "-"
    print("The word looks like " + tmp_answer)

    while True:
        print("You have " + str(n_turns) + " wrong guesses left.")

        ch = input("Your guess: ").upper()
        if not ch.isalpha():
            print("Illegal format.")
            ch = input("Your guess: ").upper()

        tmp = ""

        if ch in answer:
            print("You are correct.")
        else:
            print("There is no " + ch + "'s in the word.")
            n_turns -= 1

        for i in range(len(answer)):
            if ch == answer[i]:
                tmp += ch
            elif tmp_answer[i] != "-":
                tmp += tmp_answer[i]
            else:
                tmp += "-"

        tmp_answer = tmp

        if n_turns == 0:
            print("You are completely hung :(")
            break
        elif tmp_answer == answer:
            print("You win!!")
            break
        else:
            print("The word looks like " + tmp_answer)

    print("The word was: " + answer)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
