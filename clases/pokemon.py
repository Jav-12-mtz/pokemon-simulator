"""
pokemon.py
===========
Jerarquía de clases para el Simulador de Entrenamiento Pokémon.

Contiene:
    - Pokemon          -> clase base
    - PokemonFuego     -> clase derivada (tipo Fuego)
    - PokemonAgua      -> clase derivada (tipo Agua)
    - PokemonPlanta    -> clase derivada (tipo Planta)

Conceptos aplicados (Unidad 3 - Herencia):
    * Herencia y reutilización de miembros con super().
    * Redefinición (override) de métodos: atacar().
    * Extensión de métodos: mostrar_info().
    * Polimorfismo en tiempo de ejecución.
    * Atributo de clase, método de clase (@classmethod) y
      método estático (@staticmethod).
    * Constructor (__init__) y destructor (__del__).

Autor: Javier Martínez Andrade
"""


class Pokemon:
    """Clase base que representa a un Pokémon genérico."""

    # ------------------------------------------------------------------ #
    # Atributo de clase: compartido por TODAS las instancias.
    # Lleva la cuenta de cuántos Pokémon están activos (capturados).
    # ------------------------------------------------------------------ #
    _contador_pokemons = 0

    # Valores de mejora por defecto al subir de nivel.
    _MEJORA_ATAQUE = 5
    _MEJORA_DEFENSA = 3
    _MEJORA_SALUD = 10

    def __init__(self, nombre, ataque, defensa, salud):
        """Constructor: inicializa los atributos del Pokémon."""
        self.nombre = nombre                 # público
        self.nivel = 1                       # público: todos inician en nivel 1
        self.ataque = ataque                 # público
        self.defensa = defensa               # público
        self.salud = salud                   # público: salud actual
        self.salud_maxima = salud            # público: salud máxima
        self._tipo = "Normal"                # protegido: lo fijan las derivadas

        # Se incrementa el contador de la CLASE (no de la instancia).
        Pokemon._contador_pokemons += 1

        print(f"¡{self.nombre} ha sido capturado! 🎉")

    def __del__(self):
        """Destructor: se ejecuta al liberar (eliminar) un Pokémon."""
        print(f"{self.nombre} ha sido liberado ✨")
        Pokemon._contador_pokemons -= 1

    # ================================================================== #
    #                       MÉTODOS DE INSTANCIA                          #
    # ================================================================== #
    def entrenar(self, ataque=None, defensa=None, salud=None):
        """
        Entrena al Pokémon: sube 1 nivel y mejora sus estadísticas.

        Usa valores por defecto (None) para simular SOBRECARGA:
            * entrenar()              -> mejora TODAS las estadísticas base.
            * entrenar(ataque=10)     -> sube nivel y mejora solo el ataque.
            * entrenar(5, 5, 20)      -> mejora ataque, defensa y salud.
        """
        print(f"\n💪 {self.nombre} está entrenando...")

        # Si no se indica ninguna estadística, se mejoran todas (nivel base).
        if ataque is None and defensa is None and salud is None:
            self.subir_nivel()
            return

        # En caso contrario, se aplican solo las mejoras indicadas.
        self.nivel += 1
        if ataque:
            self.ataque += ataque
        if defensa:
            self.defensa += defensa
        if salud:
            self.salud_maxima += salud
            self.salud += salud
        print(f"¡{self.nombre} subió al nivel {self.nivel}! "
              f"(ATK {self.ataque} | DEF {self.defensa} | HP {self.salud}/{self.salud_maxima})")

    def atacar(self, objetivo):
        """
        Ataque básico contra otro Pokémon.

        El daño base es: ataque - defensa del objetivo (mínimo 1).
        Este método se REDEFINE en las clases derivadas para aplicar
        las ventajas y desventajas de tipo.
        """
        if objetivo.salud == 0:
            print(f"⚠️  {objetivo.nombre} ya está debilitado, no puedes atacarlo.")
            return 0

        dano = max(1, self.ataque - objetivo.defensa)
        print(f"⚔️  {self.nombre} ataca a {objetivo.nombre} y causa {dano} de daño.")
        objetivo.recibir_dano(dano)
        return dano

    def recibir_dano(self, cantidad):
        """Reduce la salud del Pokémon; avisa si se debilita."""
        self.salud = max(0, self.salud - cantidad)
        print(f"   {self.nombre} ahora tiene {self.salud}/{self.salud_maxima} de salud.")
        if self.salud == 0:
            print(f"   💀 ¡{self.nombre} se ha debilitado!")

    def mostrar_info(self):
        """Muestra la información del Pokémon. Se EXTIENDE en las derivadas."""
        print("┌────────────────────────────────────────────┐")
        print(f"  Nombre : {self.nombre}")
        print(f"  Tipo   : {self._tipo}")
        print(f"  Nivel  : {self.nivel}")
        print(f"  Ataque : {self.ataque}   Defensa: {self.defensa}")
        print(f"  Salud  : {self.salud}/{self.salud_maxima}")

    def subir_nivel(self):
        """Método interno: sube el nivel y mejora las estadísticas base."""
        self.nivel += 1
        self.ataque += self._MEJORA_ATAQUE
        self.defensa += self._MEJORA_DEFENSA
        self.salud_maxima += self._MEJORA_SALUD
        self.salud = self.salud_maxima  # se recupera por completo al subir de nivel
        print(f"¡{self.nombre} subió al nivel {self.nivel}! ✨")
        print(f"   ATK {self.ataque} | DEF {self.defensa} | HP {self.salud}/{self.salud_maxima}")

    # ================================================================== #
    #                        MÉTODO DE CLASE                              #
    # ================================================================== #
    @classmethod
    def total_pokemons(cls):
        """Devuelve cuántos Pokémon están activos (capturados)."""
        return cls._contador_pokemons

    # ================================================================== #
    #                        MÉTODO ESTÁTICO                             #
    # ================================================================== #
    @staticmethod
    def validar_estadistica(valor):
        """Verifica que un valor de estadística sea un número positivo."""
        return isinstance(valor, (int, float)) and valor > 0


