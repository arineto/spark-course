from pyspark import SparkConf, SparkContext
import math


DATA_PATH = 'tfidf/jarn/input'


conf = SparkConf().setMaster('local').setAppName('Stopwords')
sc = SparkContext(conf=conf)


def clean_data(row):
    file_name = row[0]
    word = ''.join(filter(str.isalpha, row[1])).lower()
    return (word, file_name)


def reducer_sum(x1, x2):
    return x1 + x2


def mapper_tfidf(row):
    termo = row[0]
    doc_id = row[1]
    f = float(row[2])
    tD = float(row[3])
    tpd = float(row[4])
    D = float(row[5])

    tf = f/tpd
    idf = math.log((D + 1) / (tD + 1), 10)
    tfidf = tf * idf

    return (termo, tfidf, doc_id)


def filter_tfidf(row):
    return (row[0], min(list(row[1])))


def get_cleaned_data():
    # Output: (termo, doc_id)
    data = sc.wholeTextFiles(DATA_PATH)
    splitted_data = data.flatMapValues(lambda text: text.split())
    cleaned_data = splitted_data.map(clean_data).filter(
        lambda row: len(row[0]) >= 2
    )
    return cleaned_data


def calculate_ntdoc(data):
    # Output: (doc_id, tpd, D)
    count_words = data.map(lambda row: (row[1], 1)).reduceByKey(reducer_sum)
    files_number = count_words.count()
    ntdoc = count_words.map(lambda row: (row[0], row[1], files_number))
    return ntdoc


def calculate_tf(data):
    # Output: (termo, doc_id, f)
    count_words = data.map(
        lambda row: ((row[0], row[1]), 1)
    ).reduceByKey(reducer_sum)
    tf = count_words.map(lambda row: (row[0][0], row[0][1], row[1]))
    return tf


def calculate_df(tf):
    # Output: (termo, doc_id, f, tD)
    words_by_file = tf.map(lambda row: (row[0], row[1])).distinct()
    word_count = words_by_file.map(
        lambda row: (row[0], (1))
    ).reduceByKey(reducer_sum)

    mapped_data = tf.map(lambda row: (row[0], (row[1], row[2])))

    df = mapped_data.join(word_count)

    mapped_df = df.map(
        lambda row: (row[0], row[1][0][0], row[1][0][1], row[1][1])
    )
    return mapped_df


def calculate_tfidf(df, ntdoc):
    # (termo, tfidf, doc_id)
    mapped_df = df.map(lambda row: (row[1], (row[0], row[2], row[3])))
    mapped_ntdoc = ntdoc.map(lambda row: (row[0], (row[1], row[2])))

    # (termo, doc_id, f, tD, tpd, D)
    tfidf_input = mapped_df.join(mapped_ntdoc).map(
        lambda r: (
            r[1][0][0], r[0], r[1][0][1], r[1][0][2], r[1][1][0], r[1][1][1]
        )
    )

    tfidf = tfidf_input.map(mapper_tfidf)
    return tfidf


def calculate_stopwords(tfidf):
    grouped_tfidf = tfidf.map(lambda r: (r[0], (r[1]))).groupByKey()
    filtered_tfidf = grouped_tfidf.map(filter_tfidf)
    sorted_tfidf = filtered_tfidf.map(lambda r: (r[1], r[0])).sortByKey()
    stopwords = sorted_tfidf.take(30)
    return stopwords


def run():
    data = get_cleaned_data()
    tf = calculate_tf(data)
    df = calculate_df(tf)
    ntdoc = calculate_ntdoc(data)
    tfidf = calculate_tfidf(df, ntdoc)
    stopwords = calculate_stopwords(tfidf)

    for entry in stopwords:
        print('{1:0.6f}\t{0}'.format(entry[1], entry[0]))


run()
