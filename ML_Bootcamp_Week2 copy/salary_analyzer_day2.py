import pandas as pd
employees = {
    "Name":         ["ola", "sola", "bolu", "tope", "sola", "titi", "tolu", "felix", "lanre", "mary", "lena", "tom"],
    "Department":   ["engineering", "HR", "engineering", "marketing", "HR", "marketing", "engineering", "HR", "marketing", "engineering", "HR", "marketing",],
    "Level":        ["senior", "junior", "junior", "senior", "senior", "junior", "senior", "senior", "junior", "junior", "senior", "senior",],
    "Salary":       [50000, 32000, 48000, 60000, 55000, 28000, 85000, 50000, 35000, 45000, 58000, 62000]
}
df = pd.DataFrame(employees)
print("Employee Records Loaded:", df.shape)

print("\n=== OVERALL SALARY STATS ===")
print(f"total payroll:  ${df['Salary'].sum()}")
print("average salary: $",df["Salary"].mean())
print("higest salary: $",df["Salary"].max())
print("lowest salary: $",df["Salary"].min())

print("\n=== AVERAGE SALARY BY DEPARTMENT ===")
dept_avg = df.groupby("Department")["Salary"].mean()
print(dept_avg.sort_values(ascending=False))

print("\n=== TOTAL PAYROLL BY DEPARTMENT ===")
dept_avg = df.groupby("Department")["Salary"].sum()
print(dept_avg.sort_values(ascending=False))

print("\n=== HEADCOUNT BY DEPARTMENT ===")
dept_count = df.groupby("Department")["Salary"].count()
print(dept_count)

high_earners = df[df["Salary"] >= 60000]
mid_earners = df[(df["Salary"] >= 40000) & (df["Salary"] < 60000)]
low_earners = df[df["Salary"] < 40000]

print("\n=== SALARY BAND DISTRIBUTION ===")
print("high (>= $60k):", len(high_earners), "employees")
print("mid ($40K- $60k):", len(mid_earners), "employees")
print("low (< $40k):", len(low_earners), "employees")

print("\n=== HIGH EARNER DETAILS ===")
print(high_earners[["Name", "Department", "Level", "Salary"]])

print("\n=== SENIOR VS JUNIOR AVERAGE SALARY ===")
level_avg = df.groupby("Level")["Salary"].mean()
print(level_avg)
cross = df.groupby(["Department", "Level"])["Salary"].mean()
print(cross)