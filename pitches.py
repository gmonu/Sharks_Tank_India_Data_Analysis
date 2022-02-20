import pandas as pd
from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .getOrCreate()
context = spark.sparkContext

data = "ShartankIndiaAllPitches.csv"
df1 = spark.read.format("csv").option("header", "true").load(data)
df1.createOrReplaceTempView("sharksdetails")
column_names = spark.sql("DESCRIBE sharksdetails")
column_names.show()

# column counts
print("Total columns = ", column_names.count())
print(type(column_names))
# printing total values in particular column
for col in column_names.collect():
    col_names = col['col_name']
    col_values = spark.sql("SELECT '{}' FROM sharksdetails".format(col_names))
    col_values.show()

