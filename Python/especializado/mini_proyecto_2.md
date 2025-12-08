### Proyecto Retador 2: "Bot de Cobranza y Facturación Automatizada"

**Duración:** 4 dias

Descripción:

El estudiante creará un sistema modular para una pequeña empresa de servicios (ej: internet o gimnasio). El sistema leerá deudores, generará facturas y notificará.

**Requerimientos Técnicos:**

1. **Modularidad:** El proyecto debe tener carpetas separadas. `main.py` (ejecutable), `modulos/gestor_archivos.py` y `modulos/notificaciones.py`.
2. **Archivos CSV:** Debe leer un archivo `clientes.csv` que contenga: *Nombre, Telefono, MontoDeuda, FechaVencimiento*.
3. **Lógica de Negocio:** Identificar quiénes tienen deudas vencidas.
4. **Archivos TXT:** Para cada deudor, generar un archivo individual `factura_[Nombre].txt` con un formato legible del cobro.
5. **Automatización WhatsApp:** Usar `pywhatkit` para enviar un mensaje automático a los deudores: *"Hola [Nombre], tu factura ya fue generada. Debes: [Monto]"*.
6. **Manejo de Excepciones:** Si el archivo CSV no existe o no hay internet para WhatsApp, el programa no debe colapsar.