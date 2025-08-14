import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
import calendar

db_path = "sales_data.db"  # change if needed
conn = sqlite3.connect(db_path)
output_folder = os.path.dirname(os.path.abspath(__file__))
monthly_query = """
SELECT 
    strftime('%m', order_date) AS month,
    SUM(sales) AS total_sales
FROM sales
WHERE order_date IS NOT NULL
GROUP BY month
ORDER BY month;
"""
monthly_df = pd.read_sql_query(monthly_query, conn)
monthly_df = monthly_df.dropna(subset=['month'])
monthly_df['month'] = monthly_df['month'].astype(str)
print("=== Monthly Sales Summary ===")
print(monthly_df)

monthly_df.to_csv(os.path.join(output_folder, "monthly_summary.csv"), index=False)
overall_query = """
SELECT 
    SUM(sales) AS total_sales,
    SUM(quantity) AS total_quantity
FROM sales;
"""
overall_df = pd.read_sql_query(overall_query, conn)
print("\n=== Overall Totals ===")
print(overall_df)
overall_df.to_csv(os.path.join(output_folder, "overall_totals.csv"), index=False)
product_query = """
SELECT 
    product_id,
    SUM(sales) AS total_sales,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_id
ORDER BY total_sales DESC;
"""
product_df = pd.read_sql_query(product_query, conn)
print("\n=== Per Product Summary ===")
print(product_df)
product_df.to_csv(os.path.join(output_folder, "per_product_summary.csv"), index=False)
conn.close()
plt.figure(figsize=(8, 5))
monthly_df['month_name'] = monthly_df['month'].astype(int).apply(lambda x: calendar.month_abbr[x])

bars = plt.bar(monthly_df['month_name'], monthly_df['total_sales'], color='skyblue')

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Summary")
for bar, value in zip(bars, monthly_df['total_sales']):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{value:,.0f}",
        ha='center',
        va='bottom',
        fontsize=9
    )

plt.tight_layout()
plt.savefig(os.path.join(output_folder, "sales_chart.png"))
plt.show()
