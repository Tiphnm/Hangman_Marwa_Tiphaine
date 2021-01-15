#!/usr/bin/env python 
# coding=utf-8

import random 
import logging

logging.basicConfig(filename='text.log', level=logging.INFO,
                    format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')

logging.info('Reading file : start')
my_file = open("word_list.txt", "r") 
lines = my_file.readlines()
list_word = [elem.strip() for elem in lines]
logging.info('reading file : end')
my_file.close()