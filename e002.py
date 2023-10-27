import datetime
import time
import mydefs as md
import random as rd
import math


print('Hello, where do you want to navigate:\n')
print('[1] House Loan')
print('[2] Reverse Counting')
print('[3] Count Evens')
print('[4] Sum of Multiples of Three')
print('[5] Arithmetic Sequence I')
print('[6] Arithmetic Sequence II')
print('[7] Guess 0 to 10')
print('[8] Calculate Factorial')
print('[9] Display Fibonacci')


#House Loan
while True:
    #conditions /part.2
    print('\nHouse loan information ')
    a1 = md.intvalid(input('House price: '))
    a2 = md.intvalid(input('Your anual salary: '))
    a3 = md.intvalid(input('Amount of years to pay: '))
    #if the monthly premium is above 30% of montly salary, deny the loan
    #print the minimum amount of periods that makes the loan possible

    b1 = a2/12 #monthly salary
    b4 = a3*12 #total montly periods
    b2 = a1/b4 #montly premium
    b3 = b1 * 0.3 #max acceptable premium

    if b2 > b3:
        print("\nLoan Denied: Insuficient Montly Income \n")
    elif b2 > 0 and b2 <= b3:
        print("\nLoan Granted!")
    else:
        print("ERROR: Unsupported Data")
        break

    print(f"\nCurrent amount of periods: {b4}")
    print(f"Your montly salary: {b1:.2f}")
    print(f"Current premium: {b2:.2f}")
    print(f"Current limit line: {b3:.2f}\n")

    if b2 > b3:
        while b2 > b3:
            b4 += 1
            b2 = a1/b4
        b5 = b4/12
        print(f'\nFor your income range, you would need at least {b4} months, or {b5:.1f} years\n')
    q1 = md.ynvalid(input('Would you like to try again? [y/n]: '))
    if q1 == 'n':
        break

#reverse counting
for i in range(0, 11):
    a4 = 10 - i
    print(a4)
    time.sleep(1)

if a4 == 0:
    print('boom!')

print('\n')

#count odds between 1 and x
a5 = md.intvalid(input('Type any number: '))
b6 = 0
for i in range(0, a5+1):
    a6 = i % 2
    if a6 == 0:
        b6 += 1
print(f'There are {b6} even numbers between 0 and {a5}')

print('\n')

#sum o multiples of three between 1 and x
a7 = md.intvalid(input('Type any other number: '))
b7 = []
for i in range (0, a7+1):
    a8 = i % 2
    a9 = i % 3
    if a9 == 0 and a8 != 0:
        b7.append(i)

b8 = sum(b7)
print(f'\nThe sum of all multiples of three (not even) between 1 and {a7} is: {b8}\n')

#arithmetic sequence common difference
print('Now we are going to create an Arithmetic Sequence, and show the first 10 terms')
a10 = md.intvalid(input('What is the first term: '))
a11 = md.intvalid(input('What is the common difference: '))
b10 = []
for i in range(1,11):
    a12 = a10 + (i-1)*a11
    b10.append(a12)

print(b10)

print('\n')

a13 = md.intvalid(input('Type any number: '))
a14 = md.isprime(a13)

print(f'Is prime: {a14}')

print('\n')

#m or f for sex
while True:
    a21 = input("What's you gender [M/F]: ").strip().upper()
    if a21 == 'M' or a21 == 'F':
        break
    else:
        print('Type "M" for Male and "F" for Female')

print('\n')

#Repeat the exercise from line 72 using while. After displaying the first 10 terms, ask the user if they want more terms of the sequence (int, stops if 0)
b11 = md.ynvalid(input('We are going to create an Arithmetic Sequence again. Do you want to input new values? [y/n]: '))
if b11 == 'y':
    a10 = md.intvalid(input('What is the first term: '))
    a11 = md.intvalid(input('What is the common difference: '))

t1 = []
o=1
o2 = 11
a24 = 1
while a24 > 0:
    for i in range(o, o2):
        a22 = a10 + (o-1)*a11
        t1.append(a22)
        o += 1
    while True:
        a23 = len(t1)
        print(f'The next {a23} terms of the sequence are: \n{t1}')
        t1 = []
        a24 = md.intvalid(input('How many more terms would you like to know?: '))
        o2 = o + a24
        break
print('\n')

#Try to guess the right number from 0 to 10, repeat until the user gets it and display how many attempts were necessary
while True:
    a25 = rd.randint(0,10)
    a26 = md.intvalid(input('Guess a number between 0 to 10: '))
    if a25 == a26:
        print(f'Congatulations! {a26} was the right number!')
        break
    else:
        print(f'You missed... The right number was {a25}')

print('\n')

#calculate the factorial of x once with for and once with while
while True:
    print('\nNow we are going to check the factorial of any given number\n')
    a27 = md.intvalid(input("Type your number: "))
    t2 = []
    while a27 > 0:
        a27 -= 1
        t2.append(a27+1)
    print(t2)
    o4 = len(t2)
    o5 = 0
    o6 = 1
    while o5 < o4:
        o6 = o6 * t2[o5]
        o5 += 1
    print(o6)
    a29 = md.ynvalid(input('Would you like to try again? [y/n]: '))
    if a29 == 'n':
        break

print('\n')

#display a fibonnaci sequence starting from 'x' (int input)
while True:
    a30 = md.intvalid(input('What position of the fibonacci sequence do you want to know: '))
    t4 = [0, 1]
    i = 0
    while i < a30:
        a31 = t4[i+1] + t4[i]
        t4.append(a31)
        i += 1
        
        # break

    print(t4)
    print(f'the {a30}th term of the fibonacci sequence is: {t4[i]}')
    a32 = md.ynvalid(input('Would you like to try again? [y/n]: '))
    if a32 == 'n':
        break

print('\n')
#Recieve various int inputs. On each 5th input, asks if the user wants to type 5 more. At the end, display the total amount of typed numbers, their average, the Highest and the Lowest




