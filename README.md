# Data Quality & SLA Monitoring System

## Overview
This project simulates a real-world data operations system that monitors data quality and SLA compliance.

## Features
- Detects missing values, duplicates, and anomalies
- Monitors SLA breaches for delayed data
- Generates automated incident reports
- Visualizes issues in Power BI dashboard

## Tech Stack
- Python (Pandas)
- SQL (optional)
- Power BI

## Business Value
- Reduces manual data validation effort
- Improves data reliability
- Enables faster issue detection and resolution

## How to Run
1. Place dataset in /data folder
2. Run data_cleaning.py
3. Run quality_checks.py
4. Check output/incident_report.csv

## Future Improvements
- Email alerts
- Automated pipeline (Airflow)
- Cloud deployment