import seaborn as sns
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# sns.displot([0, 1, 2, 3, 4, 5])

# plt.show()

# tips = sns.load_dataset("tips")
tips = pd.read_csv('tips.csv')
# Create a histogram of the total bill amounts

sns.histplot(data=tips, x="total_bill")
plt.show()