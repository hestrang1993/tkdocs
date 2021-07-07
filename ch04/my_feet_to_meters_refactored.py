# coding=utf-8


import tkinter as tk
from tkinter import ttk


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
        self.add_title_to_window(root)
        mainframe = self.create_mainframe(root)
        self.add_mainframe_to_grid(mainframe)
        self.feet = tk.StringVar()
        feet_entry = self.create_feet_entry_widget(mainframe)
        self.add_feet_entry_widget_to_grid(feet_entry, 1, 1)
        self.meters = tk.StringVar()
        meters_label = self.create_meters_label_widget(mainframe)
        self.add_meters_label_widget_to_grid(meters_label, 4, 1)
        calculate_button = self.create_calculate_button_widget(mainframe)
        self.add_calculate_button_widget_to_grid(calculate_button, 1, 2)
        feet_string_label = self.create_feet_label_string_widget(mainframe)
        self.add_feet_label_string_widget_to_grid(feet_string_label, 2, 1)
        is_equivalent_to_string_label = self.create_is_equivalent_to_label_widget(mainframe)
        self.add_is_equivalent_to_label_widget_to_grid(is_equivalent_to_string_label, 3, 1)
        meters_string_label = self.create_meters_string_label_widget(mainframe)
        self.add_meters_string_label_widget_to_grid(meters_string_label, 5, 1)
        self._pad_children_widgets(mainframe)
        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    @staticmethod
    def add_title_to_window(root_window):
        """
        Add the title string "Feet to Meters" to the parent window.

        Parameters
        ----------
        root_window: tkinter.Tk
            The parent window that will house all of my widgets.

        Returns
        -------
        None
        """
        title_string = "Feet to Meters"
        root_window.title(title_string)

    @staticmethod
    def create_mainframe(root_window):
        """
        Create a pseudo-parent widget that will house all of my true child widgets in.

        I call it a pseudo-parent because it will be a child widget of the root window.

        Parameters
        ----------
        root_window : tkinter.Tk
            The parent window that will house all of my widgets.


        Returns
        -------
        tkinter.ttk.Frame
            The pseudo-parent widget that will house all of my other child widgets.
        """
        mainframe_padding_string = '3 3 12 12'
        mainframe = ttk.Frame(root_window, padding = mainframe_padding_string)
        return mainframe

    @staticmethod
    def add_mainframe_to_grid(mainframe_window):
        """
        Add the mainframe widget (the pseudo-parent widget) to a grid within the root window.

        Parameters
        ----------
        mainframe_window : tkinter.ttk.Frame
            The pseudo-parent widget that will house all of my other child widgets.

        Returns
        -------
        None
        """
        sticky_tuple = (tk.N, tk.W, tk.E, tk.S)
        column = 0
        row = 0
        mainframe_window.grid(column = column, row = row, sticky = sticky_tuple)

    @staticmethod
    def _configure_root_column(root_window):
        """
        Configure the column(s) of the root parent window.

        Parameters
        ----------
        root_window : tkinter.Tk
            The parent window that will house all of my widgets.


        Returns
        -------
        None
        """
        column_weight = 1
        root_window.columnconfigure(0, weight = column_weight)

    @staticmethod
    def _configure_root_row(root_window):
        """
        Configure the rows(s) of the root parent window.

        Parameters
        ----------
        root_window : tkinter.Tk
            The parent window that will house all of my widgets.


        Returns
        -------
        None
        """
        row_weight = 1
        root_window.rowconfigure(0, weight = row_weight)

    def configure_root_grid(self, root_window):
        """
        Configure the column(s) and row(s) of the root parent window.

        Parameters
        ----------
        root_window : tkinter.Tk
            The parent window that will house all of my widgets.


        Returns
        -------
        None
        """
        self._configure_root_column(root_window)
        self._configure_root_row(root_window)

    def create_feet_entry_widget(self, mainframe_window):
        feet_entry_width = 7
        feet_entry = ttk.Entry(mainframe_window, width = feet_entry_width, textvariable = self.feet)
        return feet_entry

    @staticmethod
    def add_feet_entry_widget_to_grid(feet_entry_widget, column, row):
        sticky_tuple = (tk.W, tk.E)
        feet_entry_widget.grid(column = column, row = row, sticky = sticky_tuple)

    def create_meters_label_widget(self, mainframe_window):
        meters_label = ttk.Label(mainframe_window, textvariable = self.meters)
        return meters_label

    @staticmethod
    def add_meters_label_widget_to_grid(meters_label_widget, column, row):
        sticky_tuple = (tk.W, tk.E)
        meters_label_widget.grid(column = column, row = row, sticky = sticky_tuple)

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

    def create_calculate_button_widget(self, mainframe_window):
        text = "Calculate"
        calculate_button = ttk.Button(mainframe_window, text = text, command = self.calculate)
        return calculate_button

    @staticmethod
    def add_calculate_button_widget_to_grid(calculate_button_widget, column, row):
        sticky_string = tk.W
        calculate_button_widget.grid(column = column, row = row, sticky = sticky_string)

    @staticmethod
    def create_feet_label_string_widget(mainframe_window):
        string = "feet"
        feet_label_string_widget = ttk.Label(mainframe_window, text = string)
        return feet_label_string_widget

    @staticmethod
    def add_feet_label_string_widget_to_grid(feet_label_string_widget, column, row):
        sticky_string = tk.W
        feet_label_string_widget.grid(column = column, row = row, sticky = sticky_string)

    @staticmethod
    def create_is_equivalent_to_label_widget(mainframe_window):
        string = "is equivalent to "
        is_equivalent_to_label_widget = ttk.Label(mainframe_window, text = string)
        return is_equivalent_to_label_widget

    @staticmethod
    def add_is_equivalent_to_label_widget_to_grid(is_equivalent_to_label_widget, column, row):
        sticky_string = tk.E
        is_equivalent_to_label_widget.grid(column = column, row = row, sticky = sticky_string)

    @staticmethod
    def create_meters_string_label_widget(mainframe_window):
        string = "meters"
        meters_string_label_widget = ttk.Label(mainframe_window, text = string)
        return meters_string_label_widget

    @staticmethod
    def add_meters_string_label_widget_to_grid(meters_string_label_widget, column, row):
        sticky_string = tk.W
        meters_string_label_widget.grid(column = column, row = row, sticky = sticky_string)

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


my_root = tk.Tk()
MyFeetToMeters(my_root)

if __name__ == "__main__":
    my_root.mainloop()