# Proyecto final de Modulo

**Objetivo:** Diseñar y manipular una base de datos relacional para gestionar las operaciones básicas de una tienda en línea.

**Duracion:** 3 días

### Parte 1: Estructura de la Base de Datos (DDL)

Crea una base de datos llamada `e_commerce` y genera las siguientes tablas respetando las claves primarias (PK) y foráneas (FK) para mantener la integridad referencial.

**1. Tabla: `usuarios`**

- `id` (SERIAL, PK)
- `nombre` (VARCHAR, no nulo)
- `apellido` (VARCHAR, no nulo)
- `email` (VARCHAR, único)
- `fecha_registro` (TIMESTAMP)
- `fecha_actualizacion` (TIMESTAMP)

**2. Tabla: `productos`**

- `id` (SERIAL, PK)
- `nombre` (VARCHAR)
- `precio` (NUMERIC 10,2)
- `stock` (INT)
- `fecha_registro` (TIMESTAMP)
- `fecha_actualizacion` (TIMESTAMP)

**3. Tabla: `compras`** (Cabecera del pedido)

- `id` (SERIAL, PK)
- `usuario_id` (INT, FK referenciando a `usuarios`)
- `fecha` (DATE)
- `total` (NUMERIC 10,2)
- `fecha_registro` (TIMESTAMP)
- `fecha_actualizacion` (TIMESTAMP)

**4. Tabla: `detalles_compras`** (Líneas del pedido)

- `id` (SERIAL, PK)
- `compra_id` (INT, FK referenciando a `compras`)
- `producto_id` (INT, FK referenciando a `productos`)
- `cantidad` (INT)
- `precio_unitario` (NUMERIC 10,2) - *Importante: guarda el precio en el momento de la compra.*
- `fecha_registro` (TIMESTAMP)
- `fecha_actualizacion` (TIMESTAMP)

### Parte 2: Ejercicios de Manipulación de Datos (DML)

Realiza las siguientes operaciones mediante sentencias SQL.

### A. Ejercicios de Insertar Datos (INSERT)

1.  **Registrar Usuarios:** Inserta 3 usuarios nuevos (ej. 'Ana López', 'Carlos Ruiz', 'Maria Gomez') con sus respectivos correos y fecha de hoy.
2.  **Inventario Inicial:** Inserta 5 productos diferentes (ej. 'Laptop', 'Mouse', 'Teclado', 'Monitor', 'Auriculares') con precios y cantidades de stock variadas.
3.  **Simular una Compra:**
    * Crea una inserción en la tabla `compras` para el usuario 'Ana López'.
    * Inserta 2 registros en `detalles_compras` vinculados a la compra anterior (ej. Ana compró 1 Laptop y 2 Mouse).

### B. Ejercicios de Buscar Datos (SELECT Simple)

4.  **Listar Productos:** Obtén una lista de todos los productos disponibles (nombre y precio).
5.  **Filtro de Precios:** Muestra los productos que cuestan más de $100.00.
6.  **Búsqueda de Usuario:** Encuentra el correo electrónico del usuario cuyo nombre es 'Carlos Ruiz'.
7.  **Stock Bajo:** Muestra los productos que tienen menos de 5 unidades en stock.

### C. Ejercicios de Buscar Datos Relacionales (JOINS)

8.  **Historial de Compras:** Muestra una lista que incluya el nombre del usuario y la fecha de cada compra que ha realizado (Usa `INNER JOIN` entre `usuarios` y `compras`).
9.  **Detalle de Factura:** Muestra el nombre del producto, la cantidad comprada y el precio unitario para una compra específica (filtra por un `id` de compra).
10. **Compras por Usuario:** Obtén el nombre del usuario y el nombre de los productos que ha comprado en toda su historia (Requiere unir `usuarios`, `compras`, `detalles_compras` y `productos`).

### D. Ejercicios de Actualizar Datos (UPDATE)

1. **Ajuste de Precios:** Debido a la inflación, aumenta el precio de todos los productos en un 10%.
2. **Actualizar Stock:** El usuario 'Ana López' acaba de comprar productos; actualiza el stock de la tabla `productos` restando la cantidad comprada en el ejercicio 3.
3. **Corrección de Datos:** Cambia el correo electrónico del usuario 'Maria Gomez' a 'maria.nuevo@mail.com'.

### E. Ejercicios de Borrar Datos (DELETE)

1. **Cancelar Detalle:** Borra uno de los ítems de la tabla `detalles_compras` (como si el usuario hubiera devuelto un producto).
2. **Eliminar Producto:** Intenta borrar un producto que no ha sido vendido nunca.
3. **Limpieza de Usuarios:** Borra a los usuarios que no han realizado ninguna compra (Usa una subconsulta o `LEFT JOIN` para identificarlos).