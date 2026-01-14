def start_timer(label, root, work=25, break_time=5):
    total = work * 60

    def countdown(sec):
        m = sec // 60
        s = sec % 60
        label.config(text=f"{m:02d}:{s:02d}")

        if sec > 0:
            root.after(1000, countdown, sec - 1)
        else:
            label.config(text="Break Time!")
            root.after(1000, start_break)

    def start_break():
        total_break = break_time * 60

        def break_count(sec):
            m = sec // 60
            s = sec % 60
            label.config(text=f"Break {m:02d}:{s:02d}")

            if sec > 0:
                root.after(1000, break_count, sec - 1)
            else:
                label.config(text="Session Complete!")

        break_count(total_break)

    countdown(total)
