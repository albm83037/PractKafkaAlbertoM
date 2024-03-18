import logging, kafka

from kafka import KafkaProducer

log = logging.getLogger(__name__)

# Funcion para el caso de exito en la produccion del metodo
def on_send_success(record_metadata):
  print(record_metadata.topic)
  print(record_metadata.partition)
  print(record_metadata.offset)

# que haremos en caso de error
def on_send_error(ex):
  log.error('I am an Error', exc_info=ex)
  # handle exception

# Configura el productor
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')

# Lee los datos del archivo
with open('frases.txt', 'r') as file:
    for line in file:
        # Envía cada línea al tópico "tweets"
        producer.send('tweets', value=line.encode('utf-8'))

# Cierra la conexión del productor
producer.close()