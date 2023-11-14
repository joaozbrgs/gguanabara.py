import mydefs as md
import pandas as pd
import requests
from bs4 import BeautifulSoup
import random as rd


l01 = list(range(72,80))

print('-' * 30)
# for i in range (0, len(l01)):
#     print(f'{l01[i]:~^30} (insert here the related task)') #Whithin brackets for filling effect



while True:
    a1 = md.intvalid(input('type a task code: '))
    if a1 in l01:
        break
    else:
        print('\nOut of range \n')


#Tuples

#72
if a1 == 72:
    t1=(
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten'
    )

    print("=" * 100)
    print('Now you will type a number from 0 to 10 and it will display it on text format')
    print("=" * 100)

    a1 = input('\nType your number between 0 and 10: ')
    while True:
        try:
            a1 = int(a1)
            if a1 in range(0,11):
                break
            else:
                a1 = int(input('Your number was out of range. Type a new one: '))
        except ValueError:
            a1 = int(input('type a valid answer: '))


    print(f'You typed the number {t1[a1]}!')


#73
if a1 == 73:
    t2 = (
        'PAL',
        'BOT',
        'GRE',
        'BRG',
        'CAM',
        'FLA',
        'CAP',
        'FLU',
        'CUI',
        'SPA',
        'COR',
        'FOR',
        'INT',
        'SAN',
        'VAS',
        'BAH',
        'GOI',
        'CTB',
        'AMG'
    )

    print(len(t2))
    print(t2, '\n')
    print('=' * 30, '\n')
    print('Ranking: ' , end='')
    print(f'{t2[0]}', end='')
    for i in range(1,6):
        print(f' -> {t2[i]}', end='')

    print('')
    print('Reverse Ranking: ', end='')
    print(t2[-1], end='')
    for i in range(2,5):
        print(f' -> {t2[-i]}', end='')
    print('')
    a2 = sorted(t2)
    print('\nAlphabetic Order:')
    print(a2[0:])
    # print('\n')
    print('\n', '=' * 30)

    #Check position
    while True:
        while True:
            a3 = input('What team would you like to know the position: ').upper().strip()
            if a3 in t2:
                break
            else:
                print('Team not ranked!\n')

        a4 = (t2.index(a3))
        print(f'The team {a3} is ranked {a4 + 1}° team in the league!')
        print('\n')
        a5 = md.ynvalid(input('Want to check another team? [y/n]: '))
        if a5 == 'n':
            break


#74
if a1 == 74:
    while True:
        lt1 = []
        for i in range(0,5):
            b1 = rd.randint(0,99)
            lt1.append(b1)
        print('\n', '=' * 30)
        print(lt1)
        b2 = sorted(lt1)
        print(b2)
        print(len(lt1))
        print(f'The higest number was {b2[-1]} and the lowest was {b2[0]}')
        print('=' * 30, '\n')
        b3 = md.ynvalid(input('Would you like to try again? [y/n]: '))
        if b3 == 'n':
            break


#75
if a1 == 75:
    while True:
        t3 = (
            md.intvalid(input('Type a number:')),
            md.intvalid(input('Type a number:')),
            md.intvalid(input('Type a number:')),
            md.intvalid(input('Type a number:')),
            md.intvalid(input('Type a number:')),
        )
        
        if 3 in t3:
            b1 = True
        else:
            b1 = False
        
        b2 = t3.count(9)
        b3 = 0
        b4 = 0
        for i in range(0, len(t3)):
            b6 = md.iseven(t3[i])
            if b6 is True:
                b3 += 1
            elif b6 is False:
                b4 += 1
            


        print('=' * 30)
        print(f'You typed the number 3: {b1}')
        print(f'The number 9 was typed {b2} times')
        print(f'Your typed {b4} odd numbers and {b3} even numbers')
        print('=' * 30)

        #Problems on code:
        #Zero is accounting as Even (% 2 = 0)
        #No distinction between negative and positive (-9, -9, 9) will result in b2 == 3

        b7 = md.ynvalid(input('\nWould you like to try again? [y/n]: '))
        if b7 == 'n':
            break



#79
if a1 == 79:
    while True:
        l4 = []
        
        print('-' * 30)
        b1 = md.intvalid(input('How many values do you want to input?: '))
        print('\n')
        o = 1
        while len(l4) < b1:
            b2 = md.intvalid(input(f'Type your {o}° value: '))
            if b2 not in l4:
                l4.append(b2)
                o += 1
            else:
                print("This value was already on the list and won't be added")
        print('\n')
        b8 = sorted(l4)
        print(f'The numbers were:\n', l4)
        print('\n')
        print('If sorted, the numbers were:\n', b8[0], end='')
        for i in range(1, len(b8)):
            print(f' -> {b8[i]}', end='')

        print('\n')
        b7 = md.ynvalid(input('\nWould you like to try again? [y/n]: '))
        if b7 == 'n':
            break


#80
if a1 == 80:
    l5 = []
    n = 0
    while len(l5) <= 5:
        b2 = md.intvalid(input('Type a number: '))
        if b2 in l5:
            print("This value was already on the list and won't be added")
        else:
            b9 = len(l5)
            for i in range(0, b9):
                





if a1 == 71:
    l1 = [
        'One',
        2,
        3.0,
        '4',
        'five',
        6,
        7,
        '8',
        9.0,
        'ten'
    ]

    l2 = []

    for i in range(1,11):
        l2.append(i)

    l3 = list(range(20,31))


    print(l1,l2)

    if 7 in l1 and 7 in l2:
        l1.remove(7)
        l2.remove(7)

    l3.sort(reverse=True)



