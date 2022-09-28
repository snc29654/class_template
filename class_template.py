### インポート
import tkinter
from tkinter import *

class main_class():  
    def __init__(self, main):
        print ("__init__")  
        button1= Button(root, text=u'終了', command=self.quit)  
        button1.grid(row=0, column=1)  
        button1.place(x=120, y=80) 

    def method0(self):  
        print ("method0")  

    def quit(self):
        print ("quit")  
        root.destroy()

root= tkinter.Tk()  
c=main_class(root)  
root.title("表題")  
root.geometry("300x200") 
c.method0()
root.mainloop()


    
