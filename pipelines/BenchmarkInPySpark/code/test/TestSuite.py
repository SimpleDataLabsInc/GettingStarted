import unittest

from test.benchmarkinpyspark.graph.test_Cleanup import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
