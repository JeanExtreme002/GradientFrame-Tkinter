# GradientFrame-Tkinter (Python 3.x)
Create a gradient widget using only the tkinter library.

# How to use it ?
Create an instance of GradientFrame passing as a parameter the frame where it will be placed. </br> 
In addition to the Canvas settings, you can also configure the colors and direction of the gradient.

# Example:

```
from GradientFrame import GradientFrame
from tkinter import Tk

root = Tk()
gf = GradientFrame(root, colors = ("yellow", "black"), width = 800, height = 600)
gf.config(direction = gf.top2bottom)
gf.pack()
root.mainloop()
```
