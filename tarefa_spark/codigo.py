

# // import os
# // import sys

# // os.environ["PYSPARK_PYTHON"] = sys.executable

# // import pyspark
# // from pyspark.sql import SparkSession
# // spark = SparkSession.builder.master("local[*]") \
# //  .appName('contadorPalabras') \
# //  .getOrCreate()
# // sc = spark.sparkContext



texto_cont = sc.textFile("README.md")

contagem = texto_cont.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)

resultado = contagem.collect() for (word, count) in resultado: print("%s: %i" % (word, count))