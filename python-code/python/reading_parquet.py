# import pandas as pd
# df = pd.read_csv("customers-100.csv")

# filter = df[(df['Index']<10)]

# # extract customers whose index is <10 and load in to the parquet

# df.to_parquet("customers.parquet")

import pyarrow.parquet as pq
# reading the parquet file
table = pq.read_table("customers.parquet")
# converting the parquet to pandas
df = table.to_pandas()
filter_data = df[df['Index'] < 10]
print(filter_data)