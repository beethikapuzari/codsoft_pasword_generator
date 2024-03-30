#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

letters= str(input("enter alphabet from A to Z"))
numbers= str(input("enter number from 0 to 9"))
symbols= input("enter any symbol")
print("Welcome to Password Generator")
n_letters= int(input("How many letters you want in yur password?\n")) #4
n_numbers= int(input("How many numbers you want in yur password?\n")) #3
n_symbols= int(input("How many symbols you want in yur password?\n")) #2
password=""
for i in range(1,n_letters+1):
    char = random.choice(letters)
    password = password+ char
for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password = password +char
for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password = password + char
print(password)

