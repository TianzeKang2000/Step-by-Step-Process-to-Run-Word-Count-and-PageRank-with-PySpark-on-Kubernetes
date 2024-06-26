from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read input file from GCS
input_path = "gs://your-bucket-name/input/local-file.txt"
df = spark.read.text(input_path)

# Perform word count
words = df.select(explode(split(col("value"), "\s+")).alias("word"))
word_counts = words.groupBy("word").count()

# Save results to GCS
output_path = "gs://your-bucket-name/output/"
word_counts.write.mode("overwrite").csv(output_path)

spark.stop()
