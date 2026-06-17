import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a dummy CSV file for demonstration (replace with your actual file)
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 92, 78, 95]}
# dummy_df = pd.DataFrame(data)
# dummy_df.to_csv('sample_data.csv', index=False)

# # Load the CSV file
# df = pd.read_csv('tips.csv')

# Create a scatter plot of Age vs Score
plt.figure(figsize=(8, 6)) # Optional: Adjust figure size
sns.scatterplot(x='Name', y='Score', data=data)
# sns.rugplot(data=df["total_bill"], color="red")

plt.title('Age vs Score from CSV') # Optional: Add a title
plt.xlabel('Age (Years)') # Optional: Add x-axis label
plt.ylabel('Score') # Optional: Add y-axis label
plt.grid(True) # Optional: Add a grid
# Display the plot
plt.show()