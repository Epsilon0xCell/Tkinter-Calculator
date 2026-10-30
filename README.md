![tkinter calculator banner](banner.png)

# Tkinter-Calculator

A small tkinter GUI calculator for a rectangle: enter a base and a
height, press Calculate, and it shows the area and the perimeter.

## Run

```bash
python3 main.py
```

Requires Python 3 with tkinter and a display. Standard library only;
there is nothing to install beyond Python itself. On a headless
machine it needs a virtual display (for example Xvfb) to open the
window.

## How it works

- Two entry boxes take the base and the height. Both start empty.
- Decimals are accepted, not just whole numbers, and surrounding
  whitespace is ignored.
- Pressing Calculate sets the result line to
  `Area: <base times height>, Perimeter: <2 times (base plus height)>`,
  with trailing zeros trimmed (for example `Area: 15, Perimeter: 16`
  for base 5 and height 3).
- If either box is empty or not a number, the result line shows
  `Please enter two numbers` instead of a result, and the window stays
  usable.

## Honest limits

- Inputs are not range-checked: zero and negative numbers are computed
  as entered and can produce zero or negative results.
- Verification during maintenance was headless: the window was opened
  under Xvfb and the Calculate handler was driven directly with a
  matrix of inputs, but no physical display, mouse, or keyboard was
  used.

## Files

- `main.py`: the whole program.
- `logo.png`, `banner.png`: generated branding.
- `LICENSE`: GNU General Public License v3.
