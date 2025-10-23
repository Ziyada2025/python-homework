1. 
import pandas as pd
import numpy as np

def complete_homework_solution():
    """
    Complete homework solution with error handling and explanations
    """
    
    # Given data
    data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
            'Age': [25, 30, 35, 40], 
            'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
    
    try:
        df = pd.DataFrame(data)
        print("🎓 HOMEWORK 1 SOLUTION")
        print("=" * 50)
        print("Original DataFrame:")
        print(df)
        
        # 1. Rename columns
        print("\n" + "="*50)
        print("1. RENAMING COLUMNS")
        print("   Changing: 'First Name' → 'first_name', 'Age' → 'age', 'City' → 'city'")
        
        df_renamed = df.rename(columns={
            'First Name': 'first_name',
            'Age': 'age', 
            'City': 'city'
        })
        print("   Result:")
        print(df_renamed)
        
        # 2. First 3 rows
        print("\n" + "="*50)
        print("2. FIRST 3 ROWS")
        first_three = df_renamed.head(3)
        print(first_three)
        
        # 3. Mean age
        print("\n" + "="*50)
        print("3. MEAN AGE CALCULATION")
        mean_age = df_renamed['age'].mean()
        print(f"   Mean age = {mean_age}")
        print(f"   Calculation: ({' + '.join(map(str, df_renamed['age']))}) / {len(df_renamed)} = {mean_age}")
        
        # 4. Select columns
        print("\n" + "="*50)
        print("4. SELECTING COLUMNS: 'first_name' and 'city'")
        selected_cols = df_renamed[['first_name', 'city']]
        print(selected_cols)
        
        # 5. Add salary column
        print("\n" + "="*50)
        print("5. ADDING 'salary' COLUMN")
        np.random.seed(123)  # For reproducible random values
        df_renamed['salary'] = np.random.randint(50000, 100001, size=len(df_renamed))
        print("   Added random salaries between $50,000 and $100,000")
        print(df_renamed)
        
        # 6. Summary statistics
        print("\n" + "="*50)
        print("6. SUMMARY STATISTICS")
        stats = df_renamed.describe()
        print(stats)
        
        # Additional: Information about the DataFrame
        print("\n" + "="*50)
        print("ADDITIONAL INFORMATION")
        print(f"DataFrame shape: {df_renamed.shape}")
        print(f"Columns: {list(df_renamed.columns)}")
        print(f"Data types:\n{df_renamed.dtypes}")
        
        return df_renamed
        
    except Exception as e:
        print(f"Error: {e}")
        return None

# Run the complete solution
final_df = complete_homework_solution() 
2. 
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

print("Sales and Expenses DataFrame:")
print(sales_and_expenses)
print("\n" + "="*50)

# Calculate and display maximum values
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

print("\n1. MAXIMUM VALUES:")
print(f"   Maximum Sales: ${max_sales:,}")
print(f"   Maximum Expenses: ${max_expenses:,}")

# Calculate and display minimum values
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

print("\n2. MINIMUM VALUES:")
print(f"   Minimum Sales: ${min_sales:,}")
print(f"   Minimum Expenses: ${min_expenses:,}")

# Calculate and display average values
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

print("\n3. AVERAGE VALUES:")
print(f"   Average Sales: ${avg_sales:,.2f}")
print(f"   Average Expenses: ${avg_expenses:,.2f}")

# Additional: Display all statistics together
print("\n4. COMPREHENSIVE STATISTICS:")
print(sales_and_expenses[['Sales', 'Expenses']].describe()) 
3. 
import pandas as pd

# Create the DataFrame
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)
print("Original Expenses DataFrame:")
print(expenses)
print("\n" + "="*50)

# Set 'Category' as index
expenses_indexed = expenses.set_index('Category')
print("\nDataFrame with 'Category' as index:")
print(expenses_indexed)
print("\n" + "="*50)

# Calculate and display maximum expense for each category
max_expenses = expenses_indexed.max(axis=1)
print("\n1. MAXIMUM EXPENSE FOR EACH CATEGORY:")
print(max_expenses)

# Calculate and display minimum expense for each category
min_expenses = expenses_indexed.min(axis=1)
print("\n2. MINIMUM EXPENSE FOR EACH CATEGORY:")
print(min_expenses)

# Calculate and display average expense for each category
avg_expenses = expenses_indexed.mean(axis=1)
print("\n3. AVERAGE EXPENSE FOR EACH CATEGORY:")
print(avg_expenses)
