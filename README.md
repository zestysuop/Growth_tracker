# Growth_tracker
A Python Flask web app that helps track weekly mental, physical, social, and economic growth through goals, task completion, weekly reflections, and progress tracking from September to December 2026.
# 🌱 4-Month Growth Tracker

A personal web-based **Growth Tracker** built with Python and Flask to track progress across four important areas of life:

* 🧠 **Mental Growth**
* 💪 **Physical Growth**
* 👥 **Social Growth**
* 💰 **Economic & Career Growth**

The goal of this project is to set weekly tasks, complete them, and reflect on progress at the end of every week.

The tracker will run for **4 months — September 1, 2026 to December 31, 2026.**

---

## 🎯 Project Goal

The purpose of this project is to create a structured system for personal growth.

Instead of simply setting yearly goals, the application breaks them down into **weekly tasks and reviews**.

Every week, I can:

1. Set goals for the week.
2. Divide goals into four growth categories.
3. Mark completed tasks.
4. Track my weekly completion percentage.
5. Review what went well.
6. Identify areas that need improvement.
7. Set better goals for the following week.

---

## 🗓️ Project Duration

**Start Date:** September 1, 2026
**End Date:** December 31, 2026
**Duration:** 4 Months
**Number of Weeks:** Approximately 17 weeks

---

## 📌 Growth Categories

### 🧠 Mental Growth

Examples:

* Read 20 pages every day.
* Learn a new concept.
* Practice meditation.
* Maintain a journal.
* Reduce unnecessary screen time.

### 💪 Physical Growth

Examples:

* Exercise 4 times a week.
* Walk 8,000 steps.
* Drink enough water.
* Maintain a consistent sleep schedule.
* Follow a healthier diet.

### 👥 Social Growth

Examples:

* Talk to a friend or family member.
* Meet someone new.
* Improve communication skills.
* Practice speaking English.
* Spend meaningful time with people.

### 💰 Economic & Career Growth

Examples:

* Study for GATE.
* Learn Python.
* Complete an Excel project.
* Apply for jobs.
* Improve technical skills.
* Work on a portfolio project.

---

## ⚙️ Features

### Current Features

* Add weekly tasks.
* Assign tasks to growth categories.
* Mark tasks as completed.
* Calculate weekly completion percentage.
* View weekly progress.
* Weekly reflection questions.
* Automatic week calculation based on the project start date.

### Planned Features

* [ ] SQLite database
* [ ] Permanent task storage
* [ ] Automatic weekly reminders
* [ ] Progress charts
* [ ] Monthly progress dashboard
* [ ] 17-week progress history
* [ ] Personal notes and reflections
* [ ] Final 4-month growth report
* [ ] Responsive mobile design
* [ ] Dark mode
* [ ] User authentication

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **SQLite** *(planned)*
* **Git & GitHub**

---

## 📂 Project Structure

```text
4-Month-Growth-Tracker/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── add_task.html
│   └── review.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/4-Month-Growth-Tracker.git
```

### 2. Open the project

```bash
cd 4-Month-Growth-Tracker
```

### 3. Install Flask

```bash
pip install flask
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the website

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📊 How the Tracker Works

The application follows a simple weekly cycle:

```text
             SET WEEKLY GOALS
                    ↓
        ┌───────────┴───────────┐
        ↓           ↓           ↓
     Mental      Physical      Social
        │           │           │
        └───────────┬───────────┘
                    ↓
             Economic/Career
                    ↓
             COMPLETE TASKS
                    ↓
             TRACK PROGRESS
                    ↓
              WEEKLY REVIEW
                    ↓
             REFLECT & IMPROVE
                    ↓
             NEXT WEEK
```

---

## 📈 Weekly Review

At the end of every week, the application will calculate the percentage of completed tasks.

For example:

```text
Week 4

Mental       → 4/5 tasks completed
Physical     → 5/6 tasks completed
Social       → 2/4 tasks completed
Economic     → 5/5 tasks completed

Overall Progress → 80%
```

The weekly review will also ask questions such as:

* What did I accomplish this week?
* What went well?
* What didn't go well?
* What stopped me from completing certain tasks?
* What did I learn?
* What should I improve next week?
* What is my biggest priority for next week?

---

## 🏆 4-Month Goal

At the end of the four-month period, the application will provide a summary of the journey.

The final report will track:

* Total tasks created
* Total tasks completed
* Weekly completion percentage
* Progress in each growth category
* Strongest area of growth
* Area requiring the most improvement
* Weekly reflections
* Overall 4-month progress

---

## 📅 Weekly Journey

| Period    | Focus                           |
| --------- | ------------------------------- |
| September | Building consistency            |
| October   | Improving habits                |
| November  | Increasing performance          |
| December  | Reflection & long-term planning |

---

## 💡 Why I Built This

I wanted to build something that is not just another programming project.

This project combines **learning Python and web development with personal development**.

I will use this application throughout the four-month period to document my progress and learn how software can solve a real-life problem.

---

## 🔮 Future Vision

The long-term goal is to turn this into a complete personal growth platform where users can:

* Create long-term goals.
* Break goals into weekly tasks.
* Track habits.
* Receive reminders.
* Write weekly reflections.
* Visualize their progress.
* Compare monthly performance.
* Generate personal growth reports.

---

## 👩‍💻 Author

**Aqsa Nizami**

This project is being developed as a learning project while exploring:

**Python → Flask → Web Development → Databases → GitHub**

---

## ⭐ Project Status

🚧 **Currently in development**

The project will be continuously updated throughout the four-month journey.

> **Small progress every day becomes significant progress over time. 🌱**
