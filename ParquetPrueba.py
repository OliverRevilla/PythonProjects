#Libraries 
import findspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType,DecimalType
from pyspark.sql.functions import col,coalesce,filter

# Creating the spark session
# findspark.init()
findspark.init()
from pyspark.sql import SparkSession

# Shuffle: Partitions which help us to improve the time of the proccesing
conf = SparkConf().setMaster("local").setAppName("Ratings")
#spark = SparkSession.builder.getOrCreate(SparkConf)
SparkSession.builder.appName("MySession")
SparkSession.builder.getOrCreate()


