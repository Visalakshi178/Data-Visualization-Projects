# 📊 Sales Performance Dashboard

> Interactive sales analytics with regional KPIs, YoY trends, and drill-down filtering by product category and time period.

## 📊 Overview

This project delivers a comprehensive sales performance analysis covering 2,000+ transactions across regions, product categories, and sales reps. It provides KPI summaries, year-over-year comparisons, and Tableau-ready exports for interactive dashboard publishing.

## 🛠️ Tools & Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)

## 📁 Project Structure

```
sales-performance-dashboard/
│
├── sales_dashboard.py        # Main analysis & visualization script
├── sales_data.csv            # Full transaction dataset (Tableau-ready)
├── regional_summary.csv      # Regional KPI breakdown
├── category_quarterly.csv    # Category × Quarter revenue matrix
├── sales_dashboard.png       # Dashboard screenshot
└── README.md
```

## 🔍 Key Steps

1. **Data Generation** — Simulated 2,000 sales transactions across regions, categories, and reps
2. **KPI Calculation** — Total revenue, units sold, avg order value, top performers
3. **YoY Analysis** — Month-over-month and year-over-year revenue comparisons
4. **Regional Breakdown** — Revenue, units, and discount analysis by region
5. **Category Drill-Down** — Revenue by product category and quarter
6. **Dashboard Export** — CSV exports formatted for direct Tableau ingestion

## 📈 Key Metrics Tracked

| KPI | Description |
|-----|-------------|
| Total Revenue | Sum of all net sales |
| YoY Growth | Month-level comparison across years |
| Regional Performance | Revenue & units by North/South/East/West |
| Category Mix | Revenue share by product category |
| Top Sales Reps | Ranked by total revenue contribution |
| Customer Type | New vs Returning vs VIP revenue split |

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib seaborn
python sales_dashboard.py
```

Then import `sales_data.csv` into Tableau for interactive filtering.

## 📬 Contact

**Visalakshi Polepalli** — [LinkedIn](https://linkedin.com/in/visalakshi-polepalli17)
