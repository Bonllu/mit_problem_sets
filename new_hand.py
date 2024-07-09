
import random
import string 
import math 

hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u':1, 'i':1}

word = 'quaill'

def update_hand(hand, word):
    '''
    This function gets as input the word which is played by the gamer and the hand dict, and removes the letters from the copie dictionary
    we have made to not modifying the hand dictionary. If the item generated in the loop has the same value
    than the same item in hand dictionary, then it is deleted. If not, then is substracted. The function return new_hand dictionary which
    contents only the items still to play by the gamer.
    '''
    copie = hand.copy()
    new_hand = dict()
    for i in word:
        new_hand[i] = new_hand.get(i, 0) + 1
        if copie[i] - new_hand[i] <= 0:
            del copie[i]
            
        else:
            copie[i] = copie[i] - 1
    
    return copie 

print(update_hand(hand, word))
