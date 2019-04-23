#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:13:37 2019

@author: rin35130
"""
from os.path import basename, splitext
import tkinter as tk
from functools import partial
# from tkinter import ttk


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
        for radek in range(10):
            radekBarev = []
            for sloupec in range(5):
                c = tk.Canvas(self, background='lightgray', width=self.sirka,
                              height=self.vyska)
                c.grid(column=sloupec, row=radek+2)
                radekBarev.append(c)
            self.hadaneBarvy.append(radekBarev)
        #self.hadaneBarvy[1][4].config(background='magenta')

        # odpověď programu
        odpovedProgramu = []
        for radek in range(10):
            lbl = tk.Label(self, text="-/-")
            lbl.grid(column=6, row=radek+2)
            odpovedProgramu.append(lbl)

        # oddělovací čára
        c = tk.Canvas(self, background='#777', width=6*self.sirka, height=8)
        c.grid(column=0, row=12, columnspan=5)

        # tlačítka
        for radek, barva in enumerate(self.barvy):
            for sloupec in range(5):
                b = tk.Button(width=self.sirka, height=self.vyska,
                              bitmap='gray12',
                              activebackground=barva, activeforeground=barva,
                              bg=barva, fg=barva,
                              command=partial(self.click, radek, sloupec))
                b.grid(row=radek+13, column=sloupec)
                
                
        self.btn=tk.Button(self, text="Odeslat", command=self.odeslat)
        self.btn.grid(row=13,column=6)
        
        self.bind("<Escape>", self.quit)

    def click(self, r, s):
        global aktualniradek
        self.hadaneBarvy[0][s].config(bg=self.barvy[r])
        
        print(r, s)
        
    def odeslat(self):
        pass
    
    
    aktualniradek=9
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()

