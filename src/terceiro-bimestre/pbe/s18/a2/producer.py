# docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
# pip install pika

import pika

# Conecta ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara uma fila (cria se ela não existir)
channel.queue_declare(queue='hello')

# Publica a mensagem na fila 'hello'
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Olá, RabbitMQ!')

print(" [x] Mensagem enviada: 'Olá, RabbitMQ!'")

# Fecha a conexão
connection.close()

