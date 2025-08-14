import sqlite3
import pandas as pd

# Step 1: Read the Excel file
excel_file = "online_sales.xlsx"
df = pd.read_excel(excel_file)

# Optional: Display to check if data is loaded correctly
print("Excel Data Preview:")
print(df.head())

# Step 2: Connect to SQLite database (or create if it doesn’t exist)
conn = sqlite3.connect("sales_data.db")

# Step 3: Save the dataframe into a table named 'sales'
# If the table already exists, replace it
df.to_sql("sales", conn, if_exists="replace", index=False)

# Step 4: Close connection
conn.close()

print(f"Database 'sales_data.db' created successfully with data from '{excel_file}'.")
