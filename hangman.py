# import necessary modules

import random
import sys

# define set of available words

f = file('google-10000-english-usa.txt').readlines()
choices = []
for line in f:
    line = line[:-1]
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
        stupid_test = True
        while stupid_test:
            guess = raw_input("What letter would you like to guess? ").upper()
            if guess not in guesses:
                stupid_test = False
            else:
                print "You already tried " + guess + ". Get more creative!"        
        guesses.append(guess)
        for i, letter in enumerate(targetword[0]):
            if guess == letter.upper():
                correctguessset[i] = guess
                correct += 1
        print "***************"
        if correct > target:
            if correct == len(targetword[0]):
                print "***************"
                print "***************"
                print "***************"
                print "Congratulations. You won!"
                print "It was that dastardly mouthful", targetword[0].upper()
                start_game()
            else:
                print "Nice job,", guess.upper(), "is in the word."
        else:
            print "Sorry, " + guess.upper() + " is not present in this word."
            wrongguess += 1
            if wrongguess > 5:
                print_hangman(wrongguess)
                print "Sorry, you lost this round."
                print "If you were wondering, the word was", targetword[0] + ". What a doozy..."
                print "***********"
                start_game() 
        print_hangman(wrongguess)
        print "You have these letters: ", correctguessset
        print "You have tried the following letters: ", guesses

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