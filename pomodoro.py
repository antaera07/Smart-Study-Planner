import time
from tkinter import messagebox

def start_timer(work=25, break_time=5):
    for i in range(work * 60, 0, -1):
        time.sleep(1)

    messagebox.showinfo("Break Time!", "Take a 5 minute break!")

    for i in range(break_time * 60, 0, -1):
        time.sleep(1)
