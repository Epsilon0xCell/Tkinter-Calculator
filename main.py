# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:58:56 2024

@author: cy83r-3x71nc710n
"""

import tkinter as tk
window = tk.Tk()
window.attributes('-alpha', 0.7)
window.title('Area and Rectangle Calculator')
window.config(bg="black")   
window.geometry("275x85")
window.minsize(275,95)
window.maxsize(275,95)

def calculate():
    base = textbox1.get()
    height = textbox2.get()
    base = int(base)
    height = int(height)
    result = base*height
    lbl_result["text"] = result
    
# Base x Height
textbox1 = tk.StringVar()
textbox1.set("Area...")
textbox2 = tk.StringVar()
textbox2.set("Perimeter...")

# Title
lbl_title = tk.Label(master=window, text="Area and Perimeter Calculator",bg="black",fg="white",font=("Helvetica",15))
lbl_title.grid(row=0, column=0,sticky="nsew", columnspan=2)
lbl_title.grid_columnconfigure(0, weight=1)

# Base Entry Box

entbase_box = tk.Entry(master=window,text="",bg="black",fg="white",textvariable=textbox1)
entbase_box.grid(row=2, column=0,sticky="nsew")


# Height Entry Box

entbase_box = tk.Entry(master=window,text="",bg="black",fg="white",textvariable=textbox2)
entbase_box.grid(row=2, column=1,sticky="nsew")


# Enter Button
btn_enter = tk.Button(master=window, text="Calculate", command=calculate,bg="black",fg="white")
btn_enter.grid(row=3, column=0,sticky="nsew", columnspan=2)



# Result Label

lbl_result = tk.Label(master=window, text="",bg="black",fg="white")
lbl_result.grid(row=4, column=0,sticky="nsew", columnspan=2)

window.mainloop()
