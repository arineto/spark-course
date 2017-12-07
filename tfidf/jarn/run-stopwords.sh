#!/bin/bash

# job MapReduce / Avaliacao 1
# Arimatea Neto
# Especialização em Ciência de Dados e Analytics


hadoop fs -rm -r /jarn/output/avaliacao1/tf/
hadoop fs -rm -r /jarn/output/avaliacao1/df/
hadoop fs -rm -r /jarn/output/avaliacao1/ntdoc/
hadoop fs -rm -r /jarn/output/avaliacao1/tfidf/
hadoop fs -rm -r /jarn/output/avaliacao1/stopwords/


hadoop jar \
 	$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
	 -file ~/jarn/code/tf_map.py \
	 -file ~/jarn/code/tf_reduce.py \
	 -mapper ~/jarn/code/tf_map.py \
	 -reducer ~/jarn/code/tf_reduce.py \
	 -input /jarn/input/avaliacao1 \
	 -output /jarn/output/avaliacao1/tf


hadoop jar \
     $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
     -file ~/jarn/code/df_map.py \
     -file ~/jarn/code/df_reduce.py \
     -mapper ~/jarn/code/df_map.py \
     -reducer ~/jarn/code/df_reduce.py \
     -input /jarn/output/avaliacao1/tf \
     -output /jarn/output/avaliacao1/df


hadoop jar \
$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
     -file ~/jarn/code/ntdoc_map.py \
     -file ~/jarn/code/ntdoc_reduce.py \
     -mapper ~/jarn/code/ntdoc_map.py \
     -reducer ~/jarn/code/ntdoc_reduce.py \
     -input /jarn/input/avaliacao1 \
     -output /jarn/output/avaliacao1/ntdoc


hadoop jar \
$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
     -file ~/jarn/code/tfidf_map.py \
     -file ~/jarn/code/tfidf_reduce.py \
     -mapper ~/jarn/code/tfidf_map.py \
     -reducer ~/jarn/code/tfidf_reduce.py \
     -input /jarn/output/avaliacao1/df \
     -input /jarn/output/avaliacao1/ntdoc \
     -output /jarn/output/avaliacao1/tfidf 


hadoop jar \
$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
     -file ~/jarn/code/stopwords_map.py \
     -file ~/jarn/code/stopwords_reduce.py \
     -mapper ~/jarn/code/stopwords_map.py \
     -reducer ~/jarn/code/stopwords_reduce.py \
     -input /jarn/output/avaliacao1/tfidf \
     -output /jarn/output/avaliacao1/stopwords 


hadoop fs -text /jarn/output/avaliacao1/stopwords/part* | more
