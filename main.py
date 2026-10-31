# -*- coding: utf-8 -*-
"""A small tkinter calculator for a rectangle: base and height in,
area and perimeter out.

The arithmetic sits in calculate_result(), which takes the two
entry strings and returns the exact text the result label should
show. It touches no widget, so I can test it on a machine with no
display. The window itself is built in main(), under the guard at
the bottom, so importing this file no longer opens a window or
blocks in mainloop the way the first version did.
"""

import math
import tkinter as tk


def format_number(value):
    # I print with ten decimal places and trim the zeros I added.
    # 5 by 3 still reads "15", not "15.0000000000", and a large
    # product keeps all its digits: the %g format I used before
    # kept six significant digits and switched to exponent form,
    # so 1234567 by 7654321 came out as 9.44977e+12 instead of
    # 9449772114007. The trade is at the small end: a result under
    # 1e-10 in size rounds to 0 at this precision, which no pair of
    # sides I would type into this window gets near.
    text = f"{value:.10f}"
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    if text in ("", "-0"):
        return "0"
    return text


def calculate_result(base_text, height_text):
    """Return the result label text for two entry strings."""
    try:
        # float() is the parse rule. It takes decimals and padded
        # numbers, which int() did not, and int() was what crashed
        # this program on the old placeholder text and on a value
        # like 2.5. It also takes 1e3, inf, and nan without
        # complaint, so the finite check below is mine, not its.
        base = float(base_text)
        height = float(height_text)
    except ValueError:
        # Bad input reports through the result label. The first
        # version let the ValueError escape the click handler, so
        # a bad entry died with no message in the window at all.
        return "Please enter two numbers"
    if not (math.isfinite(base) and math.isfinite(height)):
        # An inf or nan in a box used to print "Area: inf" as if
        # that were an answer. It is the same kind of bad input as
        # a word, so it gets the same message.
        return "Please enter two numbers"
    if base < 0 or height < 0:
        # A rectangle side cannot be negative. Zero stays allowed:
        # a 0 by 5 rectangle has area 0 and perimeter 10, and that
        # answer is true as far as it goes.
        return "Base and height cannot be negative"
    area = base * height
    perimeter = 2 * (base + height)
    return "Area: %s, Perimeter: %s" % (
        format_number(area),
        format_number(perimeter),
    )


def main():
    window = tk.Tk()
    # I want the window semi transparent at 0.7. Whether that shows
    # depends on the window manager and compositor; some systems
    # ignore the setting and draw the window solid, and the program
    # runs the same either way.
    window.attributes('-alpha', 0.7)
    window.title('Area and Perimeter Calculator')
    window.config(bg="black")
    # The geometry height is 95 because minsize and maxsize below
    # are also 95. An earlier version asked for 85 here against a
    # 95 minimum, so the size I asked for could never be the size I
    # got. With min and max set equal, the window cannot be resized
    # at all, which is what I want for this fixed layout.
    window.geometry("275x95")
    window.minsize(275, 95)
    window.maxsize(275, 95)
    # Column weights belong on the window. An earlier version set
    # one inside the title label, where it stretched nothing.
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    # The two entry boxes read through these variables, not through
    # the entry widgets themselves. They start empty on purpose:
    # the first version prefilled them with the words Area... and
    # Perimeter..., and pressing Calculate on those words crashed
    # the parse. Empty is what makes the shipped state safe to click.
    textbox1 = tk.StringVar()
    textbox1.set("")
    textbox2 = tk.StringVar()
    textbox2.set("")

    # Title
    lbl_title = tk.Label(master=window, text="Area and Perimeter Calculator", bg="black", fg="white", font=("Helvetica", 15))
    lbl_title.grid(row=0, column=0, sticky="nsew", columnspan=2)

    # Base Entry Box
    # The boxes sit on grid row 2, under the title on row 0. Row 1
    # has no widget in it, and an empty grid row takes no height,
    # so the boxes still land directly under the title. The text=""
    # argument on the entries sets nothing that matters:
    # textvariable is what the box shows and what calculate()
    # reads.
    entbase_box = tk.Entry(master=window, text="", bg="black", fg="white", textvariable=textbox1)
    entbase_box.grid(row=2, column=0, sticky="nsew")

    # Height Entry Box
    # This box gets its own name. The first version reused
    # entbase_box here, so after setup the name pointed at the
    # height box only and the base box could not be reached by its
    # widget name at all.
    entheight_box = tk.Entry(master=window, text="", bg="black", fg="white", textvariable=textbox2)
    entheight_box.grid(row=2, column=1, sticky="nsew")

    # Result Label
    # This label is the only output the program has. calculate()
    # writes both real results and the bad input messages into it.
    lbl_result = tk.Label(master=window, text="", bg="black", fg="white")
    lbl_result.grid(row=4, column=0, sticky="nsew", columnspan=2)

    def calculate():
        # The handler is a shell on purpose: read the two boxes,
        # hand the strings to calculate_result(), show what it
        # returns. All the deciding happens in that function,
        # where a test can reach it without a window.
        lbl_result["text"] = calculate_result(textbox1.get(), textbox2.get())

    # Enter Button
    # command takes calculate itself, with no parentheses. Writing
    # calculate() here would run it once while the window is being
    # built, and the button would do nothing on click.
    btn_enter = tk.Button(master=window, text="Calculate", command=calculate, bg="black", fg="white")
    btn_enter.grid(row=3, column=0, sticky="nsew", columnspan=2)

    # mainloop goes last and blocks. Anything after it would not
    # run until the window closes, so all setup stays above it.
    window.mainloop()


if __name__ == "__main__":
    main()
