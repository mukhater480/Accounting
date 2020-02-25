import tkinter as tk
import tkinter.font as tk_font
from PIL import Image, ImageTk


# functions:

def increase_font_size_for_label(event):
    print(event.x)
    font_size = font_style_for_label['size']
    if font_size > 60:
        w.configure(fg="#ff0066", bg="#000")
        return
    font_style_for_label.configure(size=font_size + 3)


def change_color(event):
    event_type = str(event.type)
    if event_type == "Enter":
        button.configure(bg="#fff", fg="#000")
    elif event_type == "Leave":
        button.configure(bg="#000", fg="#ffffb3")


def new_window(event):
    # root.deiconify()  # show form
    # root.destroy()  # delete form
    root.withdraw()  # hide form

    # create new form:
    new_page = tk.Toplevel()
    new_page.overrideredirect(1)  # remove windows bar on top
    new_page.geometry("800x600+300+100")

    # label image:
    # img = tk.PhotoImage(file="img/button.png")
    pil_img = Image.open("img/Khafan-1.jpg")  # use jpg image in Tkinter!
    img = ImageTk.PhotoImage(pil_img)
    label = tk.Label(new_page, image=img, bg="#fff")
    label.image = img
    label.pack()


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

# background color of main page:
root["bg"] = "white"

# font style:
font_style_for_label = tk_font.Font(family="Lucida Grande", size=25)
font_style_for_button = tk_font.Font(family="Lucida Grande", size=18)

# label:
w = tk.Label(root, text="Hello World!", font=font_style_for_label)
w.pack()

# button:
button = tk.Button(root, text="ok", font=font_style_for_button, bg="#000", fg="#ffffb3",
                   width=6, cursor="hand2", relief=tk.FLAT)
button.bind("<Button-1>", increase_font_size_for_label)
button.bind("<Enter>", change_color)
button.bind("<Leave>", change_color)
button.pack()

# draw button:
btn_img = tk.PhotoImage(file="img/button.png")
draw_button = tk.Button(root, image=btn_img)
draw_button["bg"] = "white"
# b1["border"] = 0
draw_button["relief"] = tk.FLAT
draw_button.bind("<Button-2>", new_window)
draw_button.pack()


if __name__ == "__main__":
    root.mainloop()  # running app
