import redis
import threading

def escuchar_por_mensajes(pubsub):
    for mensaje in pubsub.listen():
        if mensaje['type'] == 'message':
            print("Recibido - 2: " + mensaje['data'].decode())

r = redis.Redis(host='localhost', port=6379, db=0)

pubsub = r.pubsub()

pubsub.subscribe('chat')

threading.Thread(target=escuchar_por_mensajes, args=(pubsub,)).start()