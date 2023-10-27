import datetime
import time
import mydefs as md
import random as rd
import math

a01 = md.strvalid(input("What's your name? "))
print(f'Hello {a01}, where do you want to navigate:\n')

a001 = 'Menu 1'
a002 = 'a'

t1 = {0:0 ,1: 'Menu 1' , 2: 'Menu 2', 3: 'Menu 3', 4: 'Menu 4', 5: 'Name 2', 6: 'Name 3'}
t2 = {0:0, 1: 'Name 2', 2: 'Name 3'}

while True:
    if a001 == 'Menu 1':
        #Menu 1
        print('[1] Birth Date')
        print('[2] Check Primitives')
        print('[3] Checking Operators')
        print('[4] Multiplication Table')
        print('[5] Exchange Rate')

        print('\n[n] Go to Next\n')

        a002 = md.specialint(input('-> ')) 
        if a002 == 'n':
            a001 = t1[2]
        elif 0 < a002 and a002 < 6:
            a001 = t2[a002]

    elif a001 == 'Menu 2':
        #Menu 2
        print('[6] Finding the Hypotenuse')
        print('[7] Ranking Athletes')
        print('[8] Normalizing Text')
        print('[9] Compound Interest')
        print('[10] Speed Limit - Car Ticket')

        print('\n[n] Go to Next')
        print('[p] Go to Previous \n')
        a002 = md.specialint(input('-> ')) 

        if a002 == 'n':
            a001 = t1[3]
        elif a002 == 'p':
            a001 = t1[1]
        elif 5 < a002 and a002 < 11:
            a001 = t2[a002]

    elif a001 == 'Menu 3':
        #Menu 3
        print('[11] House Loan')
        print('[12] Reverse Counting')
        print('[13] Count Evens')
        print('[14] Sum of Multiples of Three')
        print('[15] Arithmetic Sequence I')

        print('\n[n] Go to Next')
        print('[p] Go to Previous \n')

        a002 = md.specialint(input('-> ')) 
        if a002 == 'n':
            a001 = t1[4]
        elif a002 == 'p':
            a001 = t1[2]
        elif 10 < a002 and a002 < 16:
            a001 = t2[a002]

    elif a001 == 'Menu 4':
        #Menu 4
        print('[16] Arithmetic Sequence II')
        print('[17] Guess 0 to 10')
        print('[18] Calculate Factorial')
        print('[19] Display Fibonacci')

        print('\n[p] Go to Previous \n')

        a002 = md.specialint(input('-> ')) 
        if a002 == 'p':
            a001 = t1[3]
        elif 15 < a002 and a002 < 20:
            a001 = t2[a002]


    elif a001 == 'Name 2':
        b04 = input('What is your name again? ')
    elif a001 == 'Name 3':
        b04 = 4
        b05 = 10
        print(f'{b05} / {b04} = {b05/b04} ')


