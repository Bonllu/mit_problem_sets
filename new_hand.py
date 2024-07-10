import random
import string 
import math 

hand = {'j': 2, 'o': 1, 'l': 1, 'w': 1, 'n':2}

word = 'jolly'

def update_hand(hand, word):
  
    copie = hand.copy()
    new_hand = dict()
    for i in word:
        new_hand[i] = new_hand.get(i, 0) + 1
    for i in list(new_hand):
        if i not in list(copie):
            del new_hand[i]
    for i in new_hand:
        if new_hand.get(i) >= copie.get(i):
            del copie[i]
        else:
            copie[i] = copie[i] - 1
    return copie
