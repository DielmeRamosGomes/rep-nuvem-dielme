import pika

# Conecta ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara a fila novamente (segurança)
channel.queue_declare(queue='hello')

# Define a função que será chamada quando uma mensagem for recebida
def callback(ch, method, properties, body):
    print(f" [x] Mensagem recebida: {body.decode()}")

# Inicia o consumo da fila 'hello'
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')
channel.start_consuming()
