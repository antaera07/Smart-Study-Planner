from tkinter import *
from database import setup, connect
from scheduler import generate_schedule
from pomodoro import start_timer
from tracker import show_progress

setup()

root = Tk()
root.title("Smart Study Planner")

def add_subject():
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO subjects VALUES(NULL, ?, ?, ?, ?)",
                (name.get(), date.get(), priority.get(), hours.get()))
    conn.commit()
    conn.close()

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
Button(root, text="Start Pomodoro", command=start_timer).pack()
Button(root, text="Show Progress", command=show_progress).pack()

root.mainloop()
