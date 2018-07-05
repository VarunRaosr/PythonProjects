# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:15:00 2018

@author: varun
"""

import random
import time


def display_intro():
    print("You've entered the Dragon Forest!!!")
    time.sleep(2)
    print("You see two caves in front of you. One of them has treasure and the other one...")
    time.sleep(2)
    print("Has the Dragon !!!!!!!!1")
    time.sleep(2)
    
def choose_cave():
    cave = ""
    while cave != '1' and cave !='2':
        print("Which cave will you go to? (1 or 2) ?")
        cave = input()
        
    return cave

def checkCave(chosenCave):
    print("You approach the cave!!")
    time.sleep(2)
    print("It is dark and spooky..")
    time.sleep(2)
    print("A large dragon jumps in front of you!",end=" ")
    time.sleep(2)
    print("His jaws wide open and....!")
    time.sleep(2)
    
    friendlycave = random.randint(1,2)
    
    safe = [' lucky kid ','','sweet child']
    unsafe = [" stupid kid "," fool ","'re unlucky "]
    if str(chosenCave) == str(friendlycave):
        time.sleep(2)
        word = random.choice(safe)
        amt = random.randint(1,1200)
        print("you",word,"here's your treasure ",amt,"$")
    else:
        time.sleep(2)
        word = random.choice(unsafe)
        print("You",word,"You're eaten by the dragon!!!")
    
playagain = 'yes'
while playagain == 'yes' or playagain == 'y':
    display_intro()
    cavenum = choose_cave()
    checkCave(cavenum)
    print("Do you want to play again? (yes or no)")
    playagain = input().strip()

        