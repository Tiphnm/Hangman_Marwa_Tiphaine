#!/usr/bin/env python 
# coding=utf-8

import random 
import logging

logging.basicConfig(filename='text.log', level=logging.INFO,
                    format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')

logging.info('This is an info:')
logging.error('This is an error:')

logging.info('Reading file : start')
my_file = open("word_list.txt", "r") 
lines = my_file.readlines()
list_word = [elem.strip() for elem in lines]
logging.info('reading file : end')
my_file.close()

###### Variables

Game_is_on = True

lives = 5

hidden_list = []

logging.info('Choosing random word : start')
random_word = list(random.choice(list_word))

print(random_word) #pour nous 
#print(type(user_choice))  #pour nous

###### Remplacing letter by "_"

def underscore(chosen_word, secret_list):
    for i in chosen_word :
        i = "_"
        secret_list.append(i)
    return secret_list

underscore_word = underscore(random_word, hidden_list)
print(underscore_word)


def user_try(life, chosen_word, secret_list): 

    Game_is_on = True

    while Game_is_on:
        guess = raw_input("Choose a letter: ").lower()
        
        for i in range(len(secret_list)):
            letter = chosen_word[i]
            if guess == letter: 
                secret_list[i]= letter 
        print(secret_list)

        if secret_list.count("_") == 0:
            Game_is_on = False 
            print("You win")
    
        if guess not in chosen_word: 
            life -=1
            print("You lost a life, you have %s life remaining" %(life)) 

        if life == 0: 
            Game_is_on = False
            print("You are dead.")
        
        

#mon user a des vies et il devine la bonne lettre: on remplace l'underscore en la lettre deviné 

#mon user n'a plus de vie, le jeu s'arrete 

#autre proposition: tant qu'il y a des underscore dans ma liste et que mes vies sont supérieuses à 0 
            

user_try(lives, random_word, underscore_word)