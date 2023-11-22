import mydefs as md


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