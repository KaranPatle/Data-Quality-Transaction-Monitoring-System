# 📊 Data Quality & Transaction Monitoring System

### End-to-End Data Quality Monitoring using Python, SQL & Power BI

---

## 📌 Problem Statement

In real-world business environments, data often contains issues such as missing values, duplicates, invalid entries, and anomalies.  
These issues can lead to incorrect analysis, misleading dashboards, and poor business decisions.

Manual data validation is inefficient and does not scale with large datasets.

---

## 🎯 Solution

This project builds an **automated Data Quality Monitoring System** that:

- Detects data quality issues (missing values, duplicates, anomalies)
- Cleans and standardizes data using SQL
- Generates automated data quality reports using Python
- Monitors SLA (data arrival time)
- Provides business insights through Power BI (in progress)

---

## ⚙️ Tech Stack

- **Python** (Pandas, Faker)
- **SQL (MySQL)** for data cleaning and validation
- **Power BI** for dashboarding (in progress)

---

## 🧱 Project Workflow
# 📊 Data Quality & Transaction Monitoring System

### End-to-End Data Quality Monitoring using Python, SQL & Power BI

---

## 📌 Problem Statement

In real-world business environments, data often contains issues such as missing values, duplicates, invalid entries, and anomalies.  
These issues can lead to incorrect analysis, misleading dashboards, and poor business decisions.

Manual data validation is inefficient and does not scale with large datasets.

---

## 🎯 Solution

This project builds an **automated Data Quality Monitoring System** that:

- Detects data quality issues (missing values, duplicates, anomalies)
- Cleans and standardizes data using SQL
- Generates automated data quality reports using Python
- Monitors SLA (data arrival time)
- Provides business insights through Power BI (in progress)

---

## ⚙️ Tech Stack

- **Python** (Pandas, Faker)
- **SQL (MySQL)** for data cleaning and validation
- **Power BI** for dashboarding (in progress)

---

## 🧱 Project Workflow
Data Generation → SQL Cleaning → Data Quality Checks → SLA Monitoring → Report Generation → Dashboard



---

## 🔍 Features

- ✅ Synthetic data generation with real-world issues  
- ✅ Duplicate detection and removal  
- ✅ Missing value detection  
- ✅ Negative value handling  
- ✅ Outlier detection using statistical methods  
- ✅ SLA monitoring for data arrival validation  
- ✅ Automated data quality report generation  

---

## 📊 Key Insights

- Detected and corrected **109 negative transactions**
- Achieved **0 missing values after cleaning**
- Identified potential anomalies using statistical thresholds
- Improved overall data reliability for downstream analysis

---


---

## 📈 Output

The system generates a **Data Quality Report**:

| Check              | Count | Status   |
|-------------------|------|----------|
| Missing Values     | 0    | OK       |
| Negative Values    | 109  | WARNING  |
| Future Dates       | 0    | OK       |

---

## 📊 Dashboard (In Progress)

A Power BI dashboard is being developed to visualize:

- Data quality metrics  
- Revenue trends  
- Customer behavior  
- Anomaly detection  

---

## 🚀 How to Run

```bash
# Clone repository
git clone https://github.com/KaranPatle/Data-Quality-Transaction-Monitoring-System.git

# Navigate to project folder
cd Data-Quality-Transaction-Monitoring-System

# Install dependencies
pip install -r requirements.txt

# Generate dataset
python src/generator.py

# Run quality checks
python src/quality_checks.py

# Run SLA monitoring
python src/sla_monitor.py


💼 Real-World Use Cases
Banking & FinTech → Fraud detection and transaction validation
E-commerce → Clean sales data before reporting
Business Intelligence → Ensure reliable dashboards
Data Engineering → Automated data validation pipelines
