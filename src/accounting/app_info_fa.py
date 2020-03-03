import tkinter as tk
import tkinter.font as tk_font
import webbrowser

# windows:
from lang import Lang  # using this class for inheritance


class AppInfoFa(Lang):
    """
    this class for creating farsi information of application window
    this window extends Lang class
    """

    # using super initialization because this window similar to language window:
    def __init__(self, parent):
        super().__init__(parent)  # call object of super class and send argument
        self.root.title("اطلاعات برنامه")  # change title!

    def _change_lang(self, event):  # protected method from Lang class
        pass  # override this method (doing nothing!)

    def add_widgets(self):  # override this method (new style!)
        # text about me farsi (open with encoding UTF-8):
        with open("config/aboutMeFa.txt", encoding="UTF-8") as F:
            text = F.read()

        # font for text:
        font = tk_font.Font(size=18)

        # label about me:
        label_about_me = tk.Label(self.root, text=text,
                                  bg="black", fg="white",
                                  font=font, justify=tk.RIGHT)
        label_about_me.place(x=520,
                             y=30,
                             anchor="ne")

        # font for link:
        font = tk_font.Font(size=14)

        # label for link:
        label_link = tk.Label(self.root, text=":راه های ارتباطی",
                              bg="black", fg="#ffffb3",
                              font=font, justify=tk.RIGHT)
        label_link.place(x=520,
                         y=170,
                         anchor="ne")

        # links:

        email = tk.Label(self.root, text="aryanbadiee333@gmail.com",
                         bg="black", fg="#ff4dff",
                         font=font, cursor="hand2")
        email.bind("<Button-1>", lambda event: webbrowser.open_new("mailto:aryanbadiee333@gmail.com"))
        email.bind("<Enter>", lambda event: email.configure(fg="#66a3ff"))
        email.bind("<Leave>", lambda event: email.configure(fg="#ff4dff"))
        email.place(x=275,
                    y=210,
                    anchor="center")

        github = tk.Label(self.root, text="github.com/aryanbadiee",
                          bg="black", fg="#ff4dff",
                          font=font, cursor="hand2")
        github.bind("<Button-1>", lambda event: webbrowser.open_new("https://www.github.com/aryanbadiee"))
        github.bind("<Enter>", lambda event: github.configure(fg="#66a3ff"))
        github.bind("<Leave>", lambda event: github.configure(fg="#ff4dff"))
        github.place(x=275,
                     y=240,
                     anchor="center")

        instagram = tk.Label(self.root, text="instagram.com/aryanbadiee",
                             bg="black", fg="#ff4dff",
                             font=font, cursor="hand2")
        instagram.bind("<Button-1>", lambda event: webbrowser.open_new("https://www.instagram.com/aryanbadiee/"))
        instagram.bind("<Enter>", lambda event: instagram.configure(fg="#66a3ff"))
        instagram.bind("<Leave>", lambda event: instagram.configure(fg="#ff4dff"))
        instagram.place(x=275,
                        y=270,
                        anchor="center")
