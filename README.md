# TASK 7: Basic Sales Summary from SQLite using Python

## Objective
Use SQL inside Python to pull simple sales info (total quantity sold, total revenue), 
display it using print statements, and visualize it using a simple matplotlib bar chart.

## Tools
- Python (with sqlite3, pandas, matplotlib)
- SQLite (built-in with Python)
- Jupyter Notebook or .py file

## Dataset
- `sales_data.db` : SQLite database with one table `sales`
- Table columns: 
    - order_date (date)
    - product_id / product_name
    - quantity (integer)
    - sales (float)

## Usage
1. Ensure Python is installed.
2. Install required packages:
   pip install pandas matplotlib
3. Place `sales_summary.py` and `sales_data.db` in the same folder.
4. Run the script:
   python sales_summary.py

## What the script does
1. Connects to `sales_data.db`.
2. Generates 3 summaries:
   - Monthly sales (`monthly_summary.csv`)
   - Overall totals (`overall_totals.csv`)
   - Per product totals (`per_product_summary.csv`)
3. Prints all summaries to console.
4. Plots a monthly sales bar chart and saves it as `sales_chart.png`.

## Outputs
- CSV files: `monthly_summary.csv`, `overall_totals.csv`, `per_product_summary.csv`
- Chart: `sales_chart.png`
- Console printouts of all summaries

## Notes
- Make sure `sales_data.db` exists and has the required `sales` table.
- The chart shows total sales per month with values on top.
