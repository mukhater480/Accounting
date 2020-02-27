import tkinter as tk
import tkinter.font as tk_font
import json


class Lang:
    """ this class for creating language window """

    def __init__(self, parent):
        self.parent = parent  # root window of this window

        self.root = tk.Toplevel()
        self.root.title("Languages")  # title of window
        self.root.iconbitmap("img/icon-1.ico")  # set icon for window
        self.root.resizable(False, False)  # can't to resize window
        self.width = 550
        self.height = 300
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
        # font:
        font = tk_font.Font(size=18)

        # color:
        fg = "white"
        bg = "black"

        # label:
        label = tk.Label(self.root, text="Please, Choose your language:", font=font,
                         bg=bg, fg=fg)
        label.place(x=50, y=40)

        # buttons:
        english_button = tk.Button(self.root, text="English", font=font,
                                   width=10, state=tk.DISABLED)
        english_button.place(x=100, y=100)

        farsi_button = tk.Button(self.root, text="فارسی", font=font,
                                 width=10, cursor="hand2")
        farsi_button.place(x=100, y=180)
        farsi_button.bind("<Button-1>", self._change_lang)

    def _change_lang(self, event):  # _methodName means protected method (just for programmer)
        self.parent.destroy()  # remove root window
        self.root.destroy()  # remove this window

        from main_fa import MainFa
        main_window = MainFa()  # change main window to farsi language
        main_window.show()  # show main window

        # change setting.config:
        setting = {"lang": "fa"}
        setting = json.dumps(setting)

        with open("config/setting.config", 'w') as F:
            F.write(setting)

    def show(self):
        self.root.deiconify()  # show window

    def hide(self):
        self.root.withdraw()  # hide window

    def destroy(self):
        self.root.destroy()  # destroy window

    def on_quit(self):
        self.destroy()

        self.parent.deiconify()  # show root window
