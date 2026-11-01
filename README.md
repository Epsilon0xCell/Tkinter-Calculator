![Intro scenery](intro-banner.png)


# Tkinter-Calculator

![Wordmark banner](banner.png)

![Animated scene](scene.svg)

![Separator](sep-heavy.svg)

> **Bench note:** a display is required to open the window, and the window itself went untested on a machine with no screen.


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
  `Area: <base times height>, Perimeter: <2 times (base plus height)>`.
  Results print with trailing zeros trimmed (`Area: 15, Perimeter: 16`
  for base 5 and height 3), and a large product prints all its digits
  (1234567 by 7654321 gives `Area: 9449772114007`).
- If either box is empty or not a number, the result line shows
  `Please enter two numbers` instead of a result, and the window stays
  usable. The same message covers `inf` and `nan`, which `float()`
  accepts as text: an earlier version printed `Area: inf` as if it
  were an answer.
- A negative base or height shows `Base and height cannot be
  negative`. Zero is allowed and computes as entered.

The deciding code is separate from the window. `calculate_result()`
in `main.py` takes the two entry strings and returns the exact text
for the result label; the button handler only reads the boxes and
shows that text. Importing `main.py` builds nothing, so the logic
can be tested on a machine with no display.

## Tests

```bash
python3 -m unittest
```

12 tests over `calculate_result()` and the number formatting:
whole numbers, decimals, padded input, exponent input, zero,
empty and text input, `inf` and `nan`, negative sides, the large
product above, and float noise (`0.1` by `0.2` reads `Area: 0.02`).

## Honest limits

- The window itself was not run in this pass: the maintenance host
  has no display, so `python3 main.py` stops with a tkinter
  `TclError` there, and I record the GUI as not run rather than
  passed. The logic tests above are what this pass verified.
- Results under 1e-10 in size round to 0 at the print precision I
  use. No pair of sides typed into this window gets near that.

## Files

- `main.py`: the whole program, logic and window.
- `test_main.py`: the headless logic tests.
- `logo.png`, `banner.png`: generated branding.
- `LICENSE`: GNU General Public License v3.
