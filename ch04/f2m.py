# coding=utf-8
"""
A very basic application.

It will convert feet into meters.
"""
import tkinter as tk
from tkinter import ttk


def calculate(*args):
    """
    Convert feet into meters.

    Parameters
    ----------
    *args

    Returns
    -------
    None

    Raises
    ------
    ValueError
        The value fed into the function is neither an integer or a float.
    """
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


root = tk.Tk()
"""
tkinter.Tk: The main window of my application.
"""
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
"""
tkinter.ttk.Frame: A rectangular container for my other widgets.

It is a child of the ``root`` widget.
The padding is offset in certain dimensions.
"""

mainframe_sticky = (tk.N, tk.W, tk.E, tk.S)
"""
tuple[str, str, str, str]: A tuple containing strings that tell tkinter how to position widgets in an application.

This will apply mainly to the ``mainframe``.
"""
mainframe.grid(column = 0, row = 0, sticky = mainframe_sticky)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

feet = tk.StringVar()
"""
tkinter.StringVar: A wrapper for my feet text object.
"""
meters = tk.StringVar()
"""
tkinter.StringVar: A wrapper for my meters text object.
"""

feet_entry = ttk.Entry(mainframe, width = 7, textvariable = feet)
"""
tkinter.ttk.Entry: An entry field to put in the number of feet I want to convert into meters.
"""
feet_entry_sticky = (tk.W, tk.E)
"""
tuple[str, str]: A tuple containing strings that tell tkinter how to position widgets in an application.

This will apply mainly to the ``feet_entry``.
"""
feet_entry.grid(column = 2, row = 1, sticky = feet_entry_sticky)

ttk.Label(mainframe, textvariable = meters).grid(column = 2, row = 2, sticky = feet_entry_sticky)
ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column = 3, row = 3, sticky = tk.W)

ttk.Label(mainframe, text = "feet").grid(column = 3, row = 1, sticky = tk.W)
ttk.Label(mainframe, text = "is equivalent to").grid(column = 1, row = 2, sticky = tk.E)
ttk.Label(mainframe, text = "meters").grid(column = 3, row = 2, sticky = tk.W)

for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
