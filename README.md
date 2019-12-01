# GradientFrame-Tkinter (Python 3.x)
This class creates a gradient frame using the tkinter library. In it, you can add any widget you want.

# How to use it ?
Just create an instance of GradientFrame passing as a parameter the frame where it will be placed,</br> 
frame size and gradient colors (from, to).

# Example:

```
from GradientFrame import GradientFrame
from tkinter import Tk

root = Tk()
gf = GradientFrame(root,[400,400],colors = ("red","black"))
gf.pack()
root.mainloop()
```
