import random as rd
import unicodedata
error = ('type a valid answer: ')
yes_or_no = ('type "y" for YES and "n" for NO: ')
n_or_p = 'type "n" for NEXT and "p" for PREVIOUS: '

def strvalid(text1):
    while True:
        try:
            m1 = str(text1).strip()
            break
        except ValueError:
            text1 = input(error)
    return m1
        
def intvalid(text2):
    while True:
        try:
            m2 = int(text2)
            if m2 >= 0:
                break
            else:
                m2 = m2 * -1
                break
        except ValueError:
            text2 = input(error)
    return m2

def floatvalid(text4):
    while True:
        try:
            m2 = float(text4)
            if m2 >= 0:
                break
            else:
                m2 = m2 * -1
                break
        except ValueError:
            text4 = input(error)
    return m2

def isprime(text3):
    t01 = 0
    for i in range(1, text3+1):
        if text3 % i == 0:
            t01 += 1
    # if t01 > 2:
    #     m03 = ('FALSE')
    # elif t01 == 2:
    #     m03 = ('TRUE')
    # else:
    #     m03 = t01
    
    # m03 = t01 > 2 ? ('FALSE') : t01 == 2 ? ('TRUE') : t01

    m03 = ('FALSE') if t01 > 2  else ('TRUE') if t01 == 2 else t01
    
    return m03

def ynvalid(text4):
    while True:
        m04 = text4.lower().strip()
        if m04 == 'y' or m04 == 'n':
            break
        else:
            text4 = input(yes_or_no)
    return m04

def npvalid(text4):
    while True:
        m04 = text4.lower().strip()
        if m04 == 'n' or m04 == 'p':
            break
        else:
            text4 = input(n_or_p)
    return m04

def s_triangle():
    while True:
        t01 = []
        for i in range(0,3):
            b25 = rd.randint(1,100)
            t01.append(b25)
        t01.sort()
        a10 = t01[0] + t01[1]
        a11 = t01[2]
        if a10 > a11:
            break
    return t01

def normalize_text(text5):
    
    #normalize the text to NFKD format
    text5 = unicodedata.normalize("NFKD", text5)
    #encode using only ascii characters
    text5 = text5.encode('ascii', 'ignore')
    #decode the text back to string, in the desired standard, in this case 'utf-8'
    text5 = text5.decode('utf-8')
    #transform all characters in uppercase
    text5 = text5.upper()

    return text5

def specialint(text7):
    while True:
        try:
            m2 = int(text7)
            if m2 >= 0:
                break
            else:
                m2 = m2 * -1
                break
        except ValueError:
            if text7.strip().isalpha():
                m2 = npvalid(text7)
                break
            else:
                text2 = input(error)
    return m2

