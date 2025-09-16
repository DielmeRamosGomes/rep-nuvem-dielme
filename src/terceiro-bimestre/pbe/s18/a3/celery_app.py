# docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management
# pip install "celery[librabbitmq]"

from celery import Celery
from celery.schedules import crontab

# A URL para o RabbitMQ é 'amqp://'.
# Se você estiver usando as credenciais e o host padrão (guest@localhost),
# a URL é simples: 'amqp://guest:guest@localhost:5672//'
app = Celery(
    'meu_programa',
    broker='amqp://guest:guest@localhost:5672//',
    backend='rpc://', # backend='rpc://': Este backend é recomendado para produção com RabbitMQ, pois ele usa uma fila temporária para enviar o resultado da tarefa de volta ao cliente.
    include=['tasks']
)

app.conf.timezone = 'America/Sao_Paulo'

# Adicionando o agendamento
app.conf.beat_schedule = {
    'enviar-mensagem-a-cada-minuto': {
        'task': 'tasks.enviar_mensagem',
        'schedule': crontab(minute='*'),  # Roda a cada minuto
        'args': ('usuário_automatico_rabbit', 'Olá, esta é uma mensagem automática com RabbitMQ!')
    },
}

# terminal 1
# Este comando iniciará o worker do Celery.
# celery -A celery_app worker --loglevel=info

# terminal 2
# Este comando iniciará o agendador.
# celery -A celery_app beat

# conferir o status das filas e das mensagens no painel de gerenciamento do RabbitMQ 
# http://localhost:15672/