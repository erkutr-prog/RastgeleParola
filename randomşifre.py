import random
import string
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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



def generate_and_show():
    pwd = password(length=length_var.get(), num=check_var.get(), strength=selected_diff.get())
    messagebox.showinfo("Message","Generated password is {} ".format(pwd))


tk = Tk()

frm = ttk.Frame(tk, padding=200)




frm.grid()
ttk.Label(frm , text="Şifre zorluğunu seçiniz:").grid(column=0, row=2)

selected_diff = StringVar(tk, value="zayıf")

dropdown_for_strength = ttk.Combobox(frm, textvariable=selected_diff)
dropdown_for_strength['values'] = ["zayıf","orta","güçlü"]

dropdown_for_strength['state'] = 'readonly'
dropdown_for_strength.grid(column=0, row=3)

ttk.Label(frm, text="Şifre uzunluğunu seçiniz:").grid(column=0,row=0)
length_var = IntVar(tk, value=8)

length_of_pwd = ttk.Entry(frm,textvariable=length_var).grid(column=0,row=1)

check_var = BooleanVar(tk)
check_box = ttk.Checkbutton(frm, text="Number",variable=check_var)
check_box.grid(column=0,row=4)


button =  ttk.Button(frm , text="GENERATE", command=generate_and_show)
button.grid(column=0, row=10)



tk.mainloop()