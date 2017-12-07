#!/bin/bash

# job MapReduce / Avaliacao 1
# Arimatea Neto
# Especialização em Ciência de Dados e Analytics


hadoop fs -rm -r /jarn/output/avaliacao1/stopwords/


hadoop jar \
$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
     -file ~/jarn/code/stopwords_map.py \
     -file ~/jarn/code/stopwords_reduce.py \
     -mapper ~/jarn/code/stopwords_map.py \
     -reducer ~/jarn/code/stopwords_reduce.py \
     -input /jarn/output/avaliacao1/tfidf \
     -output /jarn/output/avaliacao1/stopwords 


hadoop fs -text /jarn/output/avaliacao1/stopwords/part* | more
