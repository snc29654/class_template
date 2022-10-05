### インポート
import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import threading
import time


class main_class():  
    def __init__(self, main):
        print ("__init__")  
        button1= Button(root, text=u'終了', command=self.quit)  
        button1.grid(row=0, column=1)  
        button1.place(x=90, y=10) 
        self.textExample=ScrolledText(root, height=30,width=80, wrap=tkinter.CHAR)
        self.textExample.pack()
        self.textExample.place(x=90, y=70)
    def method0(self,message):  
        print ("method0")  
        self.textExample.insert(tkinter.END,message)

    def thread_method(self):
        while(1):
            result=0
            for i in range(30):
                self.textExample.insert(tkinter.END,str(result)+"\n")
                result = result + 1
                time.sleep(0.1)
                self.textExample.yview_moveto(1)
                self.textExample.configure(height=i,width=i*2)

    def quit(self):
        print ("quit")  
        root.destroy()

root= tkinter.Tk()  
c=main_class(root)  
root.title("表題")  
root.geometry("800x500") 

thread1 = threading.Thread(target=c.thread_method)
thread1.start()

root.mainloop()


    
