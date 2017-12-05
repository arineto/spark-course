from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('WordCount')
sc = SparkContext(conf=conf)

text_input = sc.textFile(
    '/Users/arimateaneto/Workspace/spark-course/word_count/book.txt'
)
words = text_input.flatMap(lambda x: x.split())
wordCounts = words.countByValue()

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if (cleanWord):
        print(cleanWord.decode() + ' ' + str(count))
