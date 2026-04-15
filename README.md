# 🪟 Windows Threat Detection Tool

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20Logs-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![Version](https://img.shields.io/badge/version-v1.0-blue)

---

## 📌 Overview

The **Windows Threat Detection Tool** is a Python-based cybersecurity project that simulates a **Security Operations Center (SOC)** workflow by analyzing Windows authentication logs.

It detects:
- Brute-force login attempts  
- Targeted account attacks  
- Suspicious failed login activity  

---

## 🚀 Key Features

- 🔍 Parses Windows-style security logs (Event ID 4625 – Failed Login)  
- 📊 Tracks failed login attempts by source IP and user account  
- ⚠️ Detects brute-force attacks using configurable thresholds  
- 🎯 Identifies targeted account attacks  
- 🕒 Generates timestamped alerts  
- 📁 Exports alerts to TXT, CSV, and JSON  

---

## 🧩 System Architecture

```text
Windows Security Logs
        |
        v
      Parser
        |
        v
 Detection Engine
   /           \
  v             v
IP Detection  User Detection
   \           /
    v         v
   Alert Generation
        |
        v
 TXT / CSV / JSON Reports

```


## 🖥️ How to Run (Step-by-Step)

### 1. Clone the repository

```bash
git clone https://github.com/oams84/windows-threat-detection-tool.git
cd windows-threat-detection-tool
```

### 2. Check Python
```bash
python3 --version
```

### 3. Use the sample log file
```bash
Location:
logs/windows_security.csv
```
```bash
📊 Example Output

timestamp,event_id,account_name,source_ip,status
2026-04-14 09:00:01,4625,admin,192.168.1.50,Failed
```

### 4. Run the tool
```bash
python3 main.py
```
### 📁 Project Structure
```bash
windows_threat_detection/
├── logs/
│   └── windows_security.csv
├── reports/
├── parser.py
├── detector.py
├── main.py
├── README.md
└── requirements.txt
```
## 📂 Reports Generated

- alerts.txt → human-readable alerts
- alerts.csv → structured data
- alerts.json → machine-readable format

---

## 🛠 Technologies Used
- Python 3
- CSV Processing
- JSON
- Linux (Ubuntu)
- Windows Security Event Concepts
---
##🎯 Skills Demonstrated
- Windows Log Analysis
- Threat Detection
- Brute-Force Detection
- Incident Response Simulation
- Python Automation
- SOC / Blue Team Concepts
---
##🔮 Future Improvements
- Support real .evtx Windows logs
- Add threat intelligence integration
- Add dashboard visualization
- Add real-time monitoring


---

##📜 License

This project is licensed under the MIT License.

