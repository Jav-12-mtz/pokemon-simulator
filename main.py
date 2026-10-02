"""
main.py
========
Programa principal del Simulador de Entrenamiento Pokémon.

Muestra un menú interactivo en consola que permite capturar, entrenar,
atacar, consultar y liberar Pokémon, demostrando herencia y polimorfismo.

Autor: Javier Martínez Andrade
Materia: Programación Orientada a Objetos
Actividad 1 - Tema 3: Herencia
"""

from clases.pokemon import (
    Pokemon,
    PokemonFuego,
    PokemonAgua,
    PokemonPlanta,
)

# Tipos permitidos y la clase derivada que corresponde a cada uno.
TIPOS_VALIDOS = {
    "Fuego": PokemonFuego,
    "Agua": PokemonAgua,
    "Planta": PokemonPlanta,
}


# ---------------------------------------------------------------------- #
#                       FUNCIONES AUXILIARES                             #
# ---------------------------------------------------------------------- #
def mostrar_menu():
    """Imprime el menú principal."""
    print("\n" + "=" * 50)
    print("        SIMULADOR DE ENTRENAMIENTO POKÉMON")
    print("=" * 50)
    print("  1. Capturar Pokémon")
    print("  2. Entrenar Pokémon")
    print("  3. Atacar")
    print("  4. Ver información")
    print("  5. Total de Pokémon")
    print("  6. Liberar Pokémon")
    print("  7. Salir")
    print("=" * 50)


def pedir_entero(mensaje):
    """Pide un número entero positivo, validando la entrada."""
    valor = int(input(mensaje))
    if not Pokemon.validar_estadistica(valor):
        raise ValueError("La estadística debe ser un número positivo.")
    return valor


def seleccionar_pokemon(equipo, mensaje="Selecciona un Pokémon"):
    """Muestra la lista del equipo y devuelve el Pokémon elegido."""
    if not equipo:
        print("⚠️  No tienes Pokémon capturados todavía.")
        return None

    print(f"\n{mensaje}:")
    for i, p in enumerate(equipo, start=1):
        print(f"  {i}. {p.nombre} ({p._tipo}) - Nivel {p.nivel} "
              f"- HP {p.salud}/{p.salud_maxima}")

    indice = int(input("Número: ")) - 1
    if 0 <= indice < len(equipo):
        return equipo[indice]
    print("⚠️  Opción inválida.")
    return None


# ---------------------------------------------------------------------- #
#                   OPCIONES DEL MENÚ (acciones)                         #
# ---------------------------------------------------------------------- #
def capturar_pokemon(equipo):
    """Opción 1: crea un Pokémon del tipo indicado y lo agrega al equipo."""
    nombre = input("Nombre del Pokémon: ").strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")

    tipo = input("Tipo (Fuego / Agua / Planta): ").strip().capitalize()
    if tipo not in TIPOS_VALIDOS:
        raise ValueError(f"Tipo inválido: '{tipo}'. Usa Fuego, Agua o Planta.")

    ataque = pedir_entero("Ataque: ")
    defensa = pedir_entero("Defensa: ")
    salud = pedir_entero("Salud: ")

    # Polimorfismo: se instancia la clase derivada correcta según el tipo.
    clase = TIPOS_VALIDOS[tipo]
    nuevo = clase(nombre, ataque, defensa, salud)
    equipo.append(nuevo)


def entrenar_pokemon(equipo):
    """Opción 2: entrena a un Pokémon con los parámetros por defecto."""
    pokemon = seleccionar_pokemon(equipo, "¿A quién quieres entrenar?")
    if pokemon:
        pokemon.entrenar()  # sin argumentos -> mejora todas las estadísticas


def atacar_pokemon(equipo):
    """Opción 3: un Pokémon ataca a otro (aplica ventajas de tipo)."""
    if len(equipo) < 2:
        print("⚠️  Necesitas al menos 2 Pokémon para combatir.")
        return

    atacante = seleccionar_pokemon(equipo, "Elige al ATACANTE")
    if atacante is None:
        return
    objetivo = seleccionar_pokemon(equipo, "Elige al OBJETIVO")
    if objetivo is None:
        return

    if atacante is objetivo:
        print("⚠️  Un Pokémon no puede atacarse a sí mismo.")
        return

    print()
    # Polimorfismo: se llama atacar() sin saber el tipo concreto;
    # cada clase ejecuta su propia versión redefinida.
    atacante.atacar(objetivo)


def ver_informacion(equipo):
    """Opción 4: muestra la información de todos los Pokémon."""
    if not equipo:
        print("⚠️  No tienes Pokémon capturados todavía.")
        return

    print("\n========== TU EQUIPO POKÉMON ==========")
    for pokemon in equipo:
        # Polimorfismo: cada Pokémon muestra su información según su tipo.
        pokemon.mostrar_info()
    print("=======================================")


def total_pokemon():
    """Opción 5: muestra el total de Pokémon activos (método de clase)."""
    print(f"\n📊 Total de Pokémon capturados: {Pokemon.total_pokemons()}")


def liberar_pokemon(equipo):
    """Opción 6: elimina un Pokémon del equipo (activa el destructor)."""
    pokemon = seleccionar_pokemon(equipo, "¿A quién quieres liberar?")
    if pokemon:
        equipo.remove(pokemon)
        del pokemon  # invoca el destructor __del__


# ---------------------------------------------------------------------- #
#                          PROGRAMA PRINCIPAL                            #
# ---------------------------------------------------------------------- #
def main():
    equipo = []  # lista de Pokémon capturados

    print("¡Bienvenido, entrenador! Es hora de formar tu equipo Pokémon.")

    while True:
        mostrar_menu()
        try:
            opcion = input("Elige una opción (1-7): ").strip()

            if opcion == "1":
                capturar_pokemon(equipo)
            elif opcion == "2":
                entrenar_pokemon(equipo)
            elif opcion == "3":
                atacar_pokemon(equipo)
            elif opcion == "4":
                ver_informacion(equipo)
            elif opcion == "5":
                total_pokemon()
            elif opcion == "6":
                liberar_pokemon(equipo)
            elif opcion == "7":
                print("\n¡Hasta la próxima, entrenador! 👋")
                break
            else:
                print("⚠️  Opción no válida. Elige un número del 1 al 7.")

        except ValueError as error:
            # Captura errores de conversión y validaciones.
            print(f"❌ Error: {error}")
        except Exception as error:
            # Red de seguridad para cualquier otro error inesperado.
            print(f"❌ Ocurrió un error inesperado: {error}")


if __name__ == "__main__":
    main()
