import pandas as pd
students = {
    "Name":     ["john", "mary", "anna", "paul", "lena", "tom", "sera", "ola"],
   "Age":       [20, 22, 19, 21, 23, 20, 22, 19],
    "Subject":  ["math", "math", "sciene", "sciene", "math", "sciene", "math", "sciene"],
    "Marks":    [60, 75, 80, 45, 90, 55, 88, 42],
    "Grade":    ["c", "b", "a", "f", "a", "d", "a", "f"]
}
df =pd.DataFrame(students)
print("=== DATA PREVIEW ===")
print(df.head)

print("=== DATA SHAPE ===")
print(df.shape)

print("=== COLOUMN TYPES ===")
print(df.info())

print("=== STSTISTICAL SUMMARY ===")
print(df.describe())
passed = df[df["Marks"] >= 50]
failed = df[df['Marks'] < 50]

print("\n=== PASSED STUDENTS ===")
print(passed[['Name', 'Marks', 'Grade']])

print("\n=== FAILED STUDENTS ===")
print(failed[['Name', 'Marks', 'Grade']])

print("\nPass Rate:", round(len(passed)/len(df)*100, 1), "%")

print("\n=== AVERAGE MARKS BY SUBJECT ===")

subject_avg = df.groupby("Subject")['Marks'].mean()
print(subject_avg)

print("\n===  STUDENTS BY MARKS DESCENDING ===")
print(df.sort_values("Marks", ascending=False))

print("\n=== GRADE A STUDENT ONLY ===")
print(df[df["Grade"] == "a"])


