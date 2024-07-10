import random
import string 
import math 

hand = {'j': 4, 'o': 1, 'l': 1, 'w': 1, 'n':2}

word= 'jjolly'

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
            copie[i] = copie[i] - new_hand[i]
    return copie


print(update_hand(hand, word))
