from words import *
import random

secretWord = list(
    wordsList[int(random.randint(0, (len(wordsList)) - 1))].upper())

hidden = []

letterTryed = []

for char in secretWord:
    hidden.append('-')

attempts = 8

while attempts > 0:

    if hidden == secretWord:
        print('Congratulations !!')
        break  # Stop the while even if the attempts is higher than 0
    else:

        # The index is for only take the first letter
        letter = input('Try a letter: ').upper()[0]

        if not letter.isalpha():
            print('Type a letter pls')
        else:

            if letter in secretWord:
                for i in range(len(hidden)):
                    if letter == secretWord[i]:
                        hidden[i] = letter
            else:
                # if the letter is not in the letterTryed the attemps not change
                if letter not in letterTryed:
                    letterTryed.append(letter)
                    attempts -= 1

    print(
        f'All letter already tried : {letterTryed}, you have {attempts} attempts')

    for letter in hidden:
        print(letter, end='')

    print('\n\n\n')

if attempts == 0:
    print('Sorry you lose')
