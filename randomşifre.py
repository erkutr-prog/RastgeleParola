import random
import string

def password(length,num=False,strength='zayıf'):
    """şifrenin uzunluğu, sayı istiyorsanız num,ve şifrenin gücü(zayıf,orta,güçlü)"""   
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    if strength == 'zayıf':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)
    elif strength == 'orta':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letter)
    elif strength == 'güçlü':
        ran = random.randint(2,4)
        if num:
            length -= ran
            for i in range(ran):
                pwd += random.choice(dig)
        ran2 = random.randint(1,3)
        length -= ran2
        for i in range(ran2):
            pwd += random.choice(punct)
        for i in range(length):
            pwd += random.choice(letter)

    pwd = list(pwd)
    random.shuffle(pwd)
    return ''.join(pwd)

print("Zayıf şifre",password(5,True))

print("Güçlü şifre",password(10,True,'orta'))

print("Çok güçlü şifre",password(15,True,'güçlü'))

