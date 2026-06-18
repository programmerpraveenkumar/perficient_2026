from pyspark.sql.functions import concat, lit
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Customer Demo") \
    .master("local[*]") \
    .getOrCreate()

df = spark.range(100)

df = df.withColumn(
    "FirstName",
    concat(lit("Customer_"), df.id)
)

df = df.withColumn(
    "Email",
    concat(lit("user"), df.id, lit("@gmail.com"))
)

df.show(5, False)

df.coalesce(1) .write .mode("overwrite") .option("header", True) .csv("customers")