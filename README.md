# 🔴 Simulador de Entrenamiento Pokémon

Simulador por consola en **Python** donde, en el papel de entrenador, puedes
**capturar, entrenar y hacer combatir** Pokémon de distintos tipos (Fuego, Agua
y Planta). Es el proyecto de la **Actividad 1 – Tema 3: Herencia** de la materia
**Programación Orientada a Objetos** (ITA – Educación a Distancia).

El programa está pensado para demostrar, de forma práctica, los pilares de la
herencia: una **clase base** con el comportamiento común y **clases derivadas**
que lo heredan y lo especializan.

---

## 📂 Estructura del proyecto

```
pokemon_simulator/
│
├── main.py              # Menú interactivo y lógica de interacción
├── README.md            # Este archivo
└── clases/
    ├── __init__.py      # Expone las clases del paquete
    └── pokemon.py       # Clase base Pokemon + clases derivadas
```

- **`clases/pokemon.py`** contiene *qué es* un Pokémon y *qué sabe hacer*.
- **`main.py`** contiene *cómo interactúa el usuario* con esos Pokémon.

Esta separación hace que la lógica del juego (las clases) sea independiente de la
interfaz (el menú).

---

## ▶️ Cómo ejecutar

Requisitos: **Python 3.8 o superior** (no usa librerías externas).

```bash
# 1. Clona el repositorio
git clone https://github.com/Jav-12-mtz/pokemon-simulator.git

# 2. Entra a la carpeta del proyecto
cd pokemon-simulator

# 3. Ejecuta el programa
python main.py
```

> 💡 En Windows, si no se ven los emojis en la consola, ejecuta antes
> `chcp 65001` o usa la **Terminal de Windows**.

---

## ⚙️ Cómo funciona

### 1. La clase base `Pokemon`

Es la plantilla de la que parten todos los Pokémon. Define:

| Elemento | Qué es | Para qué sirve |
|----------|--------|----------------|
| `nombre`, `nivel`, `ataque`, `defensa`, `salud`, `salud_maxima` | Atributos de instancia | Estado de cada Pokémon |
| `_tipo` | Atributo **protegido** | Guarda el tipo ("Fuego", "Agua", "Planta") |
| `_contador_pokemons` | Atributo **de clase** | Cuenta los Pokémon activos (lo comparten *todas* las instancias) |
| `__init__` | **Constructor** | Inicializa el Pokémon, lo pone en nivel 1 y suma 1 al contador |
| `__del__` | **Destructor** | Se ejecuta al liberar un Pokémon; resta 1 al contador |
| `entrenar()` | Método de instancia | Sube de nivel y mejora estadísticas |
| `atacar()` | Método de instancia | Ataque básico (se **redefine** en las derivadas) |
| `recibir_dano()` | Método de instancia | Baja la salud y avisa si el Pokémon se debilita |
| `mostrar_info()` | Método de instancia | Imprime los datos (se **extiende** en las derivadas) |
| `total_pokemons()` | **`@classmethod`** | Devuelve cuántos Pokémon hay activos |
| `validar_estadistica()` | **`@staticmethod`** | Verifica que un número sea positivo |

### 2. Las clases derivadas (herencia)

`PokemonFuego`, `PokemonAgua` y `PokemonPlanta` **heredan** de `Pokemon`. Cada una:

1. **Reutiliza** el constructor de la base con `super().__init__(...)` y solo
   cambia su `_tipo`:

   ```python
   class PokemonFuego(Pokemon):
       def __init__(self, nombre, ataque, defensa, salud):
           super().__init__(nombre, ataque, defensa, salud)  # reutiliza la base
           self._tipo = "Fuego"                              # lo propio del tipo
   ```

2. **Redefine** `atacar()` para aplicar las ventajas de tipo.

3. **Extiende** `mostrar_info()`: primero llama a `super().mostrar_info()` y
   luego añade su mensaje característico (🔥, 💧 o 🌿).

Gracias a esto, el código común **no se repite**: vive una sola vez en la base.

### 3. Sistema de ventajas de tipo (redefinición de `atacar`)

El daño base de un ataque es:

```
daño = ataque_del_atacante − defensa_del_objetivo   (mínimo 1)
```

Cada tipo **redefine** `atacar()` para modificar ese daño según el tipo del
objetivo:

| Atacante | Súper efectivo (×2) contra | Poco efectivo (÷2) contra |
|----------|----------------------------|---------------------------|
| 🔥 Fuego  | 🌿 Planta                   | 💧 Agua                    |
| 💧 Agua   | 🔥 Fuego                    | 🌿 Planta                  |
| 🌿 Planta | 💧 Agua                     | 🔥 Fuego                   |

