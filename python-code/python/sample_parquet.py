import pandas as pd
df = pd.read_csv("customers-100.csv")

filter = df[(df['Index']<10)]

# extract customers whose index is <10 and load in to the parquet

df.to_parquet("customers.parquet")

import pyarrow.parquet as pq
table = pq.read_table("employees.parquet")
df = table.to_pandas()
print(df)