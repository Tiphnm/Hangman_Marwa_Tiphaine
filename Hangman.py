#!/usr/bin/env python 
# coding=utf-8

import random 
import logging

logging.basicConfig(filename='text.log', level=logging.INFO,
                    format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')

logging.info('This is an info:')
logging.error('This is an erro:')

logging.info('Reading file : start')
my_file = open("word_list.txt", "r") 
lines = my_file.readlines()
list_word = [elem.strip() for elem in lines]
logging.info('reading file : end')
my_file.close()

###### Variables

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 5

logging.info('Choosing random word : start')
user_choice = list(random.choice(list_word))

print(user_choice) #pour nous 
#print(type(user_choice))  #pour nous 

logging.info('Choosing random word : start')

hidden_list=[]

###### Remplacing letter by "_"

for i in user_choice:
    i = "_ "
    hidden_list.append(i)

guess = raw_input("Choose a letter: ").lower()

if guess not in user_choice: 
    lives -= 1 
    print("You choose %s... Sorry you lost a life: \n " %(guess) + HANGMANPICS[0] + "\nYou have %s lives remaining." %(lives))

else : 
    for i in range(len(user_choice)):
        letter = user_choice[i]
        if guess == letter: 
            hidden_list[i] = letter 
print(hidden_list)
        