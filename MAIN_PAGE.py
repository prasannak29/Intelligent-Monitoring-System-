from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk 
from tkinter import filedialog

import time

project_name = "SUSPICIOUS ACTIVITY DETECTION"

from tkinter import Tk, Label, Entry, Toplevel, Canvas

from PIL import Image, ImageDraw, ImageTk, ImageFont
image = Image.open('SC.jpeg')

import RESULT

########################################################################################    
def LOGIN_PAGE():
    login_page = Tk()
    login_page.geometry("1300x900+80+80")
    login_page.configure(background="#ffff8f")

    def LOGIN():

        def login_button():
            print("Login button")
            login_page.destroy()                    
            RESULT.get()

        def exit():
            global off
            off = 1
            login_page.destroy()
            
        photoimage = ImageTk.PhotoImage(image)
        Label(login_page, image=photoimage).place(x=0,y=0)

        label2 = Label(login_page, text=project_name)
        label2.configure(background="#ffffff")
        label2.configure(foreground="#0000ff")
        label2.config(font=("Times new roman", 35))
        label2.place(x = 0,y=15,height=40, width=1300)

        B1 = Button(login_page, text = "Start", command = login_button)
        B1.place(x = 550,y = 300 ,height=40, width=200)
        B1.config(font=("Courier", 17))
        B1.configure(background="#fffff0")

        B1 = Button(login_page, text = "Exit", command = exit)
        B1.place(x = 1180,y = 550 ,height=40, width=100)
        B1.config(font=("Courier", 17))
        B1.configure(background="#fffff0")

        login_page.mainloop()

    LOGIN()

global off
off = 0

while True:
    LOGIN_PAGE()
    if(off==1):
        break

