#!/usr/bin/env python3
# Marcos del Cueto - 11/2019
# Simple python code to generate several random passwords with varying length
# Can select what type(s) of characters will be used
# Note that each character in random and independent of previous values: characters can be repeated
import random
import string
import tkinter as tk
from tkinter import *

common_symbols='.-_$*()#@!%/'   # define string with common symbols
rare_symbols=''                 # initialize string with rare symbols
for i in string.punctuation:    # create string with rare symbols
    if i not in common_symbols: rare_symbols=rare_symbols+i

# Function to print verbose information
#def var_states():
    #print("Lowercase: %d,\nUppercase: %d,\nNumber: %d,\nCommon Symbols: %d,\nrare Symbols: %d" % (var1.get(), var2.get(), var3.get(), var4.get(), var5.get()))
    #print("Number of passwords: %i,\nLength of each password: %i" % (int(e1.get()),int(e2.get())))

# Function to create strings with random characters
def randomString():
    # initialize variables
    v1=var1.get()
    v2=var2.get()
    v3=var3.get()
    v4=var4.get()
    v5=var5.get()
    password_length=int(e2.get())
    Npassword=int(e1.get())
    result['text']=''
    # generate 'Npassword' passwords, each with length 'password_length'
    for i in range(Npassword):
        password_characters=''
        if v1==1: password_characters=password_characters+string.ascii_lowercase    # add lowercase
        if v2==1: password_characters=password_characters+string.ascii_uppercase    # add uppercase
        if v3==1: password_characters=password_characters+string.digits             # add digits
        if v4==1: password_characters=password_characters+common_symbols            # add common symbols
        if v5==1: password_characters=password_characters+rare_symbols              # add rare symbols
        one_password= ''.join(random.choice(password_characters) for i in range(password_length))
        result['text']=result['text']+"\n"+one_password

# Use Tkinter to open window to prompt user and read options
master = Tk()
# Initialize variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
e1   = IntVar()
e2   = IntVar()

Label(master, text="Select options to generate your password(s):").pack()

Checkbutton(master, text="Lowercase", variable=var1).pack()
Checkbutton(master, text="Uppercase", variable=var2).pack()
Checkbutton(master, text="Number", variable=var3).pack()
Checkbutton(master, text="Common Symbols", variable=var4).pack()
Checkbutton(master, text="Rare symbols", variable=var5).pack()

tk.Label(master, text="Number of passwords").pack()
tk.Entry(master,textvariable=e1).pack()
tk.Label(master, text="Length of passwords").pack()
tk.Entry(master,textvariable=e2).pack()


#Button(master, text='Show options:', command=var_states).pack()
Button(master, text='Show password', command=randomString).pack()
Button(master, text='Quit', command=master.quit).pack()
result=tk.Label(master,text="Resulting password(s):")
result.pack()


mainloop()
