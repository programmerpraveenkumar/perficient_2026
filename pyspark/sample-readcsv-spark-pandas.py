import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Demo") \
    .master("local[*]") \
    .getOrCreate()

pdf = pd.read_csv("customers-100.csv")

df = spark.createDataFrame(pdf)
df.select("Country").distinct().show()
df.groupBy("Country").count().show()

df.filter(df.Country == "Sri Lanka").select("First Name").show()

india_customers_df = df.filter(
    df["Country"] == "Singapore"
).select(
    "First Name",
    "Last Name",
    "Email"
)

india_customers_df.count()
# print(pdf['Country'])