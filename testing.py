import mydefs as md


# if a1 == 83:
a831 = input('\nType your expression: ')
l83 = list(a831)
l83 = [char for char in l83 if not char.isspace()]

b831 = l83.find('(', ')', '[', ']', '{', '}')

print(l83)
print(b831)
