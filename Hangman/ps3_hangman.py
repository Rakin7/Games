# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    x=0
    for i in range(0,len(secretWord)):
        if (secretWord[i] not in lettersGuessed):
            x+=1
            break
    if(x==0):
        return True
    else:
        return False
            
            
        
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    x=""
    for i in range(0,len(secretWord)):
        if (secretWord[i] in lettersGuessed):
            x+=secretWord[i]+" "
        else:
            x+="_ "
    return x
           



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    x=string.ascii_lowercase
    y=""
    for i in range(0,len(x)):
        if (x[i] not in lettersGuessed):
            y+=x[i]
    return y
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    i=8
    y='abcdefghijklmnopqrstuvwxyz'
    lettersGuessed=[]
    win=False
    while(i>0):
        print('-------------')
        print('You have '+ str(i) +  ' guesses left.')
        print('Available letters: ',y)
        z=input('Please guess a letter:')
        if(z not in y):
            print('Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
        elif(z in secretWord):
            lettersGuessed.append(z)
            y=getAvailableLetters(lettersGuessed)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            if(isWordGuessed(secretWord, lettersGuessed)):
                win=True
                break
        elif(z not in secretWord):
            lettersGuessed.append(z)
            y=getAvailableLetters(lettersGuessed)
            print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
            i-=1
    print('-------------')
    if(win==True):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was '+ secretWord)





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
