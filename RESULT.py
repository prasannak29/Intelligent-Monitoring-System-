from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk 
from tkinter import filedialog

import time

import TESTING_with_BOX

project_name = "SUSPICIOUS ACTIVITY DETECTION"


from tkinter import Tk, Label, Entry, Toplevel, Canvas

from PIL import Image, ImageDraw, ImageTk, ImageFont
image = Image.open('SC.jpeg')


########################################################################################    
def get():
    login_page = Tk()
    login_page.geometry("1300x600+30+30")
    login_page.configure(background="#ffff8f")

    def LOGIN():

        def GET_VIDEO():
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
            root.destroy()
            TESTING_with_BOX.get(file_path)

        def GET_VIDEO_0():
            TESTING_with_BOX.get(0)

        photoimage = ImageTk.PhotoImage(image)
        Label(login_page, image=photoimage).place(x=0,y=0)

        label2 = Label(login_page, text=project_name)
        label2.configure(background="#ffffff")
        label2.configure(foreground="#0000ff")
        label2.config(font=("Times new roman", 35))
        label2.place(x = 0,y=15,height=40, width=1300)

        B1 = Button(login_page, text = "UPLOAD VIDEO", command = GET_VIDEO)
        B1.place(x = 600,y = 200 ,height=35, width=200)
        B1.configure(background="#fffff0")


        B1 = Button(login_page, text = "Live Stream (Future)", command = GET_VIDEO_0)
        B1.place(x = 600,y = 300 ,height=35, width=200)
        B1.configure(background="#fffff0")



        login_page.mainloop()

    LOGIN()


