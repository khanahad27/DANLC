# 📊 Student Performance Analysis

A comprehensive Python project that uncovers insights into student performance by leveraging **MySQL**, **Pandas**, **Matplotlib**, and **Seaborn**. This analysis delves into a variety of academic and socio-economic factors, revealing critical trends that can guide educators and policymakers toward more effective strategies in education.

---

## 🧠 Project Objective

This project aims to understand the multifaceted influences on student success—ranging from academic scores and study habits to parental involvement and socio-economic status. The insights derived serve as a foundation for **data-driven interventions** and **educational reforms**.

---

## 📁 Dataset Overview

**File:** `Education_Data.csv` (place in project root)

The dataset includes detailed attributes such as:

- 🎓 Academic Metrics: Math, English, Science, and History Scores
- 📅 Attendance & Participation Rates
- 👨‍👩‍👧‍👦 Parental Involvement
- 🕒 Study Hours Per Week
- 🏆 Extracurricular Activities & Scholarship Status
- 💰 Household Income & School Funding Level
- 💻 Technology Access
- 😰 Test Anxiety Level
- 🎯 Future Plans

---

## 🔍 Data Handling & Preprocessing

- ✅ Handles missing or null values
- 🔁 Converts relevant data types (e.g., date columns to `datetime`)
- 🧹 Drops irrelevant or sparsely populated columns
- 🔎 Applies data validation and consistency checks

---

## 📊 Exploratory Data Analysis (EDA)

Harnessing the power of **Matplotlib** and **Seaborn**, the project explores:

1. **Grade Level Distribution**
2. **Age Distribution by Gender**
3. **English Score Histogram**
4. **Average Math Scores by Grade & Age**
5. **Study Hours per Week vs Age**
6. **Parental Involvement Patterns**
7. **Extracurricular Activities by Gender**
8. **Age Count by Gender and Funding Level**
9. **Participation Rate Trends by Age**
10. **Income Distribution by Scholarship Status**
11. **Future Educational Plans**
12. **Unique IP Source by States**
13. **Attendance Rate by Grade Level**

---

## 🎯 Key Insights

- A **positive correlation** exists between study hours and performance.
- **Parental involvement** strongly influences student engagement and success.
- Students in **well-funded schools** show improved academic metrics.
- **Scholarship recipients** often exhibit different household income distributions.
- **Participation in extracurricular activities** contributes to holistic student development.

---

## ✅ Requirements

Make sure you have the following installed:

- Python 3.x
- MySQL
- [`mysql-connector-python`](https://pypi.org/project/mysql-connector-python/)
- `pandas`
- `matplotlib`
- `seaborn`

Install packages via pip:

```bash
pip install mysql-connector-python pandas matplotlib seaborn
