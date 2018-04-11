import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


# *args - any number of arguments
# **kwargs - keyword arguments, small dicts
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # minimum size, priority
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[F] = frame

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # tkraise is putting sth in front
        frame.tkraise()


def qf(param):
    print(param)


class StartPage(tk.Frame):
    # controller is for using the show_frame method on the upper class
    # container jest parentem
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button1.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to start Page", command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PagTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = SeaofBTCapp()
app.mainloop()
