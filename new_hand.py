import random
import string 
import math 

hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u':1, 'i':1}

word = 'quail'

def update_hand(hand, word):
    copie = hand.copy()
    new_hand = dict()
    for i in word:
        new_hand[i] = new_hand.get(i, 0) + 1
        if new_hand[i] - copie[i] == 0:
            del copie[i]
            
        else:
            copie[i] = copie[i] - 1
    
    return copie
