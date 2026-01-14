def start_pomodoro(root, label, work=25, break_time=5):
    work_seconds = work * 60
    break_seconds = break_time * 60

    def run_work(count):
        mins = count // 60
        secs = count % 60
        label.config(text=f"Focus {mins:02d}:{secs:02d}")

        if count > 0:
            root.after(1000, run_work, count - 1)
        else:
            root.after(1000, run_break, break_seconds)

    def run_break(count):
        mins = count // 60
        secs = count % 60
        label.config(text=f"Break {mins:02d}:{secs:02d}")

        if count > 0:
            root.after(1000, run_break, count - 1)
        else:
            label.config(text="Session Complete!")

    run_work(work_seconds)
