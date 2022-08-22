r"""
 Counts words in UTF8 encoded, '\n' delimited text received from the network every second.
 Usage: network_wordcount.py <hostname> <port>
   <hostname> and <port> describe the TCP server that Spark Streaming would connect to receive data.
 To run this on your local machine, you need to first run a Netcat server
    `$ nc -lk 9999`
 and then run the example
    `$ bin/spark-submit examples/src/main/python/streaming/network_wordcount.py localhost 9999`
"""

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: network_wordcount.py", file=sys.stderr)
        sys.exit(-1)
    sc = SparkContext(appName="Kafka Spark Demo")
    ssc = StreamingContext(sc, 60)

    message = KafkaUtils.createDirectStream(ssc, topics=['testtopic'], kafkaParams= {"metadata.broker.list":"localhost:9092"})

    words=message.map(lambda x: x[1]).flatMap(lambda x: x.split(" "))

    counts = words.map(lambda word: (word, 1))\
             .reduceByKey(lambda a, b: a + b)
    counts.pprint()
    words.pprint()
    ssc.start()
    ssc.awaitTermination()
