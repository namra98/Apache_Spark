from pyspark import SparkContext, SparkConf


conf = SparkConf().setAppName("first")
sc = SparkContext(conf=conf)
contentRDD = sc.textFile("../in/word_count.text")


nonempty_lines = contentRDD.filter(lambda x: len(x) > 0)
words = nonempty_lines.flatMap(lambda x: x.split(" "))
wordcount = words.map(lambda x: (xpy, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .map(lambda x: (x[1], x[0])).sortByKey(False)


for word in wordcount.collect():
    print(word)

wordcount.saveAsTextFile("output")
