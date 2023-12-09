import mydefs as md
import random as rd
import time

<<<<<<< HEAD
=======

<<<<<<< HEAD
# if a1 == 83:
# a831 = input('\nType your expression: ')
# l83 = list(a831)
# l83 = [char for char in l83 if not char.isspace()]

# b831 = l83.find('(', ')', '[', ']', '{', '}')

# print(l83)
# print(b831)


a = input('type here; ').upper()

print(a)
=======
l84 = list()
b1 = md.intvalid(input('How many people do you want in your list: '))
for i in range(0,b1):
    l841 = [
        input(f'What is the name of person {i+1}: '),
        md.floatvalid(input(f'What is the weight of person {i+1}: ')),
        md.intvalid(input(f'What is the age of person {i+1}: '))
    ]
        


    l84.append(l841[:])
print(l84)

# Sort the list based on weight and age
l84.sort(key=lambda x: (x[1], x[2]))
print('\n')
print('\n')
print(l84)

# print(f'\nThe list contains {len(l84)} people:\n')
# for i, p in enumerate(l84):
#     print(f'The {i+1} person was {p[0]}')
#     print(f"{p[0]}'s weight is {p[1]} and they're {p[2]} years old\n")
# print(f'In ascending order, the weight is: ', end='')
# for i in range(0, len(l84)):
#     print(f'-> {l84[i][1]}', end='')
# print('')
# print(f'In ascending order, the age is: ', end='')
# for i in range(0, len(l84)):
#     print(f'-> {l84[i][2]}', end='')
# print('')

# print('\n')
# print('\n')
# print()
>>>>>>> 2b2eface15fac3a549b96b5e47a5aac210558f22
>>>>>>> 1baa184a2ae852694f0ac0cdcee851777bb11e19
