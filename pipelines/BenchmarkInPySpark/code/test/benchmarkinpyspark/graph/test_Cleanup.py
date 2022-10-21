from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from benchmarkinpyspark.graph.Cleanup import *
import benchmarkinpyspark.config.ConfigStore as ConfigStore


class CleanupTest(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/benchmarkinpyspark/graph/Cleanup/in0/schema.json',
            'test/resources/data/benchmarkinpyspark/graph/Cleanup/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/benchmarkinpyspark/graph/Cleanup/out/schema.json',
            'test/resources/data/benchmarkinpyspark/graph/Cleanup/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = Cleanup(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("L_TAX", "L_CLEARANCE"),
            dfOutComputed.select("L_TAX", "L_CLEARANCE"),
            self.maxUnequalRowsToShow
        )

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        ConfigStore.Utils.initializeFromArgs(
            self.spark,
            Namespace(file = f"configs/resources/config/{fabricName}.json", config = None)
        )
