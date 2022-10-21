from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from benchmarkinpyspark.config.ConfigStore import *
from benchmarkinpyspark.udfs.UDFs import *

def dataset2(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder
    in0.write\
        .format("delta")\
        .option("overwriteSchema", True)\
        .mode("overwrite")\
        .save("dbfs:/Prophecy/sparklearner123@gmail.com/dataset2")
