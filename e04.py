<<<<<<< HEAD
import mydefs as md

=======
import math
import mydefs as md

print('-=' * 30, '\n')
a1 = 'Calculate Compound Interest\n'
print(f'{a1: ^30}')
print('-=' * 30, '\n')

while True:
    b1 = (input(': '))
    C = md.floatvalid(input('Type the initial amount: '))
    Inc = md.floatvalid(input('Type the monthly apport: '))
    I = md.floatvalid(input('Type the interest rate: '))
    t = md.intvalid(input('Type the amount of periods: '))

    i = 1
    while i <= t:
        M = C * (1 + I) + Inc
        C = M
        print(f'{M:.1f}')
        i+=1



M = C(math.pow((1 + I), t)) + (t*Inc)
>>>>>>> 1baa184a2ae852694f0ac0cdcee851777bb11e19
