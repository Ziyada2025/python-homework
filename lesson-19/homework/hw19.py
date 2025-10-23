1. 
import pandas as pd
import numpy as np

# Load the dataset 
path='C:\\Users\\Ziyada\\Desktop\\python\\sales_data.csv'
df = pd.read_csv(path)

# Display basic information about the dataset
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Dataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print("\nFirst 5 rows:")
print(df.head())
print("\n" + "="*50)

# Check for missing values and data types
print("\nDATA INFORMATION")
print("=" * 50)
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())
print("\n" + "="*50)
# Task 1: Group by Category and get stats
print("\n1. CATEGORY STATISTICS:")
print("-" * 30)

# Group by category and calculate what we need
category_group = df.groupby('Category')

# Total quantity sold per category
total_quantity = category_group['Quantity'].sum()
print("Total quantity sold:")
print(total_quantity)
print()

# Average price per category  
avg_price = category_group['Price'].mean()
print("Average price:")
print(avg_price.round(2))
print()

# Maximum quantity in single sale per category
max_quantity = category_group['Quantity'].max()
print("Max quantity in one sale:")
print(max_quantity)
print()

# Task 2: Top product in each category
print("\n2. TOP PRODUCTS IN EACH CATEGORY:")
print("-" * 30)

# Find which product sold the most in each category
for category in df['Category'].unique():
    # Get data for this category only
    category_data = df[df['Category'] == category]
    
    # Group by product and sum quantities
    product_sales = category_data.groupby('Product')['Quantity'].sum()
    
    # Find the product with highest total sales
    top_product = product_sales.idxmax()
    top_quantity = product_sales.max()
    
    print(f"{category}: {top_product} ({top_quantity} units)")

# Task 3: Best sales day
print("\n3. BEST SALES DAY:")
print("-" * 30)

# Calculate total sales for each transaction
df['Total_Sales'] = df['Quantity'] * df['Price']

# Group by date and sum total sales
daily_sales = df.groupby('Date')['Total_Sales'].sum()

# Find the date with maximum sales
best_date = daily_sales.idxmax()
best_sales = daily_sales.max()

print(f"Date: {best_date}")
print(f"Total Sales: ${best_sales:,.2f}")
2. 
import pandas as pd

# Load data
df = pd.read_csv('C:\\Users\\Ziyada\\Desktop\\python\\customer_orders.csv')

print("SIMPLE CUSTOMER ANALYSIS")
print("=" * 35)

# Task 1: Customers with 20+ orders
print("\nTASK 1: Customers with 20+ orders")
customer_orders = df.groupby('CustomerID')['OrderID'].count()
result1 = customer_orders[customer_orders >= 20]
print(result1)

# Task 2: Customers with average price > $120  
print("\nTASK 2: Customers with avg price > $120")
avg_prices = df.groupby('CustomerID')['Price'].mean()
result2 = avg_prices[avg_prices > 120]
print(result2.round(2))

# Task 3: Products with 5+ units sold
print("\nTASK 3: Products with 5+ units sold")
product_quantities = df.groupby('Product')['Quantity'].sum()
result3 = product_quantities[product_quantities >= 5]
print(result3) 
3. 
import pandas as pd
import sqlite3

# 1. Get data from SQL
conn = sqlite3.connect('C:\\Users\\Ziyada\\Desktop\\python\\population.db')
df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

print("DATABASE INFO:")
print("Columns:", df.columns.tolist())
print("First row:", df.iloc[0].to_dict())

# MANUAL CONFIGURATION - Adjust these based on what you see above:
SALARY_COLUMN = 'salary'    # Change to your actual salary column name
STATE_COLUMN = 'state'      # Change to your actual state column name

print(f"\nUsing: Salary='{SALARY_COLUMN}', State='{STATE_COLUMN}'")

# Define salary bands
bands = [
    ('till $200,000', 0, 200000),
    ('$200,001 - $400,000', 200001, 400000),
    ('$400,001 - $600,000', 400001, 600000),
    ('$600,001 - $800,000', 600001, 800000),
    ('$800,001 - $1,000,000', 800001, 1000000),
    ('$1,000,001 - $1,200,000', 1000001, 1200000),
    ('$1,200,001 - $1,400,000', 1200001, 1400000),
    ('$1,400,001 - $1,600,000', 1400001, 1600000),
    ('$1,600,001 - $1,800,000', 1600001, 1800000),
    ('$1,800,001 and over', 1800001, float('inf'))
]

# Categorize salaries
def categorize(salary):
    for name, min_val, max_val in bands:
        if min_val <= salary <= max_val:
            return name
    return 'Unknown'

df['Category'] = df[SALARY_COLUMN].apply(categorize)

# Calculate results
print("\nSALARY BAND RESULTS:")
total = len(df)
salary_results = df.groupby('Category').agg(
    Population=(SALARY_COLUMN, 'count'),
    Avg_Salary=(SALARY_COLUMN, 'mean'),
    Median_Salary=(SALARY_COLUMN, 'median')
).round(2)

salary_results['Percentage'] = (salary_results['Population'] / total * 100).round(2)
print(salary_results)

if STATE_COLUMN in df.columns:
    print(f"\nSTATE RESULTS:")
    state_results = df.groupby(STATE_COLUMN).agg(
        Population=(SALARY_COLUMN, 'count'),
        Avg_Salary=(SALARY_COLUMN, 'mean'),
        Median_Salary=(SALARY_COLUMN, 'median')
    ).round(2)
    
    state_results['Percentage'] = (state_results['Population'] / total * 100).round(2)
    print(state_results)
