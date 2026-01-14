from tkinter import messagebox

def start_timer(root, work=25, break_time=5):
    seconds = work * 60

    def countdown(count):
        mins = count // 60
        secs = count % 60
        root.title(f"Focus Time: {mins:02d}:{secs:02d}")

        if count > 0:
            root.after(1000, countdown, count - 1)
        else:
            messagebox.showinfo("Break Time", "Focus session complete! Take a break.")
            start_break()

    def start_break():
        seconds = break_time * 60

        def break_count(count):
            mins = count // 60
            secs = count % 60
            root.title(f"Break Time: {mins:02d}:{secs:02d}")

            if count > 0:
                root.after(1000, break_count, count - 1)
            else:
                messagebox.showinfo("Session Complete", "Break over! Ready for another round.")
                root.title("Smart Study Planner")

        break_count(seconds)

    countdown(seconds)
