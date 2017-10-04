# import necessary modules

import random
import sys

# define set of available words

f = file('/usr/share/dict/words').readlines()
choices = []
for line in f:
    line = line[:-2]
    choices.append(line)

# pick a word

def play_round():
    targetword = random.sample(choices, 1)
    correctguessset = []
    guesses = []
    for i in range(len(targetword[0])):
        correctguessset.append("__")
    wrongguess = 0
    correct = 0
    print "***************"
    print "Your word has ", str(len(targetword[0])), " letters. Get six guesses wrong and you lose."
    print "***************"
    while True:
        # keep track of how many you currently have correct
        target = correct
        guess = raw_input("What letter would you like to guess? ")
        guesses.append(guess)
        for i, letter in enumerate(targetword[0]):
            if guess == letter:
                correctguessset[i] = guess
                correct += 1
        if correct > target:
            if correct == len(targetword[0]):
                print "Congratulations. You won!"
                start_game()
            else:
                print "You now have the following letters: "
                print correctguessset
                print "You have tried the following letters: "
                print guesses
        else:
            print "Sorry, " + guess + " is not present in this word."
            wrongguess += 1
            print_hangman(wrongguess)
            print "You have tried the following letters: "
            print guesses
        if wrongguess > 5:
            print_hangman(wrongguess)
            print "Sorry, you lost this round."
            start_game() 

def start_game():
    answer = raw_input("Would you like to play hangman? yes/no: ")
    if answer == "yes":
        print "***************"
        print "New game!"
        print "***************"
        play_round()        
    elif answer == "no":
        print "Probably a wise decision."
        sys.exit(0)
    else:
        print "Not a valid entry."
        start_game()

def print_hangman(num):
    if num == 0:
        print "_______"
        print "|     |"
        print "|      "
        print "|      "
        print "|      "
    elif num == 1:
        print "_______"
        print "|     |"
        print "|     O"
        print "|      "
        print "|      "
    elif num == 2:
        print "_______"
        print "|     |"
        print "|     O"
        print "|     |"
        print "|      "
    elif num == 3:
        print "_______"
        print "|     |"
        print "|     O"
        print "|     |/"
        print "|      "
    elif num == 4:
        print "_______"
        print "|     |"
        print "|     O"
        print "|    \\|/"
        print "|      "
    elif num == 5:
        print "_______"
        print "|     |"
        print "|     O"
        print "|    \\|/"
        print "|     /"
    elif num == 6:
        print "_______"
        print "|     |"
        print "|     O"
        print "|    \\|/"
        print "|     /\\"

start_game()