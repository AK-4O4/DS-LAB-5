import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Female", "Female"],
    "StudyHours": [2, 6, 3, 7, 1, 8, 4, 5, 3, 9, 6, 6],
    "Attendance(%)": [70, 92, 78, 95, 65, 98, 80, 88, 75, 96, 90, 90],
    "Marks": [55, 78, np.nan, 85, 45, 90, 65, 72, np.nan, 94, 80, 80]
}
pd.DataFrame(data).to_csv("student_performance.csv", index=False)

# TASK A
df = pd.read_csv("student_performance.csv")
print("Shape:", df.shape)
print(df.info())

# TASK B
print("Missing values per column:")
print(df.isnull().sum())
print("Missing values in Marks:", df["Marks"].isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

df_clean = df.drop_duplicates().copy()
median_marks = df_clean["Marks"].median()
df_clean["Marks"] = df_clean["Marks"].fillna(median_marks)
print("Median of Marks used for filling:", median_marks)
print("After cleaning:", df_clean.shape)
print("Missing values left in Marks:", df_clean["Marks"].isnull().sum())

# TASK C
plt.figure(figsize=(5, 4))
plt.hist(df_clean["Marks"], bins=6, color="steelblue")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.tight_layout()
plt.savefig("marks_histogram.png")

plt.figure(figsize=(4, 4))
plt.boxplot(df_clean["Marks"])
plt.ylabel("Marks")
plt.title("Marks Boxplot")
plt.tight_layout()
plt.savefig("marks_boxplot.png")

# TASK D
plt.figure(figsize=(5, 4))
plt.scatter(df_clean["StudyHours"], df_clean["Marks"], color="darkorange")
plt.xlabel("StudyHours")
plt.ylabel("Marks")
plt.title("StudyHours vs. Marks")
plt.tight_layout()
plt.savefig("studyhours_vs_marks.png")

corr_matrix = df_clean[["StudyHours", "Attendance(%)", "Marks"]].corr()
print("Correlation matrix:")
print(corr_matrix)

# TASK E
gender_summary = df_clean.groupby("Gender")[["Marks", "Attendance(%)"]].mean()
print("Average Marks and Attendance by Gender:")
print(gender_summary)

print("Saved marks_histogram.png, marks_boxplot.png, studyhours_vs_marks.png")