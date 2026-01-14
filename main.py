from tkinter import *
from database import setup, connect
from scheduler import generate_schedule
from pomodoro import start_pomodoro
from tracker import show_progress
from tkinter import Listbox, END

setup()

root = Tk()
root.title("Smart Study Planner")
timer_label = Label(root, text="25:00", font=("Arial", 18))
timer_label.pack(pady=10)
subject_list = Listbox(root, width=40, height=6)
subject_list.pack(pady=5)

def add_subject():
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO subjects VALUES(NULL, ?, ?, ?, ?)",
                (name.get(), date.get(), priority.get(), hours.get()))
    conn.commit()
    conn.close()

    subject_list.insert(END, f"{name.get()} | Exam: {date.get()} | Hours: {hours.get()}")

    name.delete(0, END)
    date.delete(0, END)
    priority.delete(0, END)
    hours.delete(0, END)

Label(root, text="Subject").pack()
name = Entry(root)
name.pack()

Label(root, text="Exam Date (YYYY-MM-DD)").pack()
date = Entry(root)
date.pack()

Label(root, text="Priority (1-5)").pack()
priority = Entry(root)
priority.pack()

Label(root, text="Total Hours Needed").pack()
hours = Entry(root)
hours.pack()

Button(root, text="Add Subject", command=add_subject).pack()
Button(root, text="Start Pomodoro",
       command=lambda: start_pomodoro(root, timer_label)).pack()
Button(root, text="Show Progress", command=show_progress).pack()

root.mainloop()
