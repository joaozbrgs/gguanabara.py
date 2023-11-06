import datetime
import time
import mydefs as md
import random as rd
import math

q01 = md.strvalid(input("What's your name? "))
print(f'Hello {q01}, where do you want to navigate:\n')

a001 = 'Menu 1'
a002 = 'a'

t1 = {0:0 ,1: 'Menu 1' , 2: 'Menu 2', 3: 'Menu 3', 4: 'Menu 4'}
t2 = {
    0: 'Terminate',
    1: 'Birth Date',
    2: 'Check Primitives', 
    3: 'Checking Operators', 
    4: 'Multiplication Table', 
    5: 'Exchange Rate',
    6: 'Finding Hypotenuse', 
    7: 'Ranking Athletes', 
    8: 'Normalize Text', 
    9: 'Compound Interest', 
    10: 'Car Ticket',
    11: 'House Loan',
    12: 'Reverse Counting',
    13: 'Count Evens',
    14: 'Sum of Multiples of Three',
    15: 'Arithmetic Sequence I',
    16: 'Arithmetic Sequence II',
    17: 'Guess 0 to 10',
    18: 'Calculate Factorial',
    19: 'Display Fibonacci',

}

# def try_again():
#     a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
#     if a01 == 'n':
#         print('\n')
#         a001 = t1[1]
#         break
#     print('\n')
#     return a001


