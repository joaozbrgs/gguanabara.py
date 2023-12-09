import random as rd

pool = []
for i in range(1,61):
    pool.append(i)

result = [12, 13, 37, 44, 48, 51]
game1 = sorted(rd.sample(pool, 6))
i = 0

while result != game1:
    print(game1, '\n')
    game1 = sorted(rd.sample(pool, 6))
    i += 1
    # if i > 5:
    #     break

print('=' * 30)
print('\n')
print(game1, '\n')
print(i)
print('\n')
print('=' * 30)