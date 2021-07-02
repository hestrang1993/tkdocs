"""
This will be my take on the standard "Hello World" program.
"""
# coding=utf-8
from tkinter import Tk
from tkinter import ttk

BUTTON_TEXT = "Hello World"
"""
str: The text I want to add into the button of my "Hello World" application.
"""

root = Tk()
"""
tkinter.Tk: The top level window of my "Hello World" application.
"""
ttk.Button(root, text = BUTTON_TEXT).grid()
"""
tkinter.ttk.Button: A button that will display the string \"Hello World\".

It will have a grid layout to it.
"""

# Run the GUI application.
if __name__ == "__main__":
    root.mainloop()
