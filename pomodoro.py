import threading
import time
from tkinter import messagebox

def pomodoro_cycle(work, break_time):
    for _ in range(work * 60):
        time.sleep(1)

    messagebox.showinfo("Break Time!", "Work session complete! Take a break.")

    for _ in range(break_time * 60):
        time.sleep(1)

    messagebox.showinfo("Session Complete", "Break over! Ready for another round.")

def start_timer(work=25, break_time=5):
    t = threading.Thread(target=pomodoro_cycle, args=(work, break_time))
    t.daemon = True
    t.start()
