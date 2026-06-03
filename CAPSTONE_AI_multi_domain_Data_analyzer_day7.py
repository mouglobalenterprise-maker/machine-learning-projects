import numpy as np
marks = np.array([60, 75, 80, 45, 90, 55, 41, 87, 64, 32, 57, 91, 58, 82, 12, 72, 61])
sales = np.array([120, 200, 150, 90, 300, 250, 350, 500, 624, 124, 157, 234, 126, 432, 234, 250])
age   = np.array([18, 25, 40, 60, 70, 35, 46, 12, 57, 75, 65, 45, 81, 32, 51, 53, 62, 50])

print("=" * 50)
print("             STUDENT INSIGHTS")
print("=" * 50)
print("average mark: ", marks.mean())
print("passed: ", marks[marks >= 50])
print("failed: ", marks[marks < 50])

print("\n" + "=" * 50)
print("              SALES INSIGHTS")
print("=" * 50)
high_sales = sales[sales >= 200]
low_sales = sales[sales < 200]
print("total sales: $", sales.sum())
print("average daily: $", sales.mean())
print("best day: $", sales.max())
print("worst day: $", sales.min())
print("high sales: $", high_sales)
print("low sales: $", low_sales)
print("number of high sales days: ", len(high_sales))
print("higest sales day - lowest sales day: ", sales.max(), "-", sales.min(), "=", sales.max() - sales.min())

print("\n" + "=" * 50)
print("          HEALTH INSIGHTS")
print("=" * 50)
risk = age > 50
print("total patients:     ", len(age))
print("high resk count:     ",np.sum(risk))
print("high risk ages:      ", age[risk])
print("safe patient ages:    ", age[~risk])