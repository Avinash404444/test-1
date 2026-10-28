import pandas as pd
import matplotlib.pyplot as plt
# Sample annual examination marks
data = {
"Mathematics": [78, 85, 90, 67, 88, 76, 92, 81, 73, 95],
"Science": [82, 79, 85, 70, 91, 77, 88, 84, 75, 93],
"English": [74, 80, 83, 69, 86, 72, 89, 78, 75, 91],
"Computer Science": [88, 92, 95, 80, 91, 85, 97, 89, 83, 94]
}
df = pd.DataFrame(data)
# Display the dataset
print("Annual Examination Marks:")
print(df)
# Create boxplot
plt.figure(figsize=(9, 6))
plt.boxplot(df.values, tick_labels=df.columns, patch_artist=True)
plt.title("Comparison of Student Performance by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis="y", alpha=0.3)
plt.show()
# Comparative analysis
print("\nMean Marks in Each Subject:")
print(df.mean().round(2))
print("\nMedian Marks in Each Subject:")
print(df.median())