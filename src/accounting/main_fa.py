import tkinter as tk
import tkinter.font as tk_font
from PIL import Image, ImageTk
import jdatetime
import time
import _thread


class MainFa:
    """ this class for creating main farsi window """

    image_path = "img/"

    def __init__(self):
        self.root = tk.Toplevel()

        self.hide()  # at first start this window is hidden

        self.root.title("صفحه اصلی")  # title of window
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

    def set_position(self, width: int, height: int):
        """ setting center position of screen for window """
        # get pixel of screen:
        width_screen = self.root.winfo_screenwidth()
        height_screen = self.root.winfo_screenheight()

        # set position of this window on center od screen:
        x = int((width_screen / 2) - (width / 2))
        y = int((height_screen / 2) - (height / 2))

        # when client wants to click close button on top bar:
        self.root.protocol("WM_DELETE_WINDOW", self.on_quit)

        self.root.geometry("%sx%s+%s+%s" % (width, height, x, y))

    def add_widgets(self):
        # size of background-image is: width=1000, height=600
        pil_img = Image.open("img/main-image.jpg")
        img = ImageTk.PhotoImage(pil_img)

        # image:
        label_img = tk.Label(self.root, image=img)
        label_img.image = img
        label_img.pack()

        # timer for hiding cursor after 3 seconds(like player!):
        _thread.start_new_thread(timer, (label_img,))

        # buttons:

        # buttons color:
        bg = "black"
        fg = "#ffff99"

        # font of buttons:
        font = tk_font.Font(size=16)

        # location of buttons:
        x = 900
        y = 75

        accounting_button = tk.Button(self.root, text="حسابداری",
                                      bg=bg, fg=fg, font=font, cursor="hand2", width=15)
        accounting_button.place(x=x, y=y, anchor="e")  # anchor="e" for setting to right layout(farsi)
        accounting_button.bind("<Button-1>", self.accounting_window)

        lang_button = tk.Button(self.root, text="زبان ها",
                                bg=bg, fg=fg, font=font, cursor="hand2", width=15)
        lang_button.place(x=x, y=y + 90, anchor="e")  # anchor="e" for setting to right layout(farsi)
        lang_button.bind("<Button-1>", self.lang_window)

        info_button = tk.Button(self.root, text="اطلاعات برنامه",
                                bg=bg, fg=fg, font=font, cursor="hand2", width=15)
        info_button.place(x=x, y=y + 180, anchor="e")  # anchor="e" for setting to right layout(farsi)
        info_button.bind("<Button-1>", self.info_window)

        # date:

        # font of date:
        font = tk_font.Font(size=21)

        jdatetime.set_locale("Persian_Iran")  # set to farsi!
        date = jdatetime.datetime.now().strftime("%a - %d / %b / %Y")
        label_date = tk.Label(self.root, font=font, text=date,
                              bg="#ffff99", fg="#663300")
        label_date.place(x=0, y=0, anchor="nw")

    def accounting_window(self, event):
        self.hide()  # hide this window
        pass

    def lang_window(self, event):
        self.hide()  # hide this window

        from lang_fa import LangFa
        lang = LangFa(self)  # show language window
        lang.root.focus_force()  # focus on languages window

    def info_window(self, event):
        self.hide()  # hide this window

        from app_info_fa import AppInfoFa
        app_info = AppInfoFa(self)  # show app information window
        app_info.root.focus_force()  # focus on app information window

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


# *** this part for hiding the cursor after 3 seconds of no movement ***

def timer(widget):  # widget is tk.Label
    while 1:  # means infinitive loop
        time.sleep(0.01)  # 1 / 100 second
        try:
            x, y = widget.winfo_pointerxy()
            hide_cursor(x, y, widget)
        except Exception as ex:
            # print(ex)
            break


old_x, old_y = -1, -1  # keeping old position of mouse
i = 0  # for counting time


def hide_cursor(x, y, widget):  # widget is tk.Label
    global old_x, old_y, i
    if old_x == x and old_y == y:
        i += 1
        if i > 300:  # after 3 seconds hides cursor
            widget.configure(cursor="none")
    else:  # if the cursor is moved, the timer will be reset
        widget.configure(cursor="arrow")
        i = 0
        old_x, old_y = x, y
