from tkinter import *
import keyboard
from binds import Binds
import pyautogui
from save_binds import SaveFiles
import os

class Interface:
    pyautogui.FAILSAFE = False
    def __init__(self):
        self.tk = Tk()
        self.tk.resizable(width = False,height = False)
        self.tk["bg"] = '#2F2E33'
        self.tk.geometry('400x420')
        self.tk.title('Binder by Miha v 2.1.1')
        self.tk.iconbitmap('D:/Py/binder/Binder-Clip-icon.ico')
        self.save_but = Button(text="Save", command=self.save_text,background="#555",width = 20)
        self.save_but.grid(row = 10,column = 2)
    

class InterfaceLogic(Interface,Binds,SaveFiles):
    @property
    def text_from_entrys(self):
        return [self.e3.get(),self.e4.get(),self.e5.get(),self.e6.get(),self.e7.get(),self.e8.get(),self.e9.get(),self.e10.get(),self.e11.get(),self.e12.get()]
    
    def initButton(self):
        self.save_but = Button(text="Save", command=self.save_text,background="#555",width = 20)
        self.save_but.grid(row = 10,column = 2)

    def initLabels(self):
        for i in range(3,13):
          label = Label(self.tk,text = 'f'+ str(i),font = 'Consolas 20',bg = '#2F2E33',fg = '#F0FFFF').grid(row = i - 3)

    def initEntrys(self):
        self.e3 = Entry(width = 55,bg = '#54535E',bd = 2)
        self.e4 = Entry(width = 55,bg = '#54535E',bd = 2)
        self.e5 = Entry(width = 55,bg = '#54535E',bd = 2)
        self.e6 = Entry(width = 55,bg = '#54535E',bd = 2)
        self.e7 = Entry(width = 55,bg = '#54535E',bd = 2)
        self.e8 = Entry(width = 55,bg = '#54535E',bd = 2) 
        self.e9 = Entry(width = 55,bg = '#54535E',bd = 2)
        self.e10 = Entry(width = 55,bg = '#54535E',bd = 2)
        self.e11 = Entry(width = 55,bg = '#54535E',bd = 2)
        self.e12 = Entry(width = 55,bg = '#54535E',bd = 2)
    
    def gridEntrys(self):
        self.e3.grid(row = 0,column = 2)
        self.e4.grid(row = 1,column = 2)
        self.e5.grid(row = 2,column = 2)
        self.e6.grid(row = 3,column = 2)
        self.e7.grid(row = 4,column = 2)
        self.e8.grid(row = 5,column = 2)
        self.e9.grid(row = 6,column = 2)
        self.e10.grid(row = 7,column = 2)
        self.e11.grid(row = 8,column = 2)
        self.e12.grid(row = 9,column = 2)
    
    def insertText(self):
        if self.file_exist:
            self.e3.insert(0,self.saved_binds[0])
            self.e4.insert(1,self.saved_binds[1])
            self.e5.insert(2,self.saved_binds[2])
            self.e6.insert(3,self.saved_binds[3])
            self.e7.insert(4,self.saved_binds[4])
            self.e8.insert(5,self.saved_binds[5])
            self.e9.insert(6,self.saved_binds[6])
            self.e10.insert(7,self.saved_binds[7])
            self.e11.insert(8,self.saved_binds[8])
            self.e12.insert(9,self.saved_binds[9])
            os.remove('binds.bin')
        
    
    

   
