# 🔐 Decoding Cyber Threats in India

A powerful data analytics project that explores **cybersecurity threat patterns across India** using **Python**, **MySQL**, **Pandas**, **Matplotlib**, and **Seaborn**. This analysis uncovers critical insights into attack vectors, protocol vulnerabilities, malware trends, and regional exposure, providing the foundation for stronger, data-driven cybersecurity defense strategies.

---

## 🧠 Project Objective

To analyze and visualize cybersecurity incidents across India, detect high-risk patterns, and identify weaknesses in digital infrastructure. The goal is to enable **early threat detection**, promote **proactive defense mechanisms**, and support **national cybersecurity strategies** through real data insights.

---

## 📁 Dataset Overview

**File:** `cybersecurity_attacks.csv` (place this file in the project root directory)

The dataset includes diverse cybersecurity parameters, such as:

- 🗓️ Temporal Data: Year, Month, Day
- 🌐 Network Info: Protocol, Packet Type, Packet Length, Traffic Type
- 🧬 Indicators: Malware Flags, Anomaly Scores, Attack Signatures
- 🚨 Alerts & Logs: IPS Alerts, Firewall Logs, Proxy Info
- 👥 User & Device Data
- 📊 Attack Metrics: Severity Level, Action Taken, Source/Destination IPs

---

## 🔄 Data Preprocessing

- ✅ Handles missing and inconsistent values
- 🧠 Converts relevant data to appropriate formats (e.g., datetime parsing)
- 🧹 Drops low-signal or mostly null columns
- 🔍 Standardizes values across categorical features

---

## 📊 Exploratory Data Analysis (EDA)

Visual insights powered by **Matplotlib** and **Seaborn** reveal:

1. **Malware Indicators by Month**
2. **Traffic Type Distribution**
3. **Device Count by Traffic Type & Protocol**
4. **Packet Length Histogram**
5. **Anomaly Score Trends by Day**
6. **Distribution of Action Taken**
7. **Monthly Alerts Breakdown**
8. **Severity Levels by Year**
9. **User Count Over Time (Year & Month)**
10. **Attack Signatures by Month**
11. **Attack Types Overview**
12. **Source IP Distribution by State**

---

## 🔍 Key Insights

- 📈 **DNS-based attacks dominate** the Indian cyber landscape.
- ⚠️ Over **33% of incidents indicate intrusion-level anomalies**.
- 🧠 Peak malware activity occurs during specific months—suggesting seasonal or event-driven attack trends.
- 🌍 Regional disparities point to varying **cyber hygiene** and **network exposure** levels across Indian states.

---

## ✅ Requirements

Ensure the following packages are installed:

- Python 3.x
- MySQL Server
- [`mysql-connector-python`](https://pypi.org/project/mysql-connector-python/)
- `pandas`
- `matplotlib`
- `seaborn`

Install with pip:

```bash
pip install mysql-connector-python pandas matplotlib seaborn
