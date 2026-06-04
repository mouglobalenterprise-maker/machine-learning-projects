import pandas as pd
sales_data = {
    "Month":        ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"],
    "Revenue":      [12000,15000,13000,18000,22000,19000,25000,21000,17000,28000,31000,35000],
    "Cost":         [8000,9500,8200,11000,13000,11500,14000,12500,10500,15000,17000,19000],
    "Target":       [14000,14000,15000,17000,20000,20000,22000,22000,18000,25000,28000,32000],
}
df =pd.DataFrame(sales_data)

df["Profit"] = df["Revenue"] - df["Cost"]
df["Margin_%"] = ((df["Profit"] / df["Revenue"]) * 100).round(1)
df["Target_Hit"] = df["Revenue"] >= df["Target"]
df["MoM_Growth_%"] = df["Revenue"].pct_change() * 100
df["MoM_Growth_%"] = df["MoM_Growth_%"].round(1)

print("\n=== FULL SALES DASHBOARD ===")
print(df.to_string(index=False))

print("\n=== ANNUAL EXECUTIVE SUMMARY ===")
print("total annual revenue: $",df["Revenue"].sum())
print("total annual profit: $",df["Profit"].sum())
print("average margin: $",(df["Margin_%"].mean()).round(1),"%")
print("month hit target: ", df["Target_Hit"].sum(),"/",len(df))
print(f"best month: {df.loc[df['Revenue'].idxmax(),'Month']}") 
print(f"worst month: {df.loc[df["Revenue"].idxmin(), "Month"]}")

missed = df[df["Target_Hit"] == False]
print("\n ==== MONTH THAT MISSED TARGET ===")
print(missed[["Month","Revenue","Target","Profit"]])

hit = df[df["Target_Hit"] == True]
print("\n=== MONTH THAT HIT TARGET===")
print(hit[["Month","Revenue","Target","Profit"]])

df["Quarter"] = ["Q1","Q1","Q1","Q2","Q2","Q2","Q3","Q3","Q3","Q4","Q4","Q4"]

print("\n=== REVENUE BY QUARTER===")
q_rev = df.groupby("Quarter")["Revenue"].sum()
print(q_rev)

print("\n===PROFIT BY QUARTER===")
q_profit = df.groupby("Quarter")["Profit"].sum()
print(q_profit)
best_margin = df.loc[df['Margin_%'].idxmax()]
print(best_margin[["Margin_%","Month"]])
print(df.to_string(index=False))