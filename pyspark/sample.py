from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Customer Demo") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv(
    "customers-100.csv",
    header=True
)
df.cache()

df.select("Country").distinct().show()
df.groupBy("Country").count().show()

df.filter(df.Country == "Sri Lanka").select("First Name").show()

sg_customers_df = df.filter(
    df["Country"] == "Singapore"
).select(
    "First Name",
    "Last Name",
    "Email"
)

sg_customers_df.show()
sg_customers_df.count()

# Write to CSV
sg_customers_df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("output/employees_filtered")

df = spark.read.parquet("sales.parquet")

# df.show()
sg_customers_df.write.parquet("students_parquet")
