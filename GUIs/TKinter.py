from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self, win_name="GUI", but_text="Exit"):
        self.master.title(win_name)
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        menu.add_cascade(label='File', menu=file)
        file.add_command(label='Exit', command=self.client_exit)
        file.add_command(label='Save', command=self.client_exit)

        edit = Menu(menu)
        menu.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='Show image', command=self.show_image)
        edit.add_command(label='Show text', command=self.show_text)

        quitButton = Button(self, text=but_text, command=self.client_exit)
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()

    def show_image(self):
        load = Image.open('tad_sznuk.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def show_text(self):
        text = Label(self, text='Hey!!')
        text.pack()


# creating a frame (main main window)
root = Tk()
# setting the dimensions for the frame
root.geometry("150x300")

app = Window(root)

root.mainloop()
