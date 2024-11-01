from tkinter import *
from tkinter import Tk, ttk
import requests

class App:

    def __init__(self):

        self.root = Tk()

        #used varibales for words displays
        self.begin_index=0
        self.end_index = 50

        #variables for typed word
        self.word_act=""
        self.tap_count=0

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

        
        self.label1 = ttk.Label(self.frame_desc, text="Type words bellow during one minute.")
        self.label1.grid(row=0, column=0)
        self.label2 = ttk.Label(self.frame_desc, text="Space between each world.")
        self.label2.grid(row=1, column=0, )
        self.label3 = ttk.Label(self.frame_desc, text="Receive your score : CPM and WPM")
        self.label3.grid(row=2, column=0)
        
        for widget in self.frame_desc.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # timer
        self.frame_timer = ttk.LabelFrame(self.frame, text="")
        self.frame_timer.grid(row=0, column=1, padx=20, pady=10)

        self.timerRest = Button(self.frame_timer, text="Restart", border=None)
        self.timerRest.grid(row=0, column=0)
        self.timerLabel = Label(self.frame_timer, text="", width=10, height=3,bg="white")
        self.timerLabel.grid(row=1, column=0)

        #typing
        self.frame_typing = ttk.LabelFrame(self.frame, text="")
        self.frame_typing.grid(row=1, column=0,columnspan=2, padx=20, pady=0)

        self.parag = Text(self.frame_typing,wrap = WORD ,width=50, height=12, highlightbackground="white")
        self.parag.grid(row=0, column=0)
        self.type_text = Text(self.frame_typing, width=30, height=1.5, highlightbackground="#091057")
        self.type_text.grid(row=1, column=0) 


        # result
        self.frame_res = ttk.LabelFrame(self.frame, text="Result ")
        self.frame_res.grid(row=2, column=0,columnspan=2, padx=20, pady=40)

        self.CPM = Label(self.frame_res, text="CPM")
        self.CPM.grid(row=0, column=0)
        self.CPM_txt = Label(self.frame_res, text="", width=10, bg="white", height=2)
        self.CPM_txt.grid(row=1, column=0)
        self.WPM = Label(self.frame_res, text="WPM")
        self.WPM.grid(row=0, column=1)
        self.WPM_txt = Label(self.frame_res, text="", width=10, bg="white",height=2)
        self.WPM_txt.grid(row=1, column=1)

        for widget in self.frame_res.winfo_children():
            widget.grid_configure(padx=60, pady=5)

        #get word from website 
        self.get_words()
        
        #show word on gui
        self.show_words()
        
        #bind keyboard
        self.root.bind("<Key>", self.key_event)

        self.root.mainloop()

    def update_text(self):
        new_word = self.words[(self.end_index)-1]
        word_del = self.words[(self.begin_index)-1]
        ind = len(word_del)+1
        st = str('1.'+str(ind))
        print(word_del)
        (self.parag).delete("1.0", st)
        (self.type_text).delete("1.0",END)
        (self.parag).insert(END, new_word +" ")
        self.word_act = self.words[self.begin_index]
        self.tap_count=0




    def key_event(self, event):
        
        #if the use enter charactere
        if event.widget == self.type_text:

            if(event.keysym=='space'):

                if self.tap_count==len(self.word_act)==(len(self.type_text.get("1.0",END))-2):
                    self.begin_index+=1
                    self.end_index+=1
                    self.update_text()                
            else:
                if self.tap_count<len(self.word_act):
                    if event.char==(self.word_act[self.tap_count]):
                        self.tap_count+=1
                        #colorer la lettre et tous le mot tapé
                        st = "1."+ str(self.tap_count)
                        self.parag.tag_add('color',"1.0",st)
                        self.parag.tag_config('color', background="yellow")
                        self.type_text.tag_add('color',"1.0",st)
                        self.type_text.tag_config('color', background="yellow")
                        





    def show_words(self):
        txt = ""
        for i in range(0, 50):
            txt+=self.words[i]+" "
        
        (self.parag).insert(INSERT, txt)
        self.word_act=self.words[0]
        self.tap_count=0
 
    def get_words(self):
        self.words = []

        #cal restfull api at 
        self.res = requests.get("https://random-word-api.herokuapp.com/word?number=500")
        if self.res.status_code!=200 :
            print("error somewhere with API's website")
        else :
            for word in self.res.json():
                self.words.append(word)
                print(word)
            

       