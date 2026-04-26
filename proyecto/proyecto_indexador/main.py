import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


# ===================== CLASES =====================

class Player:
    def __init__(self, nombre, vida, ataque, defensa, velocidad):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad


class Enemy:
    def __init__(self, vida, ataque, defensa, velocidad):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.tipo = self.asignar_tipo()

    def asignar_tipo(self):
        poder = self.vida + self.ataque + self.defensa + self.velocidad

        if poder < 1000:
            return "Slime"
        elif poder < 5000:
            return "Lobo"
        elif poder < 15000:
            return "Oso"
        elif poder < 25000:
            return "Gigante"
        else:
            return "Dios"


# ===================== APP =====================

class GameApp(App):

    def build(self):

        root = BoxLayout(orientation="vertical")

        # ===== INPUTS =====
        self.txt_nombre = TextInput(hint_text="Nombre", multiline=False)
        self.txt_vida = TextInput(hint_text="Vida", multiline=False)
        self.txt_ataque = TextInput(hint_text="Ataque", multiline=False)
        self.txt_defensa = TextInput(hint_text="Defensa", multiline=False)
        self.txt_velocidad = TextInput(hint_text="Velocidad", multiline=False)

        root.add_widget(self.txt_nombre)
        root.add_widget(self.txt_vida)
        root.add_widget(self.txt_ataque)
        root.add_widget(self.txt_defensa)
        root.add_widget(self.txt_velocidad)

        # ===== STATS =====
        stats_layout = BoxLayout(size_hint=(1, 0.2))

        self.label_jugador = Label(text="Jugador")
        self.label_enemigo = Label(text="Enemigo")

        stats_layout.add_widget(self.label_jugador)
        stats_layout.add_widget(self.label_enemigo)

        # ===== LOG SCROLL =====
        self.scroll = ScrollView(size_hint=(1, 0.5))

        self.log_label = Label(
            text="Bienvenido\n",
            size_hint_y=None,
            halign="left",
            valign="top"
        )

        self.log_label.bind(
            width=lambda i, v: setattr(i, 'text_size', (v, None))
        )
        self.log_label.bind(
            texture_size=lambda i, v: setattr(i, 'height', v[1])
        )

        self.scroll.add_widget(self.log_label)

        # ===== BOTONES =====
        botones = BoxLayout(size_hint=(1, 0.2))

        self.btn_atacar = Button(text="Atacar")
        self.btn_huir = Button(text="Huir")
        self.btn_nuevo = Button(text="Nuevo Enemigo")

        self.btn_atacar.bind(on_press=self.atacar)
        self.btn_huir.bind(on_press=self.huir)
        self.btn_nuevo.bind(on_press=self.generar_enemigo)

        botones.add_widget(self.btn_atacar)
        botones.add_widget(self.btn_huir)
        botones.add_widget(self.btn_nuevo)

        # ===== ENSAMBLAR =====
        root.add_widget(stats_layout)
        root.add_widget(self.scroll)
        root.add_widget(botones)

        return root

    # ===================== FUNCIONES =====================

    def generar_enemigo(self, instance):

        try:
            self.jugador = Player(
                self.txt_nombre.text or "Jugador",
                int(self.txt_vida.text),
                int(self.txt_ataque.text),
                int(self.txt_defensa.text),
                int(self.txt_velocidad.text),
            )
        except:
            self.log_label.text += "\n⚠️ Completa todas las stats\n"
            return

        # enemigo random
        self.enemigo = Enemy(
            random.randint(1, 9999),
            random.randint(1, 9999),
            random.randint(1, 9999),
            random.randint(1, 9999),
        )

        self.log_label.text = "⚔️ Nuevo enemigo apareció\n"

        self.actualizar_stats()

    def atacar(self, instance):

        if not hasattr(self, 'enemigo') or not self.enemigo:
            self.log_label.text += "\nPrimero genera enemigo\n"
            return

        # decidir turno por velocidad
        if self.jugador.velocidad >= self.enemigo.velocidad:
            self.turno_jugador()
            if self.enemigo.vida > 0:
                self.turno_enemigo()
        else:
            self.turno_enemigo()
            if self.jugador.vida > 0:
                self.turno_jugador()

        self.actualizar_stats()

    def turno_jugador(self):
        daño = max(self.jugador.ataque - self.enemigo.defensa, 0)
        self.enemigo.vida -= daño
        self.log_label.text += f"\nTú atacas (-{daño})\n"

        if self.enemigo.vida <= 0:
            self.log_label.text += "🔥 Enemigo derrotado\n"

    def turno_enemigo(self):

        # IA: huir si vida <= 10%
        if self.enemigo.vida <= (self.enemigo.vida * 0.1):
            if random.randint(1, 100) <= 20:
                self.log_label.text += "\n💨 Enemigo huyó\n"
                self.enemigo = None
                return

        daño = max(self.enemigo.ataque - self.jugador.defensa, 0)
        self.jugador.vida -= daño
        self.log_label.text += f"Enemigo ataca (-{daño})\n"

        if self.jugador.vida <= 0:
            self.log_label.text += "💀 Has sido derrotado\n"

    def huir(self, instance):

        if not hasattr(self, 'enemigo') or not self.enemigo:
            return

        if random.randint(1, 100) <= 50:
            self.log_label.text += "\n💨 Escapaste\n"
            self.enemigo = None
        else:
            self.log_label.text += "\n❌ No pudiste escapar\n"

            # enemigo contraataca
            daño = max(self.enemigo.ataque - self.jugador.defensa, 0)
            self.jugador.vida -= daño

            self.log_label.text += f"Enemigo te golpea (-{daño})\n"

            if self.jugador.vida <= 0:
                self.log_label.text += "💀 Has sido derrotado\n"

        self.actualizar_stats()

    def actualizar_stats(self):

        if hasattr(self, 'jugador'):
            self.label_jugador.text = (
                f"{self.jugador.nombre}\n"
                f"HP: {self.jugador.vida}\n"
                f"ATK: {self.jugador.ataque}\n"
                f"DEF: {self.jugador.defensa}\n"
                f"VEL: {self.jugador.velocidad}"
            )

        if hasattr(self, 'enemigo') and self.enemigo:
            self.label_enemigo.text = (
                f"{self.enemigo.tipo}\n"
                f"HP: {self.enemigo.vida}\n"
                f"ATK: {self.enemigo.ataque}\n"
                f"DEF: {self.enemigo.defensa}\n"
                f"VEL: {self.enemigo.velocidad}"
            )
        else:
            self.label_enemigo.text = "Enemigo\n---"


if __name__ == "__main__":
    GameApp().run()