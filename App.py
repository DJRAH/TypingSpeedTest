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
        self.root.geometry('%dx%d+%d+%d' % (w-500, self.h-40, xx+140, yy))
        self.root.resizable(False,False)

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        #instruction
        self.frame_desc = ttk.LabelFrame(self.frame, text="Description ")
        self.frame_desc.grid(row=0, column=0, padx=20, pady=40)

        
        self.label1 = ttk.Label(self.frame_desc, text="Type words bellow during one minute.").grid(row=0, column=0)
        self.label2 = ttk.Label(self.frame_desc, text="Space between each world.").grid(row=1, column=0, )
        self.label3 = ttk.Label(self.frame_desc, text="Receive your score : CPM and WPM").grid(row=2, column=0)
        
        for widget in self.frame_desc.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # timer
        self.frame_timer = ttk.LabelFrame(self.frame, text="")
        self.frame_timer.grid(row=0, column=1, padx=20, pady=10)

        self.timerRest = Button(self.frame_timer, text="Restart", border=None).grid(row=0, column=0)
        self.timerLabel = Label(self.frame_timer, text="", width=10, height=3,bg="white").grid(row=1, column=0)

        #typing
        self.frame_typing = ttk.LabelFrame(self.frame, text="")
        self.frame_typing.grid(row=1, column=0,columnspan=2, padx=20, pady=0)

        self.parag = Text(self.frame_typing ,width=50, height=12, highlightbackground="white").grid(row=0, column=0)
        self.type_text = Text(self.frame_typing, width=30, height=1.5, highlightbackground="#091057").grid(row=1, column=0) 


        # result
        self.frame_res = ttk.LabelFrame(self.frame, text="Result ")
        self.frame_res.grid(row=2, column=0,columnspan=2, padx=20, pady=40)

        self.CPM = Label(self.frame_res, text="CPM").grid(row=0, column=0)
        self.CPM_txt = Label(self.frame_res, text="", width=10, bg="white", height=2).grid(row=1, column=0)
        self.WPM = Label(self.frame_res, text="WPM").grid(row=0, column=1)
        self.WPM_txt = Label(self.frame_res, text="", width=10, bg="white",height=2).grid(row=1, column=1)

        for widget in self.frame_res.winfo_children():
            widget.grid_configure(padx=60, pady=5)

        self.root.mainloop()
       

        

       