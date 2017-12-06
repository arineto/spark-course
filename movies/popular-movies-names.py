from pyspark import SparkConf, SparkContext
import io


def load_movie_names():
    movies = {}
    with io.open('movies/ml-100k/movies_names.csv', 'r') as csv_file:
        for row in csv_file:
            data = row.split(',')
            movie_id = int(data[0])
            movie_name = data[1]
            movies[movie_id] = movie_name
    return movies


def parse_data(row):
    movie_id = int(row.split()[1])
    return (movie_id, 1)


conf = SparkConf().setMaster('local').setAppName('PopularMovies')
sc = SparkContext(conf=conf)
sc.setLogLevel('ERROR')

movies_names = sc.broadcast(load_movie_names())

lines = sc.textFile('movies/ml-100k/u.data')
movies_count = lines.map(parse_data).reduceByKey(lambda c1, c2: c1 + c2)
sorted_movies = movies_count.map(lambda row: (row[1], row[0])).sortByKey()

sorted_movies_names = sorted_movies.map(
    lambda row: (movies_names.value[row[1]], row[0])
)

for count, movie_name in sorted_movies_names.collect():
    print('{}\t{}'.format(movie_name, count))
