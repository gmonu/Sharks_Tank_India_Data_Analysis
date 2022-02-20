from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .getOrCreate()
context = spark.sparkContext

# Data Loading into dataframe
data = "ShartankIndiaAllPitches.csv"
df1 = spark.read.format("csv").option("header", "true").load(data)

# Making a table using dataset for querying on that table
df1.createOrReplaceTempView("sharksdetails")
column_names = spark.sql("DESCRIBE sharksdetails")
column_names.show()

# column counts
print("Total columns = ", column_names.count())

# printing all values in particular column
for col in column_names.collect():
    col_names = col['col_name']
    h = spark.sql(f"Select {col_names} from sharksdetails")
    h.show()

