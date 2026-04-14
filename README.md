# 🪟 Windows Threat Detection Tool

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20Logs-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![Version](https://img.shields.io/badge/version-v1.0-blue)

---

## 📌 Overview

The **Windows Threat Detection Tool** is a Python-based security analytics project designed to simulate a **Security Operations Center (SOC)** workflow by analyzing Windows authentication logs.

The tool detects:
- Brute-force login attempts
- Targeted account attacks
- Suspicious failed authentication patterns

It processes Windows-style security events and generates structured alerts for incident response and investigation.

---

## 🚀 Key Features

- 🔍 Parses Windows security log data (Event ID 4625 – Failed Login)
- 📊 Tracks failed login attempts by source IP and user account
- ⚠️ Detects brute-force attacks using configurable thresholds
- 🎯 Identifies targeted attacks against specific user accounts
- 🕒 Generates timestamped alerts for incident tracking
- 📁 Exports alerts in TXT, CSV, and JSON formats

---

## 🧩 System Architecture

```mermaid
flowchart TD
    A[Windows Security Logs] --> B[Parser]
    B --> C[Detection Engine]
    C --> D[IP-Based Detection]
    C --> E[User-Based Detection]
    D --> F[Alert Generation]
    E --> F
    F --> G[TXT / CSV / JSON Reports]

## 🖥️ How to Run (Step-by-Step)

### 1. Clone the repository

```bash
git clone https://github.com/oams84/windows-threat-detection-tool.git
cd windows-threat-detection-tool

2. Ensure Python is installed
python3 --version


3. Use the sample log file

The project includes a sample Windows-style security log:

logs/windows_security.csv

Format:

timestamp,event_id,account_name,source_ip,status
2026-04-14 09:00:01,4625,admin,192.168.1.50,Failed

4. Run the tool
python3 main.py



## 📌 Note

This project uses a **sample CSV log format** to simulate Windows Security Event Logs.

In a real environment:
- Event ID 4625 = Failed Login
- Event ID 4624 = Successful Login

Future versions will support real `.evtx` Windows Event Logs.
