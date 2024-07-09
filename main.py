import redis

class Leaderboard:
    def __init__(self, host='localhost', port=6379):
        self.r = redis.Redis(host=host, port=port)

    def agregar_puntuacion(self, jugador, puntaje):
        self.r.zadd('leaderboard', {jugador: puntaje})

    def mostrar_leaderboard(self):
        leaderboard = self.r.zrevrange('leaderboard', 0, -1, withscores=True)
        return leaderboard

    def mostrar_jugador_ranking(self, nombre):
        rank = self.r.zrevrank('leaderboard', 0)
        return rank + 1 if rank is not None else None

lb = Leaderboard()

lb.agregar_puntuacion('jugador1', 100)
lb.agregar_puntuacion('jugador2', 200)
lb.agregar_puntuacion('jugador3', 150)

leaderboard = lb.mostrar_leaderboard()
for jugador, puntuacion in leaderboard:
    print(f'{jugador.decode("utf-8")}: {puntuacion}')

rank = lb.mostrar_jugador_ranking('jugador1')
print("Ranking de jugadores:" + str(rank))