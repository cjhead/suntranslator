import tkinter as tk
from tkinter import Tk
from gui.menubar import Menubar
from gui.views.translator_view import EntryView

from importlib.resources import files, as_file


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title = "Sun Translator"
        self.cfg = as_file(files('config').joinpath('config'))

        with self.cfg as file:
            self.option_readfile(file)

        self.rowconfigure(0, weight=1, minsize=200)
        self.columnconfigure(0, weight=1, minsize=200)

        self.views = {}
        self.views["EntryView"] = EntryView(self)
        self.views["EntryView"].grid(row=0, column=0, sticky=tk.NSEW)

        self.menubar = Menubar(self)

        self.show_view("EntryView")

    def show_view(self, view_name):
        view = self.views[view_name]
        view.tkraise()
