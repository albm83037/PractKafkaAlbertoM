import json, kafka
from transformers import pipeline


from kafka import KafkaConsumer
from transformers import pipeline
#sentiment_pipeline = pipeline("sentiment-analysis")
sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
#data = ["I love you", "I hate you"]
#sentiment_pipeline(data)

consumer = KafkaConsumer('tweets',
                         group_id='py-group',
                         bootstrap_servers=['127.0.0.1:9092'],
                         auto_offset_reset='earliest')
consumer.subscribe(["tweets"])

for message in consumer:
  # message value and key are raw bytes -- decode if necessary!
  # e.g., for unicode: `message.value.decode('utf-8')`
  print(message.topic, message.partition,
                                       message.offset,
                                       message.value.decode('utf8'),
                                       sentiment_pipeline([message.value.decode('utf8')]))

