# 🔍 Admin Panel Monitoring & Web Access Insights (Splunk Dashboard)

This project showcases a custom Splunk dashboard built to monitor an internal admin panel by analyzing simulated Apache access logs. It highlights API health, client access trends, slow endpoints, suspicious usage patterns, and traffic breakdowns by device/browser.

---

## 📊 Dashboard Preview

![Admin Panel Monitoring   Web Access Insights Dashboard](https://github.com/user-attachments/assets/b0acbcd7-b067-4f2d-b28c-3dcf9cc2c834)

---

## ✅ Use Case Summary

| Panel | Description |
|-------|-------------|
| **APIs with Highest Error Rates** | Identify endpoints returning high volumes of 4xx/5xx errors. |
| **Error Trends by Status Code** | Visualize daily spikes in HTTP error categories. |
| **Slowest Performing Endpoints** | Detect APIs with high average response times. |
| **Requests by Device Type & Browser** | Analyze traffic split by device and browser from the user agent. |
| **Top Active Clients (by IP)** | Identify the most active users hitting the system. |
| **Suspicious Access Patterns** | Detect POST/PUT requests with repeated 5xx errors. |
| **Simulated Alert: 5xx Spikes** | Show error bursts over 12-hour windows for alert simulation. |

---

## ⚙️ SPL Queries Used

📁 All queries are saved in [`queries/spl_queries.txt`](./queries/spl_queries.txt).

---

## 🧪 Dataset Info

- Type: Synthetic Apache logs generated using a Python script
- Data Range: Multi-month span (2023–2025)
- Fields Used: uri_path, status, method, clientip, useragent, response_time

---

## 🛠️ Tools & Tech

- Splunk Enterprise (60-day trial)
- Custom Python log generator
- SPL (Search Processing Language)
- Dashboard XML & UI Editor

---
