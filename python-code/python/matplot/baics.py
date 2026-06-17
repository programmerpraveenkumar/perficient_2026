# pip show matplotlib
import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5] 
y = [2, 4, 1, 8, 7] # X-axis values
plt.plot(x, y, color='blue', marker='o', linestyle='--',
linewidth=2, markersize=6)
# Add title and labels
plt.title("Simple Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
# Show grid
plt.grid(True)
# Display the plot
plt.show()