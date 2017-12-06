from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('PopularMovies')
sc = SparkContext(conf=conf)
sc.setLogLevel('ERROR')


def parse_data(row):
    movie_id = int(row.split()[1])
    return (movie_id, 1)


lines = sc.textFile(
    '/home/arimateaneto/Workspace/spark-course/movies/ml-100k/u.data'
)

movies_count = lines.map(parse_data).reduceByKey(lambda c1, c2: c1 + c2)
sorted_movies = movies_count.map(lambda row: (row[1], row[0])).sortByKey()

for count, movie_id in sorted_movies.collect():
    print('{}\t{}'.format(movie_id, count))
