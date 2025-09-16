import time
from celery_app import app

# O decorator '@app.task' registra a função como uma tarefa do Celery.
@app.task
def enviar_mensagem(destinatario, mensagem):
    print(f"Iniciando o envio de mensagem para {destinatario}...")
    # Simula um processamento demorado
    time.sleep(5)
    print(f"Mensagem '{mensagem}' enviada com sucesso para {destinatario}!")
    return f"Mensagem para {destinatario} concluída."




