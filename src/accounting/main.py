import tkinter as tk
import tkinter.font as tk_font
from PIL import Image, ImageTk
import time


class Main:
    """ this class for creating main window """

    image_path = "img/"

    def __init__(self):
        self.root = tk.Toplevel()

        self.hide()  # at first start this window is hidden

        self.root.title("Main Page")  # title of window
        self.root.iconbitmap("img/icon-1.ico")  # set icon for window
        self.root.resizable(False, False)  # can't to resize window
        self.width = 950
        self.height = 500
        self.background_color = "black"

        # add details:
        self.set_position(self.width, self.height)  # setting this window on center of screen
        self.add_widgets()  # adding widgets on window

        # background color of window:
        self.root.configure(bg=self.background_color)

        # when client wants to click close button on top bar:
        self.root.protocol("WM_DELETE_WINDOW", self.on_quit)

    def set_position(self, width: int, height: int):
        """ setting center position of screen for window """
        # get pixel of screen:
        width_screen = self.root.winfo_screenwidth()
        height_screen = self.root.winfo_screenheight()

        # set position of this window on center od screen:
        x = int((width_screen / 2) - (width / 2))
        y = int((height_screen / 2) - (height / 2))

        self.root.geometry("%sx%s+%s+%s" % (width, height, x, y))

    def add_widgets(self):
        # size of background-image is: width=1000, height=600
        pil_img = Image.open("img/main-image.jpg")
        img = ImageTk.PhotoImage(pil_img)

        # image:
        label_img = tk.Label(self.root, image=img)
        label_img.image = img
        label_img.pack()

        # buttons:

        # buttons color:
        bg = "black"
        fg = "#ffff99"

        # font of buttons:
        font = tk_font.Font(size=16)

        # location of buttons:
        x = 50
        y = 75

        accounting_button = tk.Button(self.root, text="Accounting",
                                      bg=bg, fg=fg, font=font, cursor="hand2", width=15)
        accounting_button.place(x=x, y=y)
        accounting_button.bind("<Button-1>", self.accounting_window)

        lang_button = tk.Button(self.root, text="Languages",
                                bg=bg, fg=fg, font=font, cursor="hand2", width=15)
        lang_button.place(x=x, y=y + 90)
        lang_button.bind("<Button-1>", self.lang_window)

        info_button = tk.Button(self.root, text="App information",
                                bg=bg, fg=fg, font=font, cursor="hand2", width=15)
        info_button.place(x=x, y=y + 180)
        info_button.bind("<Button-1>", self.info_window)

        # date:

        # font of date:
        font = tk_font.Font(size=21)

        date = time.strftime("%a - %d / %b / %Y")
        label_date = tk.Label(self.root, font=font, text=date,
                              bg="#ffff99", fg="#663300")
        label_date.place(x=self.width, y=0, anchor="ne")

    def accounting_window(self, event):
        self.destroy()  # remove this window
        pass

    def lang_window(self, event):
        self.hide()  # hide this window

        from lang import Lang
        lang = Lang(self.root)  # show language window
        lang.root.focus_force()  # focus on languages window

    def info_window(self, event):
        self.hide()  # hide this window
        pass

    def show(self):
        self.root.deiconify()  # show window

    def hide(self):
        self.root.withdraw()  # hide window

    def destroy(self):
        self.root.destroy()  # destroy window

    def on_quit(self):
        self.destroy()
        import sys
        sys.exit(3)
