#!/usr/bin/env python
# coding: utf-8

# In[12]:


###############################
# Creates a naively encoded cipher|key pair.
# The message is encoded by randomy hiding its characters in an ascii + ' '
# random text.
# The key counterpart is created the same way but does not contain any 
# 'o' or 'O'.
# These char are to be considered as circles indicating the message's char 
# positions.
# A simple reveal is to select the whole text and then drag the selected part 
# so that the right (key) selected part overlaps the left (cipher) selected part.
#
# author : luminilion
###############################



import string 
import random 
import numpy as np

def create_text(secret, alphabet, indicator, k_alphabet) :
    #print(secret)
    #print(alphabet)
    #print(indicator)
    #print(k_alphabet)

    ## Metrics
    length = len(secret)*2
    width = 20
    size = width*length

    print('Message of size', length, 'x', width)

    ## Creation of the letters placement
    places = np.arange(size)
    np.random.shuffle(places)
    places = places[:len(secret)]
    places = np.sort(places)

    ## This is the letters placement
    #print(list(zip(places, secret)))

    msg = ''

    for i in range (0, length) :
        code = ''
        key = ''
        for j in range (0, width) :
            if (len(places) > 0) and (places[0] == i*width + j) :
                code += secret[0]
                secret = secret[1:]
                key += random.choice(indicator)
                places = places[1:]
            else :
                code += random.choice(alphabet)
                key += random.choice(k_alphabet)
                
        msg = msg + code + '|' + key + '\n'

    return msg

#######

secret = "This is a secret"
alphabet = string.ascii_letters + ' '
indicator = 'oO'
k_alphabet = alphabet.replace('o', '')
k_alphabet = k_alphabet.replace('O', '')

print(create_text(secret, alphabet, indicator, k_alphabet))
print()

alphabet = '_'
k_alphabet = '_'

print(create_text(secret, alphabet, indicator, k_alphabet))

