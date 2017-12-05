from pyspark import SparkConf, SparkContext

BASE_PATH = '/Users/arimateaneto/Workspace/spark-course/'

conf = SparkConf().setMaster('local').setAppName('Assignment1')
sc = SparkContext(conf=conf)


def parseLine(line):
    fields = line.split(',')
    customer_id = int(fields[0])
    amount_spent = float(fields[2])
    return (customer_id, amount_spent)


lines = sc.textFile('{}assignment1/customer-orders.csv'.format(BASE_PATH))

customer_expenses = lines.map(parseLine).reduceByKey(lambda v1, v2: v1 + v2)
sorted_expenses = customer_expenses.map(lambda x: (x[1], x[0])).sortByKey()

for value, c_id in sorted_expenses.collect():
    print('{0}\t{1:0.2f}'.format(c_id, value))
