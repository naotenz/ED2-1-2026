import random

class Player:
    def __init__(self, nombre, vida, ataque, defensa, velocidad):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad

    def recibir_dano(self, dano):
        self.vida -= dano


class Enemy:
    def __init__(self, vida, ataque, defensa, velocidad):
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.tipo = self.asignar_tipo()

    def asignar_tipo(self):
        if self.vida <= 100:
            return "Lobo"
        elif self.vida <= 500:
            return "Oso"
        elif self.vida <= 3000:
            return "Gigante"
        elif self.vida <= 5000:
            return "Dragon"
        else:
            return "Dios"

    def recibir_dano(self, dano):
        self.vida -= dano


# ⚔️ COMBATE COMPLETO
def combate(jugador, enemigo):

    log = ""

    # ⚡ quien empieza (velocidad)
    if jugador.velocidad > enemigo.velocidad:
        turno = "jugador"
    elif enemigo.velocidad > jugador.velocidad:
        turno = "enemigo"
    else:
        turno = random.choice(["jugador", "enemigo"])

    log += f"Empieza: {turno}\n\n"

    while True:

        # ===== TURNO JUGADOR =====
        if turno == "jugador":

            if jugador.vida <= 0:
                log += f"{jugador.nombre} ha sido derrotado\n"
                return "derrota", log

            # 🏃 intento de huida
            if jugador.vida <= jugador.vida_max * 0.1 or random.randint(1, 100) <= 20:
                if random.randint(1, 100) <= 50:
                    log += f"{jugador.nombre} escapó del combate\n"
                    return "huida", log
                else:
                    log += f"{jugador.nombre} intentó huir pero falló\n"

            # ⚔️ ataque
            dano = max(jugador.ataque - enemigo.defensa, 0)
            enemigo.recibir_dano(dano)

            log += f"{jugador.nombre} ataca (-{dano})\n"

            if enemigo.vida <= 0:
                log += f"{enemigo.tipo} ha sido derrotado\n"
                return "victoria", log

            turno = "enemigo"

        # ===== TURNO ENEMIGO =====
        else:

            if enemigo.vida <= 0:
                log += f"{enemigo.tipo} ha sido derrotado\n"
                return "victoria", log

            # 🏃 huida enemigo
            if enemigo.vida <= enemigo.vida_max * 0.1 or random.randint(1, 100) <= 20:
                if random.randint(1, 100) <= 50:
                    log += f"{enemigo.tipo} ha huido\n"
                    return "enemigo huyo", log
                else:
                    log += f"{enemigo.tipo} intentó huir pero falló\n"

            # ⚔️ ataque
            dano = max(enemigo.ataque - jugador.defensa, 0)
            jugador.recibir_dano(dano)

            log += f"{enemigo.tipo} ataca (-{dano})\n"

            if jugador.vida <= 0:
                log += f"{jugador.nombre} ha sido derrotado\n"
                return "derrota", log

            turno = "jugador"