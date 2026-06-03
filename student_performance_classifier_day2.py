import numpy as np
marks = np.array([60, 65, 41, 42, 53, 50, 49, 80, 90, 76, 61])
marks >= 50
marks[marks >= 50]
passed = marks[marks >= 50]
failed = marks[marks < 50]
excellent = marks[marks >= 80]
good = marks[(marks >=60) & (marks < 70)]
poor = marks[(marks < 60) & (marks >= 50)]
print("passed: ", passed )
print("failed: ", failed )
print("excellent: ", excellent)
print("poor: ", poor)
print("good: ", good)