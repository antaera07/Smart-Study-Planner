import sqlite3
import matplotlib.pyplot as plt

def show_progress():
    conn = sqlite3.connect("study.db")
    cur = conn.cursor()

    cur.execute("SELECT date, SUM(hours) FROM sessions GROUP BY date")
    data = cur.fetchall()

    dates = [i[0] for i in data]
    hours = [i[1] for i in data]

    plt.plot(dates, hours)
    plt.title("Weekly Study Progress")
    plt.xlabel("Date")
    plt.ylabel("Hours")
    plt.show()
