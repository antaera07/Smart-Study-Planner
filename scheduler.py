from datetime import datetime

def generate_schedule(subjects):
    today = datetime.today()
    plan = []

    for s in subjects:
        days_left = (datetime.strptime(s[2], "%Y-%m-%d") - today).days
        daily = round(s[4] / max(days_left, 1), 2)
        plan.append((s[1], daily))

    return plan
