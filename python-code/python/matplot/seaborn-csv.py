import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('tips.csv')# # Load the CSV file

# Create a scatter plot of Age vs Score
plt.figure(figsize=(8, 6)) # Optional: Adjust figure size
sns.scatterplot(x='day', y='total_bill', data=df)
sns.jointplot(data=df, x="total_bill", y="tip", kind="kde", fill=True)
sns.rugplot(data=df["total_bill"], color="red")
plt.xlabel('Day') # Optional: Add x-axis label
plt.ylabel('Total Bill') # Optional: Add y-axis label
plt.grid(True) # Optional: Add a grid
##save the plot as png file.this file can be used in frontend.
# plt.savefig("seaborn_plot.png")
# Display the plot
plt.show()

