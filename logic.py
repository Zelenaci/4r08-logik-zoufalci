#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:11:25 2019

@author: nov35102
"""


from os.path import basename, splitext
import tkinter as tk



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = 'Foo'

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.barvy = "#c90000 #99dd00 #0000ff #ffff00 #008888 #880088 "\
                     "#dd9900 #ffffff".split()
        self.sirka = 30
        self.vyska = 20
        
        
        
        
        # skrytá pole
        self.skryteBarvy = []
        for sloupec in range(5):
            c = tk.Canvas(self, background='black', width=self.sirka,
                          height=self.vyska)
            c.grid(column=sloupec, row=0)
            self.skryteBarvy.append(c)
            
            
            
        # titulek
        tk.Label(self, text=u"Logik").grid(columnspan=5)
        
        
        
        # pole s hádanou barvou
        self.hadaneBarvy = []
        for sloupec in range(5):
            radekBarev = []
            for radek in range(10):
                c = tk.Canvas(self, background='gray', width=self.sirka,
                              height=self.vyska)
                c.grid(column=sloupec, row=radek+2)
                radekBarev.append(c)
            self.hadaneBarvy.append(radekBarev)



        #oddelovaci cara
        c = tk.Canvas(self, backaround='#787', width=self.sirka, height=self.vyska)
        c.grid(column=0. row=10, columnspam=5)
        
        
        
        
        
        #tlacitka
        for sloupec in range(5):
    for radek,barva in enumerate(barvy):
        b = Button(okno, width=sirka, height=vyska,  
                bg=barva, fg=barva, 
                activebackground=barva,activeforeground=barva,
                bitmap='gray' )
        b.grid(column=sloupec, row=radek+11)

Button(okno,text=u'Odeslat').grid(column=6,row=11)


grid. 





















        self.bind("<Escape>", self.quit)
        # self.lbl = tk.Label(self, text="Hello World")
        # self.lbl.pack()
        # self.btn = tk.Button(self, text='Quit', command=self.quit)
        # self.btn.pack()

    def quit(self, event=None):
        super().quit()
        
        
        
        
        
        
        
        
        
        aktualniRadek = 9 
        zkouska=None
        pokus=[None]*5
        
        
        
        
        
        

app = Application()
app.mainloop()
