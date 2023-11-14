import mydefs as md


l5 = [0,0,0,0,0]
n = 0
while len(l5) <= 5:
    b2 = int(input('Type a number: '))
    if b2 in l5:
        print("This value was already on the list and won't be added")
    else:
        b9 = len(l5)
        # for i in range(0, b9):
