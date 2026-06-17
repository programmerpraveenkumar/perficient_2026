import pandas as pd
df = pd.read_csv('../customers-100.csv')
print(df.head())#first 5 
print(df.head(20))#first 20 
print(df.tail())#last 5 
print(df.shape) # Dimensions
print(df.columns) # Column names
print(df.info()) # Data types & nulls
print(df.describe())