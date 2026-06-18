from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("DAG Demo") \
    .getOrCreate()

# create numbers from 0 to 10000000
df = spark.range(10000000)

result = df.filter(df.id % 2 == 0)

print(result.count())

input("Press Enter to Exit...")