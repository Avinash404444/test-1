import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
categories = ["A", "B", "C", "D"]
values = [25, 30, 20, 25]

# 1. Line plot
plt.figure()
plt.plot(x, y, marker="o")
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
# 2. Bar chart
plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
# 3. Scatter plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
# 4. Histogram
plt.figure()
plt.hist(y, bins=5, edgecolor="black")
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# 5. Pie chart
plt.figure()
plt.pie(values, labels=categories, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()