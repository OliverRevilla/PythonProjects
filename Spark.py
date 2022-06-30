#Procesamiento de datos en streaming
from pyspark import SparkContext
from pyspark.streaming import  StreamingContext

# Inicializamos el contexto
sc = SparkContext("local[2]","NetworkWordCount")
# El segundo parámetro es para determinar el intervalo de procesamiento de datos
ssc = StreamingContext(sc,10)

# Inicializar el recurso
lines = ssc.socketTextStream("localhost",9090)

# Lógica de procesamiento de datos
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word,1))
wordCounts = pairs.reduceByKey(lambda x,y: x + y)

wordCounts.print()

ssc.start()
ssc.awaitTermination()