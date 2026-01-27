# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations
# It provides an API that is object-oriented for embedding plots into applications
# using general GUI kits like TKinter, wxPython, Qt, or GTK

import matplotlib.pyplot as plt

# sample data
x, y = [1, 2, 4, 6, 8], [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y, marker = 'o', linestyle = '-', color = 'b', label = 'Line 1')
plt.title("My Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# Create a Bar Chart
categories, values = ["Fruits", "Vegetables", "Meat", "Dairy"], [8, 11, 4, 6]

plt.bar(categories, values, color = 'g')
plt.title("Food in My Pantry")
plt.xlabel("Food Categories")
plt.ylabel("Number of Items")
plt.show()

# Create a scatterplot
x_scatter, y_scatter = [9, 81, 43, 66, 12, 9], [100, 5, 45, 25, 49, 8]

plt.scatter(x_scatter, y_scatter, color = 'r')
plt.title("My Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()