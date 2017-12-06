from pyspark import SparkConf, SparkContext


def load_names():
    names = {}
    with open('super_heros/Marvel-Names.csv') as names_file:
        for row in names_file:
            data = row.split(',')
            hero_id = data[0]
            hero_name = data[1].replace('\n', '')
            names[hero_id] = hero_name
    return names


def parse_lines(row):
    data = row.split()
    hero_id = data[0]
    n_friends = len(data[1:])
    return (hero_id, n_friends)


conf = SparkConf().setMaster('local').setAppName('PopularSuperheros')
sc = SparkContext(conf=conf)
sc.setLogLevel('ERROR')

heros_names = sc.broadcast(load_names())

lines = sc.textFile('super_heros/Marvel-Graph.txt')

heros_network = lines.map(parse_lines).reduceByKey(lambda l1, l2: l1 + l2)
heros_count_sorted = heros_network.map(
    lambda row: (row[1], row[0])
).sortByKey()

heros_sorted_names = heros_count_sorted.map(
    lambda row: (heros_names.value[row[1]], row[0])
)

for name, count_friends in heros_sorted_names.collect():
    print('{}\t{}'.format(name, count_friends))
