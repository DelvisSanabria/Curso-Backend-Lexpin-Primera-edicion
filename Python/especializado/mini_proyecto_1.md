# Punto de Parada 1: Consolidación de Lógica y Datos

Temas cubiertos: Variables, Operadores, Estructuras de control, Bucles, Funciones, Listas, Strings, Tuplas y Diccionarios.

### Proyecto Retador 1: "Sistema de Gestión de Torneos E-Sports"

**Duración:** 3 a 4 días.

**Fecha de entrega:** 2 de Diciembre de 2025.

Descripción:

Los estudiantes deben crear un programa de consola (CLI) que administre un torneo de videojuegos. El programa no guardará datos en archivos (aún no saben hacerlo), por lo que todo vivirá en la memoria (variables) mientras el programa corra.

**Requerimientos Técnicos:**

1. **Estructuras de Datos:** Usar una lista de diccionarios para almacenar los equipos. Ejemplo: `[{ "nombre": "Team A", "puntos": 10, "jugadores": ["Juan", "Pedro"] }]`.
2. **Menú Interactivo (While + Match/If):** Un bucle infinito que muestre opciones: Registrar equipo, Registrar Jugador, Actualizar Puntos, Ver Tabla de Posiciones, Eliminar Equipo, Salir.
3. **Funciones:** Cada opción del menú debe llamar a una función específica (ej: `registrar_equipo()`, `mostrar_tabla()`).
4. **Manipulación de Strings:** Los nombres de los equipos deben guardarse siempre capitalizados (`.capitalize()` o `.title()`) y validarse que no estén vacíos.
5. **Manejo de Errores:** Usar `try-except` para evitar que el programa se rompa si el usuario ingresa letras en lugar de puntos numéricos.