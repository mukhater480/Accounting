import tkinter as tk
import tkinter.font as tk_font
import webbrowser

# windows:
from lang import Lang  # using this class for inheritance


class AppInfo(Lang):
    """
    this class for creating information of application window
    this window extends Lang class
    """

    # using super initialization because this window similar to language window:
    def __init__(self, parent):
        super().__init__(parent)  # call object of super class and send argument
        self.root.title("App Information")  # change title!

    def _change_lang(self, event):  # protected method from Lang class
        pass  # override this method (doing nothing!)

    def add_widgets(self):  # override this method (new style!)
        # text about me:
        with open("config/aboutMe.txt") as F:
            text = F.read()

        # font for text:
        font = tk_font.Font(size=16)

        # label about me:
        label_about_me = tk.Label(self.root, text=text,
                                  bg="black", fg="white",
                                  font=font, justify=tk.LEFT)
        label_about_me.place(x=30,
                             y=30)

        # font for link:
        font = tk_font.Font(size=12)

        # label for link:
        label_link = tk.Label(self.root, text="Communication Ways:",
                              bg="black", fg="#ffffb3",
                              font=font, justify=tk.LEFT)
        label_link.place(x=30,
                         y=170)

        # links:

        email = tk.Label(self.root, text="aryanbadiee333@gmail.com",
                         bg="black", fg="#ff99ff",
                         font=font, cursor="hand2")
        email.bind("<Button-1>", lambda event: webbrowser.open_new("mailto:aryanbadiee333@gmail.com"))
        email.place(x=275,
                    y=220,
                    anchor="center")

        github = tk.Label(self.root, text="github.com/aryanbadiee",
                          bg="black", fg="#ff99ff",
                          font=font, cursor="hand2")
        github.bind("<Button-1>", lambda event: webbrowser.open_new("https://www.github.com/aryanbadiee"))
        github.place(x=275,
                     y=250,
                     anchor="center")

        instagram = tk.Label(self.root, text="instagram.com/aryanbadiee",
                             bg="black", fg="#ff99ff",
                             font=font, cursor="hand2")
        instagram.bind("<Button-1>", lambda event: webbrowser.open_new("https://www.instagram.com/aryanbadiee/"))
        instagram.place(x=275,
                        y=280,
                        anchor="center")
