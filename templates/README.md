🚀 SysPulse
### Real-Time Linux Monitoring Dashboard

SysPulse is a lightweight Linux monitoring dashboard built using Python, Flask, and WSL Ubuntu. It provides real-time visibility into system health metrics such as CPU utilization, memory consumption, disk usage, hostname, and operating system information through a browser-based dashboard.

---

## 📌 Project Overview

Managing and monitoring Linux systems often requires running multiple terminal commands to inspect resource utilization.

SysPulse simplifies this process by collecting live system metrics and presenting them through a clean web interface that updates automatically in real time.

This project demonstrates practical knowledge of:

- Linux Administration
- WSL (Windows Subsystem for Linux)
- Python Development
- REST APIs
- System Monitoring
- Flask Web Framework
- Git & GitHub

---

## 🏗 Architecture

```text
Linux (WSL Ubuntu)
        │
        ▼
   psutil Library
        │
        ▼
   Flask Backend API
        │
        ▼
   JSON Response
        │
        ▼
 Real-Time Dashboard
```

---

## ✨ Features

✅ Real-Time CPU Monitoring

✅ Memory Usage Tracking

✅ Disk Usage Monitoring

✅ Hostname Detection

✅ Operating System Information

✅ REST API Endpoint

✅ Dynamic Dashboard Updates

✅ Lightweight Deployment

✅ Linux-Based Monitoring

---

## 🖥 Dashboard Preview

Displays:

- Hostname
- Operating System
- CPU Usage (%)
- Memory Usage (%)
- Disk Utilization (%)

Values update automatically without requiring a page refresh.

---

## ⚙️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Flask | Backend Web Framework |
| psutil | System Metrics Collection |
| HTML | Frontend Interface |
| WSL Ubuntu | Linux Environment |
| Git | Version Control |
| GitHub | Source Code Hosting |

---

## 📂 Project Structure

```text
SysPulse/
│
├── app.py
├── monitor.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── venv/
```

---

## 🔍 How It Works

### 1. System Metrics Collection

The application collects live Linux system information using the `psutil` library.

Examples:

- CPU Utilization
- Memory Utilization
- Disk Usage
- Host Details

### 2. REST API Layer

The Flask backend exposes metrics through:

```http
GET /api/stats
```

Example Response:

```json
{
  "hostname": "DESKTOP-XXXXX",
  "os": "Linux",
  "cpu": 8.4,
  "memory": 34.2,
  "disk": 15.1
}
```

### 3. Dynamic UI Updates

The frontend fetches new metrics every few seconds using JavaScript and updates the dashboard automatically.

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SysPulse.git
```

### Navigate to Project

```bash
cd SysPulse
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

- Linux Monitoring Concepts
- WSL Environment Management
- Python Backend Development
- REST API Design
- Real-Time Data Visualization
- Git & GitHub Workflow
- System Administration Basics

---

## 📈 Future Enhancements

Planned improvements:

- Dark Theme UI
- Uptime Monitoring
- Network Statistics
- Process Monitoring
- Open Port Detection
- Historical Usage Graphs
- Export System Reports
- Docker Deployment
- Multi-System Agent-Based Monitoring

---

## 💼 Resume Description

**SysPulse – Real-Time Linux Monitoring Dashboard**

Developed a Linux-based monitoring dashboard using Python, Flask, and WSL Ubuntu to collect and visualize real-time CPU, memory, disk, and system metrics. Designed REST APIs for data exposure and implemented a dynamic frontend capable of live system health monitoring.

---

## 👨‍💻 Author

**Yuvanshi Bhalawat**

Final Year Engineering Student

Passionate about Linux, DevOps, Cloud Computing, and System Engineering.

---

⭐ If you found this project useful, consider giving it a star.
