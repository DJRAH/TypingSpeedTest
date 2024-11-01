from tkinter import *
from tkinter import Tk, ttk, messagebox
import requests, time, sys

#1 minute counter
COUNT=60

class App:

    def __init__(self):

        self.root = Tk()
        
        #var used for time
        self.timer=COUNT
        self.user_word_entered=0
        self.user_char_entered=0
        #used varibales for words displays
        self.begin_index=0
        self.end_index = 20

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
        self.root.geometry('%dx%d+%d+%d' % (w-400, self.h+80, xx+140, yy-20))
        self.root.resizable(False,False)

        self.root.title("Typing Speed Test (DjRAH)")
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
        self.timerRest = Button(self.frame_timer, text="Restart", border=None, command=self.restart)
        self.timerRest.grid(row=0, column=0)
        self.timerLabel = Label(self.frame_timer, text="", width=10, height=3,bg="white", font='Helvetica 15 bold')
        self.timerLabel.grid(row=1, column=0)

        #typing
        self.frame_typing = ttk.LabelFrame(self.frame, text="")
        self.frame_typing.grid(row=1, column=0,columnspan=2, padx=20, pady=0)
        self.parag = Text(self.frame_typing,wrap = WORD ,width=50, height=12, highlightbackground="white",font='Helvetica 13 bold', padx=20, pady=20)
        self.parag.grid(row=0, column=0)
        self.type_text = Text(self.frame_typing, width=30, height=1, highlightbackground="#091057", font='Helvetica 15 bold', padx=20, pady=20)
        self.type_text.grid(row=1, column=0) 

        # result
        self.frame_res = ttk.LabelFrame(self.frame, text="Result ")
        self.frame_res.grid(row=2, column=0,columnspan=2, padx=20, pady=40)
        self.label12 = ttk.Label(self.frame_res, text="You typed :")
        self.label12.grid(row=0, column=0)
        self.res_text = Label(self.frame_res, text="Not Yet",background="yellow", font='Helvetica 11 bold')
        self.res_text.grid(row=0, column=1)

        self.CPM = Label(self.frame_res, text="CPM")
        self.CPM.grid(row=1, column=0)
        self.CPM_txt = Label(self.frame_res, text="", width=10, bg="white", height=2, font='Helvetica 15 bold')
        self.CPM_txt.grid(row=2, column=0)
        self.WPM = Label(self.frame_res, text="WPM")
        self.WPM.grid(row=1, column=1)
        self.WPM_txt = Label(self.frame_res, text="", width=10, bg="white",height=2, font='Helvetica 15 bold')
        self.WPM_txt.grid(row=2, column=1)

        self.label11 = ttk.Label(self.frame_res, text="Average Word/Minute (WPM) is 3.3 !! (200words/Min)",background="yellow", font='Helvetica 11 bold')
        self.label11.grid(row=3, column=0, columnspan=2)

        for widget in self.frame_res.winfo_children():
            widget.grid_configure(padx=60, pady=5)

        #get word from website's API
        self.get_words()
        
        #show word on gui
        self.show_words()
        
        #bind keyboard for user type
        self.root.bind("<Key>", self.key_event)

        self.root.mainloop()


    #update the text given to user
    def update_text(self):
        new_word = self.words[(self.end_index)-1]
        word_del = self.words[(self.begin_index)-1]
        ind = len(word_del)+1
        st = str('1.'+str(ind))
        
        self.parag.configure(state='normal')
        (self.parag).delete("1.0", st)
        (self.type_text).delete("1.0",END)
        (self.parag).insert(END, new_word +" ")
        self.parag.configure(state='disabled')
        self.word_act = self.words[self.begin_index]
        self.tap_count=0
        
        #update stats for WPM CPM
        self.user_char_entered+=ind
        self.user_word_entered+=1


    #running countdown and show stats
    def countdown(self):
        #affichage du compteur
        self.timer-=1
        self.timerLabel.config(text = str(self.timer).upper(), background="red", foreground="white")
        
        if self.timer==0:#expired countdown
            self.type_text.configure(state='disabled')
            messagebox.showinfo("One minute left !", "See below your stats !!")
            
            wpm = str(round(self.user_word_entered/60,1))
            cpm = str(round(self.user_char_entered/60,1))
            res_txt = str(self.user_word_entered)+" words & "+str(self.user_char_entered)+" chars"
            self.res_text.config(text=res_txt)
            self.WPM_txt.configure(text=wpm)
            self.CPM_txt.config(text=cpm)

            return

        self.timerLabel.after(1000,self.countdown)

        

    def key_event(self, event):
        
        #if the use enter charactere
        if event.widget == self.type_text:

            #start typing
            if self.timer==COUNT:
                self.countdown()

            #check if the word is fully entered by user
            if(event.keysym=='space'):

                if self.tap_count==len(self.word_act)==(len(self.type_text.get("1.0",END))-2):
                    self.begin_index+=1
                    self.end_index+=1
                    self.update_text()       

            else:
                #check if the user char entered is correct, and color it if so
                if self.tap_count<len(self.word_act):
                    if event.char==(self.word_act[self.tap_count]):
                        
                        if self.word_act.find(self.type_text.get("1.0",END).removesuffix("\n"))==0:#si il ya une lettre erroné 
                            self.tap_count+=1
                            #colorer la lettre et tous le mot tapé
                            st = "1."+ str(self.tap_count)
                            self.parag.configure(state='normal')
                            self.parag.tag_add('color',"1.0",st)
                            self.parag.tag_config('color', background="yellow")
                            self.parag.configure(state='disabled')

                            self.type_text.tag_add('color',"1.0",st)
                            self.type_text.tag_config('color', background="yellow")
                        
    #initial text shown to the user
    def show_words(self):
        txt = ""
        for i in range(0, 50):
            txt+=self.words[i]+" "
        self.parag.configure(state='normal')
        (self.parag).insert(INSERT, txt)
        self.parag.configure(state='disabled')
        self.word_act=self.words[0]
        self.tap_count=0
 
    #get words from remote website
    def get_words(self):
        self.words = []

        #cal restfull api at 
        self.res = requests.get("https://random-word-api.herokuapp.com/word?number=500")
        if self.res.status_code!=200 :
            print("error somewhere with API's website")
        else :
            for word in self.res.json():
                self.words.append(word)

    #when restart button clicked    
    def restart(self):
        self.root.after(1,self.root.destroy())
        App()
        
