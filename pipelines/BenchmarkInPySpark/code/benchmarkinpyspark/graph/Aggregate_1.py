from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from benchmarkinpyspark.config.ConfigStore import *
from benchmarkinpyspark.udfs.UDFs import *

def Aggregate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("L_RETURNFLAG"), col("L_LINESTATUS"))

    return df1.agg(
        sum(col("L_QUANTITY")).alias("SUM_QTY"), 
        sum(col("L_EXTENDEDPRICE")).alias("SUM_BASE_PRICE"), 
        sum((col("L_EXTENDEDPRICE") * (lit(1) - col("L_DISCOUNT")))).alias("SUM_DISK_PRICE"), 
        sum(((col("L_EXTENDEDPRICE") * (lit(1) - col("L_DISCOUNT"))) * (lit(1) + col("L_TAX")))).alias("SUM_CHARGE"), 
        avg(col("L_QUANTITY")).alias("AVG_QTY"), 
        avg(col("L_DISCOUNT")).alias("AVG_DISC"), 
        count(lit(1)).alias("COUNT_ORDER")
    )
