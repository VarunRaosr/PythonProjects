# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 08:38:20 2018

@author: varun
"""

import string ,random
#print(help(string))
#print(string.ascii_letters)
#print(string.ascii_lowercase)


def generator(n):
    """
    input n : length of the word to be generated
    output : return name of length n
    """
    name = []
    for i in range(n):
        name.append(random.choice(string.ascii_lowercase))
    return "".join(name)

#length = int(input("Please enter the number of letters in your baby name"))
#print("Baby name is : ",generator(length))

#print(random.choice("this is a new day"))
#print(random.choice(string.ascii_uppercase))

# method 2:
    
def generate_letter(alphabet):
    if alphabet == "c":
        return random.choice(consonants)
    else:
        return random.choice(vowels)
    
vowels = 'aeiou'
consonants = "".join([x for x in string.ascii_lowercase if x not in vowels])
#print(len(consonants))
name = []
for i in range(5):
    '''
    input : user input c or v ( consonants or vowels)
    output : baby name :  string
    '''
    # call method based on input
    
    name.append(generate_letter(input("enter c for consonant or v for vowels")))

print("".join(name))







