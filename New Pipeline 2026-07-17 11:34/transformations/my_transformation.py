from pyspark import pipelines as dp

@dp.table
def customers():

    raise Exception("Demo Failure - Customer file missing")

    return spark.range(10)