Ejemplo: un Fuego con `ataque = 60` ataca a una Planta con `defensa = 42`
→ base `60 − 42 = 18` → al ser súper efectivo se multiplica ×2 → **36 de daño**.

### 4. Polimorfismo

El menú guarda todos los Pokémon en una misma lista y los trata por igual. Cuando
hace `pokemon.atacar(objetivo)` o `pokemon.mostrar_info()`, **no necesita saber
el tipo concreto**: Python ejecuta automáticamente la versión redefinida de la
clase correspondiente. Eso es el **polimorfismo en tiempo de ejecución**.

### 5. Entrenamiento y parámetros por defecto

`entrenar(ataque=None, defensa=None, salud=None)` usa valores por defecto para
**simular sobrecarga**:

- `entrenar()` → sube de nivel y mejora **todas** las estadísticas base.
- `entrenar(ataque=10)` → sube de nivel y mejora **solo** el ataque.
- `entrenar(5, 5, 20)` → mejora ataque, defensa y salud en esas cantidades.

### 6. Contador, constructor y destructor

- Al **capturar** un Pokémon, el constructor hace `_contador_pokemons += 1`.
- Al **liberar** uno (opción 6), se elimina de la lista y `del` dispara el
  destructor `__del__`, que hace `_contador_pokemons -= 1`.
- La opción 5 muestra ese contador con el método de clase `total_pokemons()`.

### 7. El flujo del programa (`main.py`)

`main.py` ejecuta un **bucle** que repite estos pasos hasta elegir *Salir*:

```
┌─────────────────────────────────────────────┐
│ 1. Mostrar el menú                           │
│ 2. Leer la opción del usuario                │
│ 3. Ejecutar la acción (dentro de try/except) │
│ 4. Volver al paso 1                          │
└─────────────────────────────────────────────┘
```

Cada acción está en su propia función (`capturar_pokemon`, `entrenar_pokemon`,
`atacar_pokemon`, etc.), y todo se envuelve en `try/except` para que un error de
entrada **no cierre el programa**, sino que muestre un mensaje amigable.

---

## 📋 Menú de opciones

| Opción | Acción | Qué demuestra |
|:------:|--------|---------------|
| 1 | **Capturar Pokémon** | Constructor + polimorfismo (crea el tipo correcto) |
| 2 | **Entrenar Pokémon** | Parámetros por defecto (sobrecarga simulada) |
| 3 | **Atacar** | Redefinición de `atacar()` + ventajas de tipo |
| 4 | **Ver información** | Extensión de `mostrar_info()` + polimorfismo |
| 5 | **Total de Pokémon** | Método de clase (`@classmethod`) |
| 6 | **Liberar Pokémon** | Destructor (`__del__`) |
| 7 | **Salir** | Cierra el programa (libera a los que queden) |

---

## 🛡️ Validaciones y manejo de errores

- El **tipo** debe ser `Fuego`, `Agua` o `Planta`; cualquier otro se rechaza.
- Las **estadísticas** deben ser números positivos (`validar_estadistica()`).
- No se puede **atacar a un Pokémon debilitado** (salud = 0).
- Se necesitan **al menos 2 Pokémon** para combatir.
- Toda entrada inválida se captura con `try/except` y muestra un mensaje claro.

---

## 💻 Ejemplo de ejecución

```
==================================================
        SIMULADOR DE ENTRENAMIENTO POKÉMON
==================================================
  1. Capturar Pokémon
  ...
  7. Salir
==================================================
Elige una opción (1-7): 1
Nombre del Pokémon: Charmander
Tipo (Fuego / Agua / Planta): Fuego
Ataque: 55
Defensa: 40
Salud: 100
¡Charmander ha sido capturado! 🎉
```

Al atacar con ventaja de tipo:

```
🔥 ¡Es súper efectivo!
⚔️  Charmander ataca a Bulbasaur y causa 36 de daño.
   Bulbasaur ahora tiene 69/105 de salud.
```

---

## 🧠 Conceptos de POO aplicados

- **Herencia** y reutilización de miembros con `super()`.
- **Redefinición (override)** del método `atacar()`.
- **Extensión** del método `mostrar_info()`.
- **Polimorfismo** en tiempo de ejecución.
- **Atributo de clase**, **método de clase** y **método estático**.
- **Constructor** (`__init__`) y **destructor** (`__del__`).
- **Simulación de sobrecarga** con parámetros por defecto.
- **Manejo de errores** con `try/except` y validaciones.

---

## 👤 Autor

**Javier Martínez Andrade**
Programación Orientada a Objetos — Tema 3: Herencia
Docente: Yomira del Carmen Rosales Martínez
Instituto Tecnológico de Aguascalientes — Educación a Distancia
