from tkinter import *
from tkinter import Tk, ttk

class App:

    def __init__(self):

        self.root = Tk()
        #define geometry
        w = 1000
        self.h = 700
        ws = self.root.winfo_screenwidth()  
        hs = self.root.winfo_screenheight()
        xx = (ws/2) - (w/2)
        yy = (hs/2) - (self.h/2)
        self.root.geometry('%dx%d+%d+%d' % (w-380, self.h, xx+150, yy))
        self.root.resizable(False,False)
        
        self.label = ttk.Label(text="").grid(row=1, column=0, columnspan=4)
        self.label1 = ttk.Label(text="      Type words bellow during one minute.").grid(row=2, column=0, columnspan=4)
        self.label2 = ttk.Label(text="      Space between each world.").grid(row=3, column=0, columnspan=4)
        self.label3 = ttk.Label(text="      Receive your score : CPM and WPM").grid(row=4, column=0, columnspan=4)
        self.label4 = ttk.Label(text="").grid(row=5, column=0, columnspan=4)
        self.label4 = ttk.Label(text="").grid(row=6, column=0, columnspan=4)

       
        self.CPM = Label(text="     CPM : ").grid(row=7, column=0)
        self.CPM_txt = Label(text="   ", width=10, bg="white").grid(row=7, column=1)
        self.WPM = Label(text="     WPM : ").grid(row=7, column=2)
        self.WPM_txt = Label(text="   ", width=10, bg="white").grid(row=7, column=3)

        #self.label5 = ttk.Label(text="",width=75).grid(row=7, column=0, columnspan=4)
        self.label6 = ttk.Label(text="",width=75).grid(row=8, column=0, columnspan=4)
        self.label7 = ttk.Label(text="",width=75).grid(row=9, column=0, columnspan=4)

        self.time = Label(text="      CountDown : ").grid(row=10, column=1)
        self.time_txt = Label(text="   ", width=10, bg="white").grid(row=10, column=2)

        self.label8 = ttk.Label(text="",width=75).grid(row=12, column=0, columnspan=4)

        self.parag = Text(width=50, height=10, highlightbackground="white").grid(row=13, column=0, columnspan=4)
        self.type_text = Text(width=30, height=1.5, highlightbackground="#091057").grid(row=14, column=0, columnspan=4)
        

        self.root.mainloop()