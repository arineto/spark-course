#!/bin/bash

# job MapReduce / Avaliacao 1
# Arimatea Neto
# Especialização em Ciência de Dados e Analytics

hadoop fs -rm -r /jarn/output/avaliacao1/tfidf/


hadoop jar \
$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
     -file ~/jarn/code/tfidf_map.py \
     -file ~/jarn/code/tfidf_reduce.py \
     -mapper ~/jarn/code/tfidf_map.py \
     -reducer ~/jarn/code/tfidf_reduce.py \
     -input /jarn/output/avaliacao1/df \
     -input /jarn/output/avaliacao1/ntdoc \
     -output /jarn/output/avaliacao1/tfidf 


hadoop fs -text /jarn/output/avaliacao1/tfidf/part* | more
