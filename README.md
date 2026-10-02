# 🔴 Simulador de Entrenamiento Pokémon

Proyecto desarrollado para la **Actividad 1 – Tema 3: Herencia** de la materia
**Programación Orientada a Objetos** (Ingeniería en Sistemas Computacionales,
Instituto Tecnológico de Aguascalientes – Educación a Distancia).

Es un simulador por consola donde, como entrenador, puedes capturar, entrenar y
hacer combatir Pokémon de distintos tipos. El proyecto aplica **herencia**,
**reutilización de miembros con `super()`**, **redefinición de métodos** y
**polimorfismo**.

---

## 📂 Estructura del proyecto

```
pokemon_simulator/
│
├── main.py              # Menú interactivo y lógica de interacción
├── README.md            # Este archivo
└── clases/
    ├── __init__.py
    └── pokemon.py       # Clase base Pokemon y clases derivadas
```

---

## 🧬 Jerarquía de clases

| Clase            | Hereda de | Tipo    | Ventaja (x2)   | Desventaja (÷2) |
|------------------|-----------|---------|----------------|-----------------|
| `Pokemon`        | —         | base    | —              | —               |
| `PokemonFuego`   | `Pokemon` | Fuego   | vs **Planta**  | vs **Agua**     |
| `PokemonAgua`    | `Pokemon` | Agua    | vs **Fuego**   | vs **Planta**   |
| `PokemonPlanta`  | `Pokemon` | Planta  | vs **Agua**    | vs **Fuego**    |

Cada clase derivada:

- Reutiliza el constructor de la base con `super().__init__()`.
- **Redefine** `atacar(objetivo)` para aplicar las ventajas de tipo.
- **Extiende** `mostrar_info()` reutilizando `super().mostrar_info()` y añadiendo
  un mensaje propio de su tipo.

---

## 🧠 Conceptos de POO aplicados

- **Herencia** y reutilización de miembros (`super()`).
- **Redefinición (override)** del método `atacar()`.
- **Extensión** del método `mostrar_info()`.
- **Polimorfismo**: el menú trata a todos los Pokémon por igual y cada uno
  responde según su tipo.
- **Atributo de clase** (`_contador_pokemons`), **método de clase**
  (`total_pokemons`) y **método estático** (`validar_estadistica`).
- **Constructor** (`__init__`) y **destructor** (`__del__`).
- **Simulación de sobrecarga** mediante parámetros por defecto en `entrenar()`.
- **Manejo de errores** con `try/except` y validaciones.

---

## ▶️ Cómo ejecutar

Requisitos: **Python 3.8+** (no requiere librerías externas).

```bash
# 1. Clona el repositorio
git clone https://github.com/Jav-12-mtz/pokemon-simulator.git

# 2. Entra a la carpeta del proyecto
cd pokemon-simulator

# 3. Ejecuta el programa
python main.py
```

> 💡 En Windows, si no se ven los emojis en la consola, ejecuta antes:
> `chcp 65001` o usa la Terminal de Windows.

---

## 📋 Menú de opciones

| Opción | Acción              | Concepto demostrado                        |
|:------:|---------------------|--------------------------------------------|
| 1      | Capturar Pokémon    | Constructor + polimorfismo (tipo correcto) |
| 2      | Entrenar Pokémon    | Parámetros por defecto (sobrecarga)        |
| 3      | Atacar              | Redefinición de `atacar()` + polimorfismo  |
| 4      | Ver información     | Extensión de `mostrar_info()` + polimorfismo |
| 5      | Total de Pokémon    | Método de clase (`@classmethod`)           |
| 6      | Liberar Pokémon     | Destructor (`__del__`)                      |
| 7      | Salir               | Cierre del programa                        |

---

## 👤 Autor

**Javier Martínez Andrade**
Programación Orientada a Objetos — Tema 3: Herencia
Docente: Yomira del Carmen Rosales Martínez
