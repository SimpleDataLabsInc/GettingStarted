from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from benchmarkinpyspark.config.ConfigStore import *
from benchmarkinpyspark.udfs.UDFs import *
from prophecy.utils import *
from benchmarkinpyspark.graph import *

def pipeline(spark: SparkSession) -> None:
    df_TPCH_SF1_LINEITEM = TPCH_SF1_LINEITEM(spark)
    df_Cleanup = Cleanup(spark, df_TPCH_SF1_LINEITEM)
    df_Aggregate_1 = Aggregate_1(spark, df_Cleanup)
    df_OrderBy_1 = OrderBy_1(spark, df_Aggregate_1)
    lineitem_agg_groupby(spark, df_OrderBy_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "3736/pipelines/BenchmarkInPySpark")
    MetricsCollector.start(spark = spark, pipelineId = "3736/pipelines/BenchmarkInPySpark")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
