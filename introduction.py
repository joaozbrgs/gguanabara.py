import time

#Tuples '()'
t1 = (
    12,
    31,
    14,
    'john',
    True,
    8.5
)
print(f'\n', '=' * 30, f'\n') 
print(t1[0])
print(t1[0:3])
print(t1[3])
print(t1[-1])
print(t1[0:])
print(f'\n', '=' * 30, f'\n') 

for i in t1:
    print(i)

print(f'\n', '=' * 30, f'\n') 
 
enumerate(t1) #returns the position of each character in the compound object
#print(sorted(t1)) #organize the items in the tuple. since it's immutable, it only displays organized, but won't acually change the order of the items.
print(t1.count(12)) #how many times has it appeared

lenght = len(t1)
print(lenght, f'\n')

#lists'[]'
l1 = [
    91,
    7,
    'Matt',
    False,
    3.1408
]

print(f'\n', '=' * 30, f'\n') 
for c in l1:
    print(c)
print(f'\n', '=' * 30, f'\n') 

#it can be actually reorganized and manipulated, unlike the tuples
#l1 = sorted(l1) #organize it if contains only numbers
for o in l1:
    print(o)
print(f'\n', '=' * 30, f'\n') 

a1 = 'Zeze'
a2 = 1441

l1.append(a1) #add a new item from to the list
l1[3] = True #change a value directly 
l1.insert(0,'New 91')

for n in l1:
    print(n)

print(f'\n', '=' * 30, f'\n') 

# del l1(3)
print(f'\n', '=' * 30, f'\n') 
l1.pop()
l1.remove(l1[4])
print(l1)
print('the command (pop) and (remove) took out the Zeze and the True from the list')


#quick way to create a new list
l2 = list(range(0,11))
print(f'\n', '=' * 30, f'\n') 
print(l2)
print(f'\n', '=' * 30, f'\n') 
l2.sort(reverse=True)
print(l2)
print(f'\n', '=' * 30, f'\n') 

for v in l2:
    print(f'{v}...')
    time.sleep(1.1)

print(f'\n', '=' * 30, f'\n') 


#linking lists
l01 = [2,4,6,10,12]
l02 = l01
print(f'List A: {l01}')
print(f'List B: {l02}')

l02[3] = 420
print(f'List A: {l01}. Realize that I changed the value on the List B, but both received the new 420 becuase they are connected')
print(f'List B: {l02}')

print(f'\n', '=' * 30, f'\n') 

l01 = [2,4,6,10,12]
l02 = l01[:] #this is the secret, now they have the same values, but are not connected
print(f'List A: {l01}')
print(f'List B: {l02}')

l02[3] = 420
print(f"List A: {l01}. Realize that now the List A didn't receive the new value 420")
print(f'List B: {l02}')






