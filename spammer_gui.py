import pyautogui
import time
import sys
import tkinter as tk


# count = 5
#
#
# def counter():
#     global count
#     title.config(text=str(count))
#     count -= 1
#     if count > -1:
#         title.after(1000, counter)
#     else:
#         return


def text_file_spam():
    time.sleep(int(sleep_time.get()))
    title.config(text="Spamming...")
    script = open("input.txt", "r")
    for word in script:
        pyautogui.typewrite(word + '\n')

    title.config(text="Leave input empty for reading from file.")


def input_spam():
    time.sleep(int(sleep_time.get()))
    title.config(text="Spamming...")
    msg = entry.get()
    n = spam_times.get()
    for i in range(0, int(n)):
        pyautogui.typewrite(msg + '\n')

    title.config(text="Leave input empty for reading from file.")


def choose_method():
    if entry.get() == "":
        text_file_spam()
    else:
        input_spam()


root = tk.Tk()
root.title("PySpammer GUI Edition v1")

title = tk.Label(text="Leave input empty for reading from file.")
title.grid(row=0, column=0, columnspan=4)

entry = tk.Entry(root, width=50, text="Enter the text here!")
entry.grid(row=1, column=0, columnspan=4)

subtitle1 = tk.Label(text="Set the sleep time\n after button press.")
subtitle1.grid(row=2, column=1)

subtitle2 = tk.Label(text="Set the number of times\n to spam the input.")
subtitle2.grid(row=2, column=2)

spam_button = tk.Button(root, text="Spam!", command=choose_method, width=10)
spam_button.grid(row=3, column=0)

spam_times = tk.Spinbox(root, from_=5, to=100, width=5)
spam_times.grid(row=3, column=1)

sleep_time = tk.Spinbox(root, from_=5, to=20, width=5)
sleep_time.grid(row=3, column=2)

stop_button = tk.Button(root, text="Stop!", command=sys.exit, width=10)
stop_button.grid(row=3, column=3)

root.mainloop()
