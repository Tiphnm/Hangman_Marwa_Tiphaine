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

lives = 5

logging.info('Choosing random word : start')
random_word = list(random.choice(list_word))

print(random_word) #pour nous 
#print(type(user_choice))  #pour nous 

hidden_list=[]

###### Remplacing letter by "_"

def underscore(chosen_word, mylist):
    for i in chosen_word :
        i = "_ "
        mylist.append(i)
    print(mylist)

underscore_word = underscore(random_word, hidden_list)


def user_try(life, chosen_word, mylist):   
    guess = raw_input("Choose a letter: ").lower()

    if guess not in chosen_word : 
        life -= 1 
        print("You choose %s... Sorry you lost a life: \n " %(guess) + "\nYou have %s lives remaining." %(life))

    else :
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if guess == letter: 
                hidden_list[i] = letter 
        print(hidden_list)
        
underscore(random_word, hidden_list)
user_try(lives, random_word, hidden_list)
