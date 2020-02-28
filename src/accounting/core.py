# tkinter:
import tkinter as tk

# windows:
from preview import Preview
from preview_fa import PreviewFa
from main import Main
from main_fa import MainFa

# extra:
import time
import json
import _thread


if __name__ == "__main__":
    with open("config/setting.config", 'rt') as F:
        data = F.read()
    setting = json.loads(data)

    root = tk.Tk()
    root.overrideredirect(1)  # remove window bar on top
    root.withdraw()  # hide window

    if setting["lang"] == "fa":
        preview_window = PreviewFa()
    else:
        preview_window = Preview()

    def main_page():
        if setting["lang"] == "fa":
            main_window = MainFa()
        else:
            main_window = Main()

        time.sleep(2)  # do something

        preview_window.destroy()  # delete preview window

        main_window.show()  # show main window

    _thread.start_new_thread(main_page, ())

    root.mainloop()
