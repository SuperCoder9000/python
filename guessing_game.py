# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:33:44 2024

@author: KIIT0001
"""

secret_num = int(input("enter the number to be guessed by player 2 : "))
i=1
while i<=35:
    print("*")
    i = i+1
guess_lim = 3
guess_count = 0 
while guess_count < guess_lim:
    guess = int(input("Guess : "))
    guess_count = guess_count+1
    if guess == secret_num:
        print("You won!!!")
        break
    elif guess_count>=guess_lim:
        print("you lost.....")