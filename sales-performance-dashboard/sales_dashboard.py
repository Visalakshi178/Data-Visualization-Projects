"""
Sales Performance Dashboard
Tools: Python, SQL, Tableau-ready exports
Author: Visalakshi Polepalli
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

# ── 1. Generate Sample Data ───────────────────────────────────────────────────
np.random.seed(42)
n = 2000

regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Clothing", "Home & Garden", "Sports", "Books"]
sales_reps = [f"Rep_{i:02d}" for i in range(1, 21)]

data = {
    "sale_id": range(1, n + 1),
    "date": pd.date_range(start="2023-01-01", periods=n, freq="12h"),
    "region": np.random.choice(regions, n),
    "product_category": np.random.choice(categories, n),
    "sales_rep": np.random.choice(sales_reps, n),
    "units_sold": np.random.randint(1, 50, n),
    "unit_price": np.round(np.random.uniform(10, 500, n), 2),
    "discount_pct": np.round(np.random.uniform(0, 0.3, n), 2),
    "customer_type": np.random.choice(["New", "Returning", "VIP"], n, p=[0.3, 0.5, 0.2]),
}

df = pd.DataFrame(data)
df["revenue"] = (df["units_sold"] * df["unit_price"] * (1 - df["discount_pct"])).round(2)
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["quarter"] = df["date"].dt.quarter
df["month_name"] = df["date"].dt.strftime("%b")

print("=" * 60)
print("SALES PERFORMANCE DASHBOARD")
print("=" * 60)
print(f"\nDataset Shape: {df.shape}")
print(f"Date Range: {df['date'].min().date()} to {df['date'].max().date()}")

# ── 2. KPI Summary ───────────────────────────────────────────────────────────
print("\n--- KPI Summary ---")
total_revenue = df["revenue"].sum()
total_units = df["units_sold"].sum()
avg_order_value = df["revenue"].mean()
top_region = df.groupby("region")["revenue"].sum().idxmax()
top_category = df.groupby("product_category")["revenue"].sum().idxmax()
top_rep = df.groupby("sales_rep")["revenue"].sum().idxmax()

print(f"Total Revenue:       ${total_revenue:,.2f}")
print(f"Total Units Sold:    {total_units:,}")
print(f"Avg Order Value:     ${avg_order_value:,.2f}")
print(f"Top Region:          {top_region}")
print(f"Top Category:        {top_category}")
print(f"Top Sales Rep:       {top_rep}")

# ── 3. YoY Trend ─────────────────────────────────────────────────────────────
yoy = df.groupby(["year", "month"])["revenue"].sum().reset_index()
yoy_pivot = yoy.pivot(index="month", columns="year", values="revenue")
print("\n--- YoY Monthly Revenue ---")
print(yoy_pivot.round(2))

# ── 4. Regional Breakdown ─────────────────────────────────────────────────────
regional = df.groupby("region").agg(
    total_revenue=("revenue", "sum"),
    total_units=("units_sold", "sum"),
    avg_discount=("discount_pct", "mean"),
    num_transactions=("sale_id", "count")
).round(2).sort_values("total_revenue", ascending=False)
print("\n--- Regional Performance ---")
print(regional)

# ── 5. Category Drill-Down ────────────────────────────────────────────────────
category_perf = df.groupby(["product_category", "quarter"])["revenue"].sum().unstack()
print("\n--- Revenue by Category & Quarter ---")
print(category_perf.round(2))

# ── 6. Visualizations ────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Sales Performance Dashboard", fontsize=18, fontweight="bold")

colors = ["#2196F3", "#4CAF50", "#FF9800", "#E91E63", "#9C27B0"]

# Monthly revenue trend
monthly_rev = df.groupby(["year", "month"])["revenue"].sum().reset_index()
for yr in monthly_rev["year"].unique():
    subset = monthly_rev[monthly_rev["year"] == yr]
    axes[0, 0].plot(subset["month"], subset["revenue"], marker="o", label=str(yr), linewidth=2)
axes[0, 0].set_title("Monthly Revenue Trend (YoY)")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Revenue ($)")
axes[0, 0].legend()
axes[0, 0].set_xticks(range(1, 13))

# Revenue by region
region_rev = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
axes[0, 1].bar(region_rev.index, region_rev.values, color=colors[:4])
axes[0, 1].set_title("Revenue by Region")
axes[0, 1].set_xlabel("Region")
axes[0, 1].set_ylabel("Revenue ($)")

# Revenue by category
cat_rev = df.groupby("product_category")["revenue"].sum().sort_values(ascending=True)
axes[0, 2].barh(cat_rev.index, cat_rev.values, color=colors)
axes[0, 2].set_title("Revenue by Product Category")
axes[0, 2].set_xlabel("Revenue ($)")

# Quarterly performance
quarterly = df.groupby("quarter")["revenue"].sum()
axes[1, 0].bar(["Q1", "Q2", "Q3", "Q4"], quarterly.values, color=colors[:4])
axes[1, 0].set_title("Quarterly Revenue")
axes[1, 0].set_ylabel("Revenue ($)")

# Customer type breakdown
cust_rev = df.groupby("customer_type")["revenue"].sum()
axes[1, 1].pie(cust_rev.values, labels=cust_rev.index, autopct="%1.1f%%",
               colors=colors[:3], startangle=140)
axes[1, 1].set_title("Revenue by Customer Type")

# Top 10 Sales Reps
top_reps = df.groupby("sales_rep")["revenue"].sum().nlargest(10).sort_values()
axes[1, 2].barh(top_reps.index, top_reps.values, color="#2196F3")
axes[1, 2].set_title("Top 10 Sales Reps by Revenue")
axes[1, 2].set_xlabel("Revenue ($)")

plt.tight_layout()
plt.savefig("sales_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nPlot saved: sales_dashboard.png")

# ── 7. Export Tableau-Ready Data ─────────────────────────────────────────────
df.to_csv("sales_data.csv", index=False)
regional.to_csv("regional_summary.csv")
category_perf.to_csv("category_quarterly.csv")
print("Exported: sales_data.csv, regional_summary.csv, category_quarterly.csv")
print("\nDone!")
