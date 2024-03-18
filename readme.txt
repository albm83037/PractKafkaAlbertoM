README 

Profesor : Sergio.khayyat@gmail.com


Tengo un fichero .yml llamado docker-compose.yml y para cargar el entorno Docker, nos posicinamos en el directorio y lo lanzamos de la siguiente manera:

>Docker compose up -d

Tengo instalado python la siguiente versión:
Versión de python 3.10.4


pip install kafka-python
pip isntall transformers
pip install torch


Primero creamos el topic, para hacerlo podemos o bien ejecutar :

kafka-topics --bootstrap-server kafka1:19092 --create --topic tweets --partitions 1 --replication-factor 1

Después nos posicionamos en el directorio de la práctica donde estan los códigos de python y lanzamos el consumer:

>python .\consumer1.py

>python .\consumer2.py

>python .\consumer1OtroGrupo.py

El siguiente paso es lanzar el producer. Para hacerlo:

>python .\producer.py

