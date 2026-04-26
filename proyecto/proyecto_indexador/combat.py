import random

def combate(jugador, enemigo):
    while jugador.vida > 0 and enemigo.vida > 0:
        # Ataque del jugador
        dano_jugador = jugador.ataque - enemigo.defensa
        if dano_jugador < 0:
            dano_jugador = 0  # Si la defensa es mayor que el ataque, no hace daño
        enemigo.vida -= dano_jugador
        print(f"{jugador.nombre} atacó a {enemigo.tipo}. {enemigo.tipo} perdió {dano_jugador} de vida.")

        # Verificar si el enemigo murió
        if enemigo.vida <= 0:
            print(f"{enemigo.tipo} ha sido derrotado.")
            return "victoria", jugador, enemigo

        # Ataque del enemigo
        dano_enemigo = enemigo.ataque - jugador.defensa
        if dano_enemigo < 0:
            dano_enemigo = 0
        jugador.vida -= dano_enemigo
        print(f"{enemigo.tipo} atacó a {jugador.nombre}. {jugador.nombre} perdió {dano_enemigo} de vida.")

        # Verificar si el jugador murió
        if jugador.vida <= 0:
            print(f"{jugador.nombre} ha sido derrotado.")
            return "derrota", jugador, enemigo

    return "en combate", jugador, enemigo