1. 
import matplotlib.pyplot as plt 
# Exercise 1: Calculate the average grade for each student
df1['Average_Grade'] = df1[['Math', 'English', 'Science']].mean(axis=1).round(2)
print("Exercise 1 - DataFrame with Average Grade:")
print(df1[['Student_ID', 'Average_Grade']])
print("\n" + "="*50 + "\n")

# Exercise 2: Find the student with the highest average grade
highest_avg_student = df1.loc[df1['Average_Grade'].idxmax()]
print("Exercise 2 - Student with Highest Average Grade:")
print(f"Student ID: {highest_avg_student['Student_ID']}")
print(f"Average Grade: {highest_avg_student['Average_Grade']}")
print(f"Math: {highest_avg_student['Math']}, English: {highest_avg_student['English']}, Science: {highest_avg_student['Science']}")
print("\n" + "="*50 + "\n")

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student
df1['Total'] = df1['Math'] + df1['English'] + df1['Science']
print("Exercise 3 - DataFrame with Total Marks:")
print(df1[['Student_ID', 'Math', 'English', 'Science', 'Total']])
print("\n" + "="*50 + "\n")

# Exercise 4: Plot a bar chart to visualize the average grades in each subject
subject_means = df1[['Math', 'English', 'Science']].mean()

plt.figure(figsize=(10, 6))
bars = plt.bar(subject_means.index, subject_means.values, color=['skyblue', 'lightcoral', 'lightgreen'])
plt.title('Average Grades by Subject', fontsize=16, fontweight='bold')
plt.xlabel('Subjects', fontsize=12)
plt.ylabel('Average Grade', fontsize=12)
plt.ylim(75, 95)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.3,
             f'{height:.1f}', ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Display the complete final DataFrame
print("Exercise 4 - Complete Final DataFrame:")
print(df1)
print(f"\nSubject Averages:")
print(f"Math: {subject_means['Math']:.2f}")
print(f"English: {subject_means['English']:.2f}")
print(f"Science: {subject_means['Science']:.2f}") 
2. 
import matplotlib.pyplot as plt 
# Exercise 1: Calculate the total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Exercise 1 - Total Sales for Each Product:")
for product, total in total_sales.items():
    print(f"{product}: {total}")
print("\n" + "="*60 + "\n")

# Exercise 2: Find the date with the highest total sales
df2['Total_Sales'] = df2['Product_A'] + df2['Product_B'] + df2['Product_C']
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
max_sales_value = df2['Total_Sales'].max()
print("Exercise 2 - Date with Highest Total Sales:")
print(f"Date: {max_sales_date.strftime('%Y-%m-%d')}")
print(f"Total Sales: {max_sales_value}")
print(f"Breakdown - Product_A: {df2.loc[df2['Total_Sales'].idxmax(), 'Product_A']}, "
      f"Product_B: {df2.loc[df2['Total_Sales'].idxmax(), 'Product_B']}, "
      f"Product_C: {df2.loc[df2['Total_Sales'].idxmax(), 'Product_C']}")
print("\n" + "="*60 + "\n")

# Exercise 3: Calculate the percentage change in sales for each product from the previous day
df2_pct_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
df2_pct_change = df2_pct_change.round(2)
df2_pct_change.insert(0, 'Date', df2['Date'])
print("Exercise 3 - Percentage Change in Sales from Previous Day:")
print(df2_pct_change)
print("\n" + "="*60 + "\n")

# Exercise 4: Plot a line chart to visualize the sales trends for each product over time
plt.figure(figsize=(12, 8))

# Plot each product line
plt.plot(df2['Date'], df2['Product_A'], marker='o', linewidth=2, label='Product A', color='blue')
plt.plot(df2['Date'], df2['Product_B'], marker='s', linewidth=2, label='Product B', color='red')
plt.plot(df2['Date'], df2['Product_C'], marker='^', linewidth=2, label='Product C', color='green')

