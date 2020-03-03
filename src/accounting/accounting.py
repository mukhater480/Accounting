import tkinter as tk
import tkinter.font as tk_font
import _thread


class Accounting:
    """ this class for creating accounting window """

    def __init__(self, parent):
        self.parent = parent  # root window of this window

        self.root = tk.Toplevel()
        self.root.title("Accounting")  # title of window
        self.root.iconbitmap("img/icon-1.ico")  # set icon for window
        self.root.resizable(False, False)  # can't to resize window
        self.width = 1050
        self.height = 600
        self.background_color = "black"

        # add details:
        self.set_position(self.width, self.height)  # setting this window on center of screen
        self.add_widgets()  # adding widgets on window

        # background color of window:
        self.root.configure(bg=self.background_color)

        # when client wants to click close button on top bar:
        self.root.protocol("WM_DELETE_WINDOW", self.on_quit)

        # connect to DB:

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
        pass

    def show(self):
        self.root.deiconify()  # show window

    def hide(self):
        self.root.withdraw()  # hide window

    def destroy(self):
        self.root.destroy()  # destroy window

    def on_quit(self):
        self.destroy()  # destroy this window

        self.parent.show()  # show root window
