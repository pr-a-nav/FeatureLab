from pyspark import SparkConf, SparkFiles
from pyspark.sql.functions import col
import pyspark



class pysparks:

    def __init__(self) -> None:
        pass
    
    def operation(self , file):
        SparkFiles.read(file)