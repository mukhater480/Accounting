import tkinter as tk
import tkinter.font as tk_font


# functions:
def increase_font_size_for_label(event):
    # print(event)
    font_size = font_style_for_label['size']
    if font_size > 60:
        w.configure(fg="#ff0066")
        return
    font_style_for_label.configure(size=font_size + 3)


# ------------------------------------------------------------------------

# creating main:
root = tk.Tk()

# title:
root.title("Accounting")

# icon:
root.iconbitmap("img/icon-1.ico")

# size and location of main window:
width = 600
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)  # center of screen
y = (screen_height / 2) - (height / 2)  # center of screen
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, False)

# font style:
font_style_for_label = tk_font.Font(family="Lucida Grande", size=25)
font_style_for_button = tk_font.Font(family="Lucida Grande", size=18)

# label:
w = tk.Label(root, text="Hello World!", font=font_style_for_label)
w.pack()

# button:
b = tk.Button(root, text="ok", font=font_style_for_button, bg="black", fg="#ffffb3", width=5)
b.bind("<Button-1>", increase_font_size_for_label)
b.pack()

if __name__ == "__main__":
    root.mainloop()  # running app
