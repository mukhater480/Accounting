import tkinter as tk
import tkinter.font as tk_font
import json


class LangFa:
    """ this class for creating farsi language window """

    def __init__(self, parent):
        self.parent = parent  # root window of this window

        self.root = tk.Toplevel()
        self.root.title("زبان ها")  # title of window
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
        label = tk.Label(self.root, text=":لطفا زبان مورد نظر خود را انتخاب کنید", font=font,
                         bg=bg, fg=fg)
        label.place(x=500, y=40, anchor="e")  # anchor="e" for rtl

        # buttons:
        english_button = tk.Button(self.root, text="English", font=font,
                                   width=10, cursor="hand2")
        english_button.place(x=450, y=100, anchor="e")  # anchor="e" for rtl
        english_button.bind("<Button-1>", self._change_lang)

        farsi_button = tk.Button(self.root, text="فارسی", font=font,
                                 width=10, state=tk.DISABLED)
        farsi_button.place(x=450, y=180, anchor="e")  # anchor="e" for rtl

    def _change_lang(self, event):  # _methodName means protected method (just for programmer)
        self.parent.destroy()  # remove root window
        self.destroy()  # remove this window

        from main import Main
        main_window = Main()  # change main window to english language
        main_window.show()  # show main window

        # change setting.config:
        setting = {"lang": "en"}
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

        self.parent.show()  # show root window
