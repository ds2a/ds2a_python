from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CSV Example").getOrCreate()
# Reading from a CSV file
df = spark.read.csv("output.csv", header=True, inferSchema=True)
df.show()

# Writing to a CSV file
df.write.csv("output_1.csv", header=True)

