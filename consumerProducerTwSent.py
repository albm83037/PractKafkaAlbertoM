import json, kafka
from transformers import pipeline
from kafka import KafkaConsumer, KafkaProducer

sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")


def delivery_report(err, msg):
    if err is not None:
        print(f'Error al enviar mensaje: {err}')
    else:
        print(f'Mensaje enviado a {msg.topic()} [{msg.partition()}]')

consumer = KafkaConsumer('tweets',
                         group_id='py-sent',
                         bootstrap_servers=['127.0.0.1:9092'],
                         auto_offset_reset='earliest')
consumer.subscribe(["tweets"])
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
topic = 'tweets_sent'
for message in consumer:
 
  print(message.topic, message.partition,
                                       message.offset,
                                       message.value.decode('utf8'),
                                       sentiment_pipeline([message.value.decode('utf8')]))
  # Creamos un diccionario con los campos que vamso a usar
  result = {
        'partition': message.partition,
        'offset': message.offset,
        'text': message.value.decode('utf8'),
        'sentiment_label': sentiment_pipeline([message.value.decode('utf8')])[0]['label'],      
        'sentiment_score': sentiment_pipeline([message.value.decode('utf8')])[0]['score']      

    }
  # Convertimos el diccionario a una cadena JSON
  result_json = json.dumps(result)
  # Enviamos un mensaje al topic
  producer.send(topic, value=result_json.encode('utf-8'))
  
producer.close()

