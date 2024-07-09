
import math
 
import random
import string





n = 6
s_l_v = {
  'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


mot = ["weed"]

def get_word_score(paroles, n):
    deuxieme = list()
    cle_valeur = list()
    valeurs = list()

    for word in paroles:
        deuxieme.append(7 * len(word) - 3 * (n -len(word)))
        l_s = dict()
        for i in word:
            l_s[i] = l_s.get(i, 0) + s_l_v[i]
        cle_valeur.append(l_s)
        valeurs.append(sum(l_s.values())) 
        fin = int(deuxieme[0]) * int(valeurs[0])
    return fin

print(get_word_score(mot, n))
     

def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure=False
    # dictionary of words and scores
    words = {("weed", 6):176
              }
    for (word, n) in words.keys():
        score = get_word_score(mot, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score()")
            print("\tExpected", words[(word, n)], "points but got '" + \
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True
    if not failure:
        print("SUCCESS: test_get_word_score()") 

test_get_word_score()
