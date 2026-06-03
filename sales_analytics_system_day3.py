import numpy as np
sales = np.array([120, 134, 153, 200, 300, 102, 203])
high_sales = sales[sales >= 200]
low_sales = sales[sales < 200]
print("total weekly sales: $", sales.sum())
print("average daily sales: $", sales.mean())
print("higest sales day: ", sales.max())
print("lowest sales days: ", sales.min())
print("high sales days: ", high_sales)
print("low sales days: ", low_sales)
print("number of high sales days: ", len(high_sales))
print("higest sales day - lowest sales day: ", sales.max(), "-", sales.min(), "=", sales.max() - sales.min())