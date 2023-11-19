import math


while True:
    a1 = 8
    gen = int(input('type the generation you want: '))

    if gen == 1:
        a2 = 8 * pow(2, gen-1)
    elif gen == 2:
        a2 = 8 * pow(2, gen-2) + 8 * pow(2, gen-1)
    elif gen >= 3:
        a2 = 8 * pow(2, gen-3) + 8 * pow(2, gen-2) + 8 * pow(2, gen-1)

    print('\n', '-'*30, '\n')
    print(a2)
    print('\n', '-'*30, '\n')
