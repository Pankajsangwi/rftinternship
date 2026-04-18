import pandas as pd

# Create DataFrame
data = {
    "NAME": ["A", "B", "C", "D"],
    "DEPT": ["IT", "HR", "IT", "HR"],
    "SALARY": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

# Display Data
print("Employee Data:\n")
print(df)

# 1. Average Salary Per Department
print("\nAverage Salary Per Department:")
avg_salary = df.groupby("DEPT")["SALARY"].mean()
print(avg_salary)

# 2. Highest Paid Employee Per Department
print("\nHighest Paid Employee Per Department:")
highest_paid = df.loc[df.groupby("DEPT")["SALARY"].idxmax()]
print(highest_paid)

# Bonus 1. Count Employees Per Department
print("\nCount Employees Per Department:")
count_emp = df.groupby("DEPT")["NAME"].count()
print(count_emp)

# Bonus 2. Sort Departments by Average Salary
print("\nDepartments Sorted by Average Salary:")
sorted_dept = avg_salary.sort_values(ascending=False)
print(sorted_dept)