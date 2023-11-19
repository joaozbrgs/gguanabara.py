import math

#This program is intended to calculate the populational growth of given society;
#Here are the rules:
#1. Population starts as 8, and all the time there will be a 50/50 distribution of men and women
#2. Every generation will last 50 years and all the couples will have 8 kids
#3. Each individual only survives for 2 generations
#4. The individuals from the previous generation can have kids, but should be counted
#5. The total amount of people on each generation will be (1: The people from the previous, 2: Adults from the current, 3: Children from the current)

while True:
    t1 = [8, 32, 128]
    gen = int(input('Type the generation you want: '))

    if len(t1) >= gen:
        if gen == 1:
            r2 = t1[0]
        elif gen == 2:
            r2 = t1[1] + t1[0]
        elif gen == 3:
            r2 = t1[2] + t1[1] + t1[0]
    else:
        for i in range(len(t1) + 1, gen + 1):
            a1 = t1[-1] * 4
            t1.append(a1)
            r3 = t1[-1] + t1[-2] + t1[-3]

    if gen <= 3:
        print(r2)
    else:
        print(r3)

    print('\n', '-'*30, '\n')
    print(t1)
    print('\n', '-'*30, '\n')



