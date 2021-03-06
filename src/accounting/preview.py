import tkinter as tk
import tkinter.font as tk_font


class Preview:
    """ this class for creating preview window """

    image_path = "img/"

    def __init__(self):
        self.root = tk.Toplevel()
        self.root.overrideredirect(1)  # remove windows bar on top
        self.width = 800
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

        self.root.geometry("%sx%s+%s+%s" % (width, height, x, y))

    def add_widgets(self):
        # size of gif is: width=189, height=24, frames=12

        # get all frame of gif:
        frames = [tk.PhotoImage(file=Preview.image_path + "preview.gif",
                                format="gif -index %i" % i) for i in range(12)]

        # every time set frame of gift:
        def update(index: int):
            frame = frames[index]
            label_img.configure(image=frame)
            label_img.image = frame
            index += 1
            if index > 11:
                index = 0
            label_img.after(35, update, index)

        # image:
        label_img = tk.Label(self.root)
        label_img.place(x=self.width / 2,
                        y=self.height / 2,
                        anchor="center")
        update(0)

        # text:
        font = tk_font.Font(size=21)

        label_text = tk.Label(self.root, text="Loading...",
                              fg="yellow", bg="black", font=font)
        label_text.place(x=self.width / 2,
                         y=(self.height / 2) - 50,
                         anchor="center")

    def show(self):
        self.root.deiconify()  # show window

    def hide(self):
        self.root.withdraw()  # hide window

    def destroy(self):
        self.root.destroy()  # destroy window
