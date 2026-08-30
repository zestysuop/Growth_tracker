from flask import Flask, render_template, request, redirect
from datetime import date, timedelta

app = Flask(__name__)

# Starting date
START_DATE = date(2026, 9, 1)

# Four growth categories
categories = [
    "Mental",
    "Physical",
    "Social",
    "Economic"
]

# Temporary task storage
tasks = []


def get_week_number():
    today = date.today()

    if today < START_DATE:
        return 1

    days_passed = (today - START_DATE).days
    week = (days_passed // 7) + 1

    return min(week, 17)


@app.route("/")
def home():

    current_week = get_week_number()

    current_tasks = [
        task for task in tasks
        if task["week"] == current_week
    ]

    completed = len([
        task for task in current_tasks
        if task["completed"]
    ])

    total = len(current_tasks)

    if total > 0:
        progress = round((completed / total) * 100)
    else:
        progress = 0

    return render_template(
        "index.html",
        tasks=current_tasks,
        categories=categories,
        week=current_week,
        progress=progress
    )


@app.route("/add", methods=["POST"])
def add_task():

    task_name = request.form["task"]
    category = request.form["category"]

    tasks.append({
        "task": task_name,
        "category": category,
        "week": get_week_number(),
        "completed": False
    })

    return redirect("/")


@app.route("/complete/<int:task_id>")
def complete_task(task_id):

    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True

    return redirect("/")


@app.route("/review")
def review():

    current_week = get_week_number()

    weekly_tasks = [
        task for task in tasks
        if task["week"] == current_week
    ]

    total = len(weekly_tasks)

    completed = len([
        task for task in weekly_tasks
        if task["completed"]
    ])

    if total > 0:
        progress = round((completed / total) * 100)
    else:
        progress = 0

    return render_template(
        "review.html",
        tasks=weekly_tasks,
        week=current_week,
        progress=progress
    )


if __name__ == "__main__":
    app.run(debug=True)