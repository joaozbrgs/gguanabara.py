import math

#This program is intended to calculate the populational growth of given society;
#Here are the rules:
#1. Population starts as 8, and all the time there will be a 50/50 distribution of men and women
#2. Every generation will last 50 years and all the couples will have 8 kids
#3. Each individual only survives for 2 generations
#4. The individuals from the previous generation can have kids, but should be counted
#5. The total amount of people on each generation will be (1: The people from the previous, 2: Adults from the current, 3: Children from the current)

# def generation(pop):
#     a0 = pop
#     a1 = pop/2 #divide in couples 
#     a2 = a1 * 8 #8 kids for each couple
#     a3 = a2 + a0
#     return a3



pop_01 = 8

b1 = generation(pop_01)
print(b1)

for i in range(0,19):
    
    a0 = pop_01
    a1 = pop_01/2 #divide in couples 
    a2 = a1 * 8 #8 kids for each couple
    a3 = a2 + a0
