# coding=utf-8
"""
The :mod:`feet_to_meters` module will contain a :mod:`tkinter` application
that will allow me to convert feet into
meters through a GUI interface.
"""
import tkinter as tk
from tkinter import ttk


# TODO: Refactor this class.
class MyFeetToMeters:
    """
    The :class:`MyFeetToMeters` class will run a GUI program that can convert feet into meters.
    """

    def __init__(self, root):
        """
        Create a new :class:`MyFeetToMeters` instance.

        Parameters
        ----------
        root : tkinter.Tk
            The parent window to run the GUI application in.
        """

        # Add a title to the window.
        self._title_string = "Feet to Meters"
        root.title(self._title_string)

        # Create a mainframe to add subwidgets to.
        self._mainframe_padding_string = '3 3 12 12'
        mainframe = ttk.Frame(
                root,
                padding = self._mainframe_padding_string
        )
        self._mainframe_sticky_tuple = (tk.N, tk.W, tk.E, tk.S)
        self._mainframe_column = 0
        self._mainframe_row = 0
        mainframe.grid(
                column = self._mainframe_column,
                row = self._mainframe_row,
                sticky = self._mainframe_sticky_tuple
        )

        # Configure the grid of the parent window.
        self._root_columnconfigure_weight = 1
        self._root_rowconfigure_weight = 1
        root.columnconfigure(
                0,
                weight = self._root_columnconfigure_weight
        )
        root.rowconfigure(
                0,
                weight = self._root_rowconfigure_weight
        )

        # Create an entry field to input the number of feet I want to convert into meters.
        self._feet_entry_width = 7
        self.feet = tk.StringVar()
        feet_entry = ttk.Entry(
                mainframe,
                width = self._feet_entry_width,
                textvariable = self.feet
        )
        self._feet_entry_column = 1
        self._feet_entry_row = 1
        feet_entry.grid(
                column = self._feet_entry_column,
                row = self._feet_entry_row,
                sticky = self._mainframe_sticky_tuple[1:3]
        )

        # Create a string variable for the meters output.
        # Creating this will make it easy to retrieve and manipulate the meters variable in the GUI.
        self.meters = tk.StringVar()

        # Create a label to store the meters string.
        meters_label = ttk.Label(
                mainframe,
                textvariable = self.meters
        )
        self._meter_label_column = 4
        self._meter_label_row = 1
        meters_label.grid(
                column = self._meter_label_column,
                row = self._meter_label_row,
                sticky = self._mainframe_sticky_tuple[1:3]
        )

        self._calculate_button_string = "Calculate"
        calculate_button = ttk.Button(
                mainframe,
                text = self._calculate_button_string,
                command = self.calculate
        )
        self._calculate_button_string_column = 1
        self._calculate_button_string_row = 2
        calculate_button.grid(
                column = self._calculate_button_string_column,
                row = self._calculate_button_string_row,
                sticky = self._mainframe_sticky_tuple[1]
        )

        self._feet_string_label_string = "feet"
        feet_string_label = ttk.Label(
                mainframe,
                text = self._feet_string_label_string
        )
        self._feet_string_label_column = 2
        self._feet_string_label_row = 1
        feet_string_label.grid(
                column = self._feet_string_label_column,
                row = self._feet_string_label_row,
                sticky = self._mainframe_sticky_tuple[1]
        )

        self._is_equiv_string_label_string = "is equivalent to "
        is_equivalent_to_string_label = ttk.Label(
                mainframe,
                text = self._is_equiv_string_label_string
        )
        self._is_equivalent_to_string_label_column = 3
        self._is_equivalent_to_string_label_row = 1
        is_equivalent_to_string_label.grid(
                column = self._is_equivalent_to_string_label_column,
                row = self._is_equivalent_to_string_label_row,
                sticky = self._mainframe_sticky_tuple[2]
        )

        meters_string_label = ttk.Label(mainframe, text = "meters")
        meters_string_label.grid(column = 5, row = 1, sticky = self._mainframe_sticky_tuple[1])

        self._pad_children_widgets(mainframe)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    @staticmethod
    def _pad_children_widgets(ttk_frame):
        """
        Pad all the child widgets and parent widgets.

        Parameters
        ----------
        ttk_frame : tkinter.ttk.Frame
            The mainframe that will store the multiple small widgets.

        Returns
        -------
        None
        """
        pad_x = 5
        pad_y = pad_x
        for child in ttk_frame.winfo_children():
            child.grid_configure(padx = pad_x, pady = pad_y)

    @staticmethod
    def _convert_feet_to_meters(feet):
        """
        Convert the number of feet into the number of meters.

        Parameters
        ----------
        feet : int or float
            The number of feet I want to convert into meters.

        Returns
        -------
        float
            The number of meters.
        """
        a = 0.3048
        b = 10000.0
        c = 0.5
        meters = int(a * feet * b + c) / b
        return meters

    def calculate(self, *args):
        """
        Calculate how many meters there are in a certain number of feet.

        This will be used to

        Parameters
        ----------
        *args
            The GUI items that store the feet values.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            The input was not a float or integer.
        """
        try:
            value = float(self.feet.get())
            self.meters.set(self._convert_feet_to_meters(value))
        except ValueError:
            print("Inputs need to be integers or floats.")


my_root = tk.Tk()
MyFeetToMeters(my_root)

if __name__ == "__main__":
    my_root.mainloop()
