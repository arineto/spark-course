#!/bin/bash

# job MapReduce / Avaliacao 1
# Arimatea Neto
# Especialização em Ciência de Dados e Analytics

hadoop fs -rm -r /jarn/output/avaliacao1/ntdoc/

hadoop jar \
$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
     -file ~/jarn/code/ntdoc_map.py \
     -file ~/jarn/code/ntdoc_reduce.py \
     -mapper ~/jarn/code/ntdoc_map.py \
     -reducer ~/jarn/code/ntdoc_reduce.py \
     -input /jarn/input/avaliacao1 \
     -output /jarn/output/avaliacao1/ntdoc

hadoop fs -text /jarn/output/avaliacao1/ntdoc/part* | more
