import random
import time

def displayIntro():
    print('You are in a land full of sanctity and good taste, Karenswood.')
    print('In front of you, you see two markets.')
    print('In one market, the manager is freely available and will listen')
    print('to your tirades about the store layout and visible tattoos.')
    print('In the other one the neolibs will refuse you service for')
    print('refusing to wear a mask.')

def chooseStore():
    store = ''
    while store != '1' and store != '2':
        print('Which store will you select? (1 or 2)')
        store = input()

    return store 

def checkStore(chosenStore):
    print('You approach the store...')
    time.sleep(2)
    print('It has potted plants with tiny American flags...')
    time.sleep(2)
    print('A man with a crew cut and blood red apron appears...')
    time.sleep(2)
    

    friendlyStore = random.randint(1, 2)

    if chosenStore == str(friendlyStore):
        print('I know you\'ve never shopped here before, but would you like') 
        print('to fill out a suggestion card?')

    else:
        print('The liberal agenda strikes again')

playAgain = 'yes'
while playAgain == 'yes ' or playAgain =='y':

    displayIntro()

    storeNumber = chooseStore()

    
    checkStore(storeNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    

    displayIntro()

    storeNumber = chooseStore
    
    
