import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_list

spark = SparkSession.builder.config( "spark.jars", "/Users/praveen/Downloads/postgresql-42.7.11.jar")\
      .appName("Customer Demo") .master("local[*]") .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option(
        "url",
        "jdbc:postgresql://localhost:5432/perficient_training"
    ) \
    .option(
        "dbtable",
        "sample_schema.users"
    ) \
    .option("user", "postgres") \
    .option("password", "roottoor") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.groupBy("department").agg(collect_list("user_name").alias("users")).show()

# df.show()