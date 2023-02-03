import random
from randomWords import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words) # the random word
    word_letters = set(word) # the random word put in a set to use for runnig conditions
    alphabet = set(string.ascii_uppercase) #alphabet standard ASCII
    used_letters = set() # where all used letters will be stored
    lives = 8 #number of lives we have at the begining of the game

    while len(word_letters) > 0 and lives > 0: # while loop runs so long as there is still word left in our word letters
        print('You have', lives, 'lives left. You have already used these letters: ', ' '.join(used_letters))

        #show the user the words guessed rightly and words remaining
        word_list = [letter if letter in used_letters else '-' for letter in word] #
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter... ').upper()
        if user_letter in alphabet - used_letters: # this checks if the user input is a valid alphabet and it is not in our used letters hence minus used letters
            used_letters.add(user_letter) # this adds it to our used letters list

            if user_letter in word_letters: # if the letter i guessed is in the list of the random word we remove it from word letters
                word_letters.remove(user_letter) # the removing logic
            else:
                lives = lives - 1 #else life decreses
                print('Your letter is not in the word!') #we will be notified that your letter is not in the word

        elif user_letter in used_letters: # if you repeat a number you had already used it will tell you
            print('You have already used that character. Please try again!') # the notifier
        else:
            print('Invalid character, Please try again!') #if not, means you didn't put in a charcter at all and you will be notified

    if lives == 0 : # when live ends
        print('Sorry you died! The word was ',word)
    else:
        print('Congratulations you have won!!')# when you win

hangman()