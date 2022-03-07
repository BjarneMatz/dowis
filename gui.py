import tkinter as tk
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DOWIS Python Client | Donnjer Weather and Information System")

        header = ttk.Frame(self)
        header.pack()
        headerstyle = ttk.Style(header)
        headerstyle.configure("TLabel", font=("Calibri", 20))
        mainframe = ttk.Frame(self)
        mainframe.pack()

        footer = ttk.Frame(self)
        footer.pack()

        ttk.Label(header, text="DOWIS CLIENT | Donnjer Weather Information System").pack()
        ttk.Label(mainframe, text="").pack()
        ttk.Label(footer, text="© Donnjer Development").pack()

        basicsensorframe = ttk.Frame(mainframe)
        basicsensorframe.pack()

        ttk.Label(basicsensorframe, text="Temperatur:").grid(column=1, row=1)
        ttk.Label(basicsensorframe, text="In").grid()
        ttk.Label(basicsensorframe, text="Out").grid()




if __name__ == "__main__":
    program = Gui()
    program.mainloop()