# ====================================================================== #
#                          CLASES DERIVADAS                              #
# ====================================================================== #
class PokemonFuego(Pokemon):
    """Pokémon de tipo Fuego. Fuerte contra Planta, débil contra Agua."""

    def __init__(self, nombre, ataque, defensa, salud):
        # Reutiliza el constructor de la clase base con super().
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Fuego"

    def atacar(self, objetivo):
        """Redefine el ataque aplicando ventajas del tipo Fuego."""
        if objetivo.salud == 0:
            print(f"⚠️  {objetivo.nombre} ya está debilitado, no puedes atacarlo.")
            return 0

        dano = max(1, self.ataque - objetivo.defensa)
        if objetivo._tipo == "Planta":
            dano *= 2
            print("🔥 ¡Es súper efectivo!")
        elif objetivo._tipo == "Agua":
            dano = max(1, dano // 2)
            print("💧 No es muy efectivo...")

        print(f"⚔️  {self.nombre} ataca a {objetivo.nombre} y causa {dano} de daño.")
        objetivo.recibir_dano(dano)
        return dano

    def mostrar_info(self):
        # Extiende el método base: primero lo reutiliza y luego añade lo suyo.
        super().mostrar_info()
        print("  🔥 ¡Arde con pasión!")


class PokemonAgua(Pokemon):
    """Pokémon de tipo Agua. Fuerte contra Fuego, débil contra Planta."""

    def __init__(self, nombre, ataque, defensa, salud):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Agua"

    def atacar(self, objetivo):
        """Redefine el ataque aplicando ventajas del tipo Agua."""
        if objetivo.salud == 0:
            print(f"⚠️  {objetivo.nombre} ya está debilitado, no puedes atacarlo.")
            return 0

        dano = max(1, self.ataque - objetivo.defensa)
        if objetivo._tipo == "Fuego":
            dano *= 2
            print("💧 ¡Es súper efectivo!")
        elif objetivo._tipo == "Planta":
            dano = max(1, dano // 2)
            print("🌿 No es muy efectivo...")

        print(f"⚔️  {self.nombre} ataca a {objetivo.nombre} y causa {dano} de daño.")
        objetivo.recibir_dano(dano)
        return dano

    def mostrar_info(self):
        super().mostrar_info()
        print("  💧 ¡Fluye como el río!")


class PokemonPlanta(Pokemon):
    """Pokémon de tipo Planta. Fuerte contra Agua, débil contra Fuego."""

    def __init__(self, nombre, ataque, defensa, salud):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Planta"

    def atacar(self, objetivo):
        """Redefine el ataque aplicando ventajas del tipo Planta."""
        if objetivo.salud == 0:
            print(f"⚠️  {objetivo.nombre} ya está debilitado, no puedes atacarlo.")
            return 0

        dano = max(1, self.ataque - objetivo.defensa)
        if objetivo._tipo == "Agua":
            dano *= 2
            print("🌿 ¡Es súper efectivo!")
        elif objetivo._tipo == "Fuego":
            dano = max(1, dano // 2)
            print("🔥 No es muy efectivo...")

        print(f"⚔️  {self.nombre} ataca a {objetivo.nombre} y causa {dano} de daño.")
        objetivo.recibir_dano(dano)
        return dano

    def mostrar_info(self):
        super().mostrar_info()
        print("  🌿 ¡Crece con fuerza!")
