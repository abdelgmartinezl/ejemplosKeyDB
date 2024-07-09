import redis
import threading
import time

def publicar_mensajes(pubsub, mensaje):
    pubsub.publish('chat', mensaje)

def escuchar_por_mensajes(pubsub):
    for mensaje in pubsub.listen():
        if mensaje['type'] == 'message':
            print("Recibido: " + mensaje['data'].decode())

r = redis.Redis(host='localhost', port=6379, db=0)

pubsub = r.pubsub()

pubsub.subscribe('chat')

threading.Thread(target=escuchar_por_mensajes, args=(pubsub,)).start()

#publicar_mensajes(r, 'Hello, Panama!')
for i in range(5):
    threading.Thread(target=publicar_mensajes, args=(r, f'Hola, Panama! Desde el hilo {i+1}')).start()
    time.sleep(1)