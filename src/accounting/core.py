import tkinter as tk
from preview import Preview
from preview_fa import PreviewFa
import time
import _thread
import json


with open("config/setting.config", 'rt') as F:
    data = F.read()

setting = json.loads(data)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.withdraw()

    if setting["lang"] == "fa":
        preview_window = PreviewFa()
        root.title("صفحه اصلی")
    else:
        preview_window = Preview()


    def main_page():
        time.sleep(5)  # do something
        root.geometry("900x600+100+100")

        preview_window.destroy()  # delete preview window

        root.deiconify()  # show main page


    _thread.start_new_thread(main_page, ())

    root.mainloop()