plt.title('Sales Trends for Products A, B, and C (Jan 2023)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Add some styling
plt.tight_layout()
plt.show()

# Display additional analysis
print("Exercise 4 - Additional Sales Analysis:")
print(f"Average Daily Sales:")
print(f"Product A: {df2['Product_A'].mean():.2f}")
print(f"Product B: {df2['Product_B'].mean():.2f}")
print(f"Product C: {df2['Product_C'].mean():.2f}")

print(f"\nMaximum Single Day Sales:")
print(f"Product A: {df2['Product_A'].max()} (on {df2.loc[df2['Product_A'].idxmax(), 'Date'].strftime('%Y-%m-%d')})")
print(f"Product B: {df2['Product_B'].max()} (on {df2.loc[df2['Product_B'].idxmax(), 'Date'].strftime('%Y-%m-%d')})")
print(f"Product C: {df2['Product_C'].max()} (on {df2.loc[df2['Product_C'].idxmax(), 'Date'].strftime('%Y-%m-%d')})")

# Display the final DataFrame with all calculations
print("\n" + "="*60)
print("Final DataFrame with Total Sales:")
print(df2[['Date', 'Product_A', 'Product_B', 'Product_C', 'Total_Sales']]) 
3. 
import matplotlib.pyplot as plt  
# Exercise 1: Calculate the average salary for each department
avg_salary_by_dept = df3.groupby('Department')['Salary'].mean().round(2)
print("Exercise 1 - Average Salary for Each Department:")
print(avg_salary_by_dept)
print("\n" + "="*70 + "\n")

# Exercise 2: Find the employee with the most experience
most_experienced_employee = df3.loc[df3['Experience (Years)'].idxmax()]
print("Exercise 2 - Employee with Most Experience:")
print(f"Name: {most_experienced_employee['Name']}")
print(f"Employee ID: {most_experienced_employee['Employee_ID']}")
print(f"Department: {most_experienced_employee['Department']}")
print(f"Experience: {most_experienced_employee['Experience (Years)']} years")
print(f"Salary: ${most_experienced_employee['Salary']:,}")
print("\n" + "="*70 + "\n")

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase 
# in salary from the minimum salary in the dataframe
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary * 100).round(2)
print("Exercise 3 - DataFrame with Salary Increase Percentage:")
print(df3[['Employee_ID', 'Name', 'Salary', 'Salary Increase']])
print(f"\nMinimum Salary in the company: ${min_salary:,}")
print("\n" + "="*70 + "\n")

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments
dept_distribution = df3['Department'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
bars = plt.bar(dept_distribution.index, dept_distribution.values, 
               color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])

plt.title('Employee Distribution Across Departments', fontsize=16, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('Number of Employees', fontsize=12)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.05,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Additional detailed analysis
print("Exercise 4 - Department Distribution Analysis:")
print(dept_distribution)
print(f"\nTotal number of employees: {len(df3)}")

# Display comprehensive summary
print("\n" + "="*70)
print("COMPREHENSIVE SUMMARY")
print("="*70)

print("\nDepartment-wise Analysis:")
dept_summary = df3.groupby('Department').agg({
    'Salary': ['count', 'mean', 'min', 'max'],
    'Experience (Years)': 'mean'
}).round(2)

dept_summary.columns = ['Employee Count', 'Avg Salary', 'Min Salary', 'Max Salary', 'Avg Experience']
print(dept_summary)

print(f"\nOverall Company Statistics:")
print(f"Total Employees: {len(df3)}")
print(f"Average Salary: ${df3['Salary'].mean():,.2f}")
print(f"Salary Range: ${df3['Salary'].min():,} - ${df3['Salary'].max():,}")
print(f"Average Experience: {df3['Experience (Years)'].mean():.1f} years")

# Salary increase analysis
print(f"\nSalary Increase Analysis (from minimum ${min_salary:,}):")
print(f"Highest increase: {df3['Salary Increase'].max():.2f}% (${df3.loc[df3['Salary Increase'].idxmax(), 'Salary']:,})")
print(f"Lowest increase: {df3['Salary Increase'].min():.2f}% (${df3.loc[df3['Salary Increase'].idxmin(), 'Salary']:,})") 
4. 
import matplotlib.pyplot as plt 
# Exercise 1: Calculate the total revenue from all orders
total_revenue = df4['Total_Price'].sum()
print("Exercise 1 - Total Revenue from All Orders:")
print(f"Total Revenue: ${total_revenue:,}")
print("\n" + "="*60 + "\n")

# Exercise 2: Find the most ordered product
product_orders = df4['Product'].value_counts()
most_ordered_product = product_orders.idxmax()
most_ordered_count = product_orders.max()

print("Exercise 2 - Most Ordered Product:")
print(f"Product: {most_ordered_product}")
print(f"Number of Orders: {most_ordered_count}")
print(f"\nOrder Count by Product:")
for product, count in product_orders.items():
    print(f"  Product {product}: {count} orders")
print("\n" + "="*60 + "\n")

# Exercise 3: Calculate the average quantity of products ordered
avg_quantity = df4['Quantity'].mean()
print("Exercise 3 - Average Quantity of Products Ordered:")
print(f"Average Quantity: {avg_quantity:.2f} units per order")
print("\n" + "="*60 + "\n")

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products
product_revenue = df4.groupby('Product')['Total_Price'].sum()

plt.figure(figsize=(10, 8))
colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
wedges, texts, autotexts = plt.pie(product_revenue.values, 
                                   labels=product_revenue.index, 
                                   autopct='%1.1f%%',
                                   colors=colors, 
                                   startangle=90,
                                   shadow=True,
                                   explode=(0.05, 0.05, 0.05))

# Enhance the pie chart appearance
plt.title('Distribution of Sales Revenue by Product', fontsize=16, fontweight='bold', pad=20)

# Improve text appearance
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

plt.axis('equal')
plt.tight_layout()
plt.show()

# Additional detailed analysis
print("Exercise 4 - Detailed Sales Distribution Analysis:")
print("\nRevenue by Product:")
for product, revenue in product_revenue.items():
    percentage = (revenue / total_revenue) * 100
    print(f"  Product {product}: ${revenue:,} ({percentage:.1f}%)")

print(f"\nTotal Revenue: ${total_revenue:,}")
