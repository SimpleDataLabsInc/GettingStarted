from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from benchmarkinpyspark.config.ConfigStore import *
from benchmarkinpyspark.udfs.UDFs import *

def Cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("L_ORDERKEY"), 
        col("L_PARTKEY"), 
        col("L_SUPPKEY"), 
        col("L_LINENUMBER"), 
        col("L_QUANTITY"), 
        col("L_EXTENDEDPRICE"), 
        col("L_DISCOUNT"), 
        expr("if(isnull(L_TAX), '0.02', L_TAX)").alias("L_TAX"), 
        col("L_RETURNFLAG"), 
        col("L_LINESTATUS"), 
        col("L_SHIPDATE"), 
        col("L_COMMITDATE"), 
        col("L_RECEIPTDATE"), 
        col("L_SHIPINSTRUCT"), 
        col("L_SHIPMODE"), 
        col("L_COMMENT"), 
        when(((col("L_DISCOUNT") > lit(60)) | col("L_RETURNFLAG").eqNullSafe(lit(True))), lit("true"))\
          .otherwise(lit("false"))\
          .alias("L_CLEARANCE")
    )
