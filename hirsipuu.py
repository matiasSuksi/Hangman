import random
import os


#muuttujat
wordlist = ['insinööri', 'muurari', 'sairaanhoitaja', 'nuohooja', 'kirurgi', 'lääkäri', 'maalari', 'maanviljelijä']
chosen_word = str(wordlist[random.randint(0,len(wordlist)-1)])
guesses = int(5)
hidden_word = str(len(chosen_word)*'_')


#hirsipuu
def hangman():
    if guesses == -1:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('/ \  |')
        print('     |   ')
        print('=========')
    elif guesses == 0:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print(' |   |')
        print('/ \  |')
        print('     |   ')
        print('=========')
    elif guesses == 1:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print(' |   |')
        print('/    |')
        print('     |   ')
        print('=========')
    elif guesses == 2:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('     |')
        print('     |')
        print('     |   ')
        print('=========')
    elif guesses == 3:
        print('     |')
        print('     |')
        print('     |')
        print('     |   ')
        print('=========')
    elif guesses == 4:
        print('     |   ')
        print('=========')

hangman()

print('Tervetuloa pelaamaan hirsipuuta', os.getlogin())


#peli-loop
while guesses >= 0:

    print('Arvaa ammatti!')
    print(hidden_word)
    print('Arvauksia jäljellä:')
    print(guesses)

    hangman()

    guess = str(input())

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            hidden_word = hidden_word[:index] + letter + hidden_word[index+1:]
        elif letter != guess:
            continue
    
    if guess not in chosen_word:
        guesses -= 1

    if guesses == -1:
        hangman()
        print('Hävisit pelin', '(° ͜ʖ͡°)╭∩╮')
        break
