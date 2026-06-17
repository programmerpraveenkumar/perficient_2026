import pandas as pd
# df = pd.read_csv('sample.csv')
df = pd.read_csv('../customers-100.csv')
# print(df[['Series_reference','Data_value']])
filter = df[(df['Index']<10) & 
            df['Website'].str.startswith('https')]
# filter = df[(df['Data_value']<100)]
# filter = df[(df['Data_value'] == 65.087)]
print(filter)
#  print(df[['Series_reference','Data_value']])

# Drop Rows with Nulls
# Remove rows containing any null value:
df.dropna()
# Replace nulls with a fixed value:
df.fillna('Unknown')