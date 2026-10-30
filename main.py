# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:58:56 2024

@author: cy83r-3x71nc710n
"""

import tkinter as tk

# Everything in this file runs at import, in order, top to bottom.
# There is no main guard, so importing this module opens the window
# and ends in mainloop like running it does. I build the window first,
# then define the handler, then build the widgets it reads, then start
# the loop. That order matters and the notes below say where.
window = tk.Tk()
# I want the window semi transparent at 0.7. Whether that shows
# depends on the window manager and compositor; some systems ignore
# the setting and draw the window solid, and the program runs the
# same either way.
window.attributes('-alpha', 0.7)
window.title('Area and Perimeter Calculator')
window.config(bg="black")   
# The geometry height is 95 because minsize and maxsize below are
# also 95. An earlier version asked for 85 here against a 95 minimum,
# so the size I asked for could never be the size I got. With min and
# max set equal, the window cannot be resized at all, which is what I
# want for this fixed layout.
window.geometry("275x95")
window.minsize(275,95)
window.maxsize(275,95)

def calculate():
    # This function is defined before textbox1, textbox2, and
    # lbl_result exist. That is safe only because nothing calls it
    # during startup: tkinter calls it on a button click, and by then
    # the whole file has run and all three names are set. Calling it
    # from the setup code above the widget section would fail with a
    # NameError.
    try:
        # float() is the whole input rule. It takes decimals and
        # padded numbers, which int() did not, and int() was what
        # crashed this handler on the old placeholder text and on a
        # value like 2.5. It also takes things like 1e3, inf, and nan
        # without complaint. I never added a check for those, so an
        # inf in a box really does print Area: inf.
        base = float(textbox1.get())
        height = float(textbox2.get())
    except ValueError:
        # Bad input reports through the result label and returns. The
        # first version let the ValueError escape the click handler,
        # so a bad entry died with no message in the window at all.
        lbl_result["text"] = "Please enter two numbers"
        return
    # I do not range check either number. Zero and negatives compute
    # as typed and can give a negative area or perimeter. That is a
    # known limit I left in, and the README says so.
    area = base*height
    perimeter = 2*(base+height)
    # %g trims trailing zeros, so 5 by 3 prints Area: 15 instead of
    # 15.000000. The trade is that %g keeps six significant digits and
    # switches to exponent form for very large or very small results,
    # so a huge area prints in a shorter, rougher form.
    lbl_result["text"] = "Area: %g, Perimeter: %g" % (area, perimeter)
    
# The two entry boxes read through these variables, not through the
# entry widgets themselves. They start empty on purpose: the first
# version prefilled them with the words Area... and Perimeter..., and
# pressing Calculate on those words crashed the parse. Empty is what
# makes the shipped state safe to click.
textbox1 = tk.StringVar()
textbox1.set("")
textbox2 = tk.StringVar()
textbox2.set("")

# Title
lbl_title = tk.Label(master=window, text="Area and Perimeter Calculator",bg="black",fg="white",font=("Helvetica",15))
lbl_title.grid(row=0, column=0,sticky="nsew", columnspan=2)
# This line configures a grid column inside the label itself, not in
# the window. I expected it to stretch the window columns when I wrote
# it; it does not, and the window columns never get a weight anywhere
# in this file. The layout still looks right because the title and the
# button span both columns, but the line is not doing what it looks
# like it does.
lbl_title.grid_columnconfigure(0, weight=1)

# Base Entry Box
# The boxes sit on grid row 2, under the title on row 0. Row 1 has no
# widget in it, and an empty grid row takes no height, so the boxes
# still land directly under the title. The text="" argument on the
# entries sets nothing that matters: textvariable is what the box
# shows and what calculate() reads.

entbase_box = tk.Entry(master=window,text="",bg="black",fg="white",textvariable=textbox1)
entbase_box.grid(row=2, column=0,sticky="nsew")


# Height Entry Box
# I reuse the name entbase_box for this second box, so after this line
# the name points at the height box only. The base box keeps working
# because it is held by the grid and by textbox1, but nothing later in
# the file can reach it by its widget name. If I ever need to change
# the base box itself, this reuse is the first thing to undo.

entbase_box = tk.Entry(master=window,text="",bg="black",fg="white",textvariable=textbox2)
entbase_box.grid(row=2, column=1,sticky="nsew")


# Enter Button
# command takes calculate itself, with no parentheses. Writing
# calculate() here would run it once while the window is being built,
# before the result label exists, and the button would do nothing on
# click.
btn_enter = tk.Button(master=window, text="Calculate", command=calculate,bg="black",fg="white")
btn_enter.grid(row=3, column=0,sticky="nsew", columnspan=2)



# Result Label
# This label is the only output the program has. calculate() writes
# both real results and the bad input message into it, so it has to
# exist before the first click, which the build order guarantees.

lbl_result = tk.Label(master=window, text="",bg="black",fg="white")
lbl_result.grid(row=4, column=0,sticky="nsew", columnspan=2)

# mainloop goes last and blocks. Anything I put after this line would
# not run until the window closes, so all setup has to stay above it.
window.mainloop()