while True:
    if a001 == 'Terminate':
        print('Thanks for using this code!')
        break

    elif a001 == 'Menu 1':
        #Menu 1
        print('[1] Birth Date')
        print('[2] Check Primitives')
        print('[3] Checking Operators')
        print('[4] Multiplication Table')
        print('[5] Exchange Rate')
        print('[0] Terminate')

        print('\n[n] Go to Next\n')

        a002 = md.specialint(input('-> ')) 
        if a002 == 'n':
            a001 = t1[2]
        elif a002 == 'p':
            a002 == md.specialint(input('Type a valid answer: '))
        elif 0 < a002 and a002 < 6:
            a001 = t2[a002]
        elif a002 == 0:
            break

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
        elif a002 == 0:
            break

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
        elif a002 == 0:
            break

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
        elif a002 == 'n':
            a002 == md.specialint(input('Type a valid answer: '))
        elif 15 < a002 and a002 < 20:
            a001 = t2[a002]
        elif a002 == 0:
            break


    elif a001 == 'Birth Date':
        while True:
            print(f'Hello {q01}, please type your date of birth:')
            a02 = int(md.intvalid(input('Day: ')))
            a03 = int(md.intvalid(input('Month: ')))
            a04 = int(md.intvalid(input('Year: ')))

            b01 = datetime.date(a04, a03, a02) #Use the datetime module to organize the aquired information
            b02 = datetime.date.today() #Get the current date, so we can subtract by the date of birth and find the age
            b03 = b02-b01
            age1 = b03.days // 365
            print('You are', age1, 'years old')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                a001 = t1[1]
                break
            print('\n')
            print('\n')
            a001 = t1[1]

    elif a001 == 'Check Primitives':
        while True:
            a05 = input('Type anything: ')
            print('\nThe answer is made out of letters: ', a05.isalpha())
            print('The answer is numeric: ', a05.isnumeric())
            print('The answer is alphanumeric: ', a05.isalnum())
            print('The answer is just empty spaces: ', a05.isspace())
            print('The answer is all in CAPS LOCK: ', a05.isupper())
            print('The answer has only the first letter as capital: ', a05.istitle())
            print('\n')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]

    elif a001 == 'Checking Operators':
        while True:
            a06 = input('Say Yes or No to receive a random number: ') 
            b04 = rd.randint(1,1000)
            print(f'\nYour number is {b04}:')

            b05 = b04-1
            b06 = b04+1
            b07 = b04%2
            b09 = b04*2
            b10 = b04*3
            b11 = int(math.pow(b04, 2))
            b12 = math.sqrt(b04)

            print(f'Your number is between {b05} and {b06};')
            print(f'The double of {b04} is {b09};')
            print(f'The triple of {b04} is {b10};')
            print(f'{b04} squared is {b11};')
            print(f'The square root of {b04} is {b12:.2f};') #reduce the float part to only 2 decimal cases


            if b07 == 0:
                print('Your number is EVEN;')
            else:
                print('Your number is ODD;')


            b08 = md.isprime(b04)
            print(f'Your number is PRIME: {b08}\n')

            b13 = rd.randint(1, 1000)
            b14 = (b04 + b13)/2
            print(f'I took the liberty to choose another number, that happened to be {b13};')
            print(f'The average between {b04} and {b13} is {b14}\n')

            b15 = rd.randint(11, 21)
            b16 = math.sqrt(b15)
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                a001 = t1[1]
                break
            print('\n')
            # try_again()
    
    elif a001 == 'Multiplication Table':
        #if a07 == 'y':
    # for i in range(1, 11):
        while True:
            a08 = md.intvalid(input('Type your number: '))
            print('\n')
            for o in range(1, 11):
                print(f'{a08} x {o} = {a08*o}')

            print('\n')
            a09 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a09 == 'n':
                a001 = t1[1]
                break
    
    elif a001 == 'Exchange Rate':
        while True:
            a09 = md.floatvalid(input('type a float number (it will be used as the exchange rate): '))
            b17 = rd.randint(10,20)
            b18 = rd.randint(50,120)
            b19 = math.sqrt(b17)
            b20 = b18*a09
            b21 = rd.randint(39,113)
            b22 = 5
            b23 = b21*b22
            b24 = b23*b19

            print(f'\nIf you had {b18} USD, you would be able to buy {b20:.2f} BRL.')
            print(f'With {b20:.2f} BRL, you could buy {b21} tins of paint;')
            print(f'We know that one paint tin contains {b22} liters, and that each liter covers {b19:.2f} square meters;')
            print(f'So {b21} tins would give us {b23} liters of paint, enough to paint {b24:.2f} square meters\n')
            print('\n')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]

    elif a001 == 'Finding Hypotenuse':
        while True:
            #Finding the hypotenuse
            #a10 = md.ynvalid(input('The following code will generate random right triangles. Would you like to try it? [y/n]: '))
            #if a10 == 'y':
                # while True:
                    while True:
                        b25 = md.s_triangle() #generate a simple valid triangle with random values 
                        b26 = math.pow(b25[0], 2) + math.pow(b25[1], 2)
                        b27 = math.pow(b25[2], 2)
                        if b26 == b27: #check the Pytagorean theorem condition to a right triangle
                            break
                    print(f'Your right triangle is {b25};')
                    a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
                    if a01 == 'n':
                        print('\n')
                        break
                    print('\n')
        a001 = t1[1]

    elif a001 == 'Ranking Athletes':
        print('\nNow we are going to create a list of peole and see their ranking in sports tournament;\n')
        while True:
            while True:
                a13 = md.intvalid(input('How many people you want in the tournment: '))
                if a13 < 3:
                    print('We need at least 3 people in this tournment.')
                elif a13 > 10:
                    print('You will have to give me their names, it will be tiring to name this many people')
                elif a13 >= 3 and a13 <= 10:
                    break
                else:
                    print(rd.randbytes(256))
            
            t02 = [] #define empty list
            for i in range(1, a13+1):
                a14 = input(f'Type the name of the {i} competitor: ')
                t02.append(a14)
            t03 = rd.sample(t02, a13) #use random to reorder the values


            print(f'Your competitors were: {t02}')
            print(f'They were ranked: {t03}')

            print('\n')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]
        
    elif a001 == 'Normalize Text':
        while True:
            print('\nNow we are going to manipulate text. Type using special characters (ç, à, õ, ...) and it will return the text properly formated\n')

            a15 = input('Type a sentence: ')
            col = a15.split() #Split the text. Since it's empty, it's using the whitespace as separator
            length = (len(col))

            # print(length)
            print('\n')
            #This loop uses the module 'unicodedata.normalize' to remove special characters. My def also makes all the characters uppercase, to make it a standard.
            for i in range(0, length):
                col[i] = md.normalize_text(col[i]) 
                print(col[i])
            print('\n')

            b28 = a15.strip() #removes outsides whitespaces
            b29 = a15.upper() #manipulate the text: .upper(), .lower(), .title(), etc
            #b30 = a15.count('text') #how many time text appears in the string
            #b31 = a15.replace('text1','text2') #replace every text1 for a text2
            #b32 = a15.find('text') #returns the position of text1 in the string
            print(a15)
            print('\n')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]
    
    elif a001 == 'Compound Interest':
        while True:
            a17 = md.intvalid(input("You've got an investment of $100 that yields 10% every year, how many years from now you want to know your net worth?  "))
            a18 = 100
            print('\n')
            for i in range(0, a17+1):
                print(f'Year {i}: {a18:.2f}')
                a18 = a18*1.1
            print('\n')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]

    elif a001 == 'Car Ticket':
        while True:
            a19 = md.intvalid(input('You were on a car trip. What was your max speed? '))
            b35 = 60
            b36 = 12
            b37 = a19 - b35
            #from 60 to 65, the ticket is 5, for every km above 65, there will be a 15% increase on the ticket. if a19 < 60, nothing happens
            if b37 <= 0:
                print('Ok, you were under the limit of 60, nothing happened!')
            elif b37 > 0 and b37 <= 5:
                print(f'You exceeded the speed limit by up to 5 mph, your ticket is: ${b36}')
            elif b37 > 5:
                b39 = b37 - 5
                b38 = b36 * math.pow(1.15, b39)
                print(f"You exceeded the speed limit by over 5, for every 1 mph above this range, there's a 15% increase in your ticket; \nYour ticket is: ${b38:.2f}\n")
            else:
                print('Error')
        
            print('\n')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]

    elif a001 == 'House Loan':        
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
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]

    elif a001 == 'Reverse Counting':
        for i in range(0, 11):
            a4 = 10 - i
            print(a4)
            time.sleep(1)

        if a4 == 0:
            print('boom!')

        print('\n')
        a001 = t1[1]

    elif a001 == 'Count Evens':
        while True:
            a5 = md.intvalid(input('Type any number: '))
            b6 = 0
            for i in range(0, a5+1):
                a6 = i % 2
                if a6 == 0:
                    b6 += 1
            print(f'There are {b6} even numbers between 0 and {a5}')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]    

    elif a001 == 'Sum of Multiples of Three':
        while True:
            a7 = md.intvalid(input('Type any other number: '))
            b7 = []
            for i in range (0, a7+1):
                a8 = i % 2
                a9 = i % 3
                if a9 == 0 and a8 != 0:
                    b7.append(i)

            b8 = sum(b7)
            print(f'\nThe sum of all multiples of three (not even) between 1 and {a7} is: {b8}\n')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]

    elif a001 == 'Arithmetic Sequence I':
        while True:
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
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]

    elif a001 == 'Arithmetic Sequence II':
        while True:
            b11 = md.ynvalid(input('We are going to create an Arithmetic Sequence again. Do you want to input new values (if you have not done topic 15, type "y")? [y/n]: '))
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
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]


    elif a001 == 'Guess 0 to 10':
        while True:
            while True:
                a25 = rd.randint(0,10)
                a26 = md.intvalid(input('Guess a number between 0 to 10: '))
                if a25 == a26:
                    print(f'Congatulations! {a26} was the right number!')
                    break
                else:
                    print(f'You missed... The right number was {a25}')
            a01 = md.ynvalid(input('Would you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]

    elif a001 == 'Calculate Factorial':
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
            a01 = md.ynvalid(input('\nWould you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]

    elif a001 == 'Display Fibonacci':
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
            a01 = md.ynvalid(input('\nWould you like to try again? [y/n]: '))
            if a01 == 'n':
                print('\n')
                break
            print('\n')
        a001 = t1[1]



print('Thanks for trying this code!')