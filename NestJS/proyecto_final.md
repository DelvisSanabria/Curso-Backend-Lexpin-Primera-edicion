# Proyecto Final: "LinkHub API" (Clon de Linktree)

### 1. Objetivo del Proyecto

Construir una API RESTful que permita a los usuarios registrarse, gestionar su perfil público y administrar una lista de enlaces (links) personales. Es, en esencia, el backend para un servicio tipo "Link-in-Bio" como Linktree o Bio.link.

Este proyecto obliga a los estudiantes a usar **autenticación (JWT)**, **autorización (Guards)**, **CRUD** (Creación, Lectura, Actualización, Borrado) en rutas protegidas, **manejo de relaciones** en la base de datos (Usuario tiene Links) y **validación de datos (DTOs)**.

**Duración:** 4 Días

### 2. Alcance y Funcionalidad (Endpoints)

El proyecto se divide en tres módulos de funcionalidad principales:

**A. Módulo `Auth` (Autenticación - Rutas Públicas)**

- `POST /auth/register`: Recibe un `RegisterUserDto` (email, password). Hashea la contraseña y crea un nuevo usuario.
- `POST /auth/login`: Recibe un `LoginUserDto` (email, password). Valida las credenciales y devuelve un `access_token` (JWT).

**B. Módulo `Users` (Perfil - Rutas Protegidas)**

- `GET /users/me`: Ruta protegida por el `JwtAuthGuard`. Devuelve el perfil (email, bio, nombre) del usuario actualmente autenticado (extraído del token).
- `PATCH /users/me`: Ruta protegida. Recibe un `UpdateProfileDto` (ej. `displayName`, `bio`) y actualiza el perfil del usuario autenticado.

**C. Módulo `Links` (Enlaces - Rutas Protegidas)**

- `POST /links`: Ruta protegida. Recibe un `CreateLinkDto` (`title`, `url`). Crea un nuevo enlace **asociado al usuario autenticado**.
- `GET /links`: Ruta protegida. Devuelve todos los enlaces que pertenecen **únicamente** al usuario autenticado.
- `PATCH /links/:id`: Ruta protegida. Recibe un `UpdateLinkDto`. Permite al usuario actualizar uno de sus propios enlaces.
- `DELETE /links/:id`: Ruta protegida. Permite al usuario eliminar uno de sus propios enlaces.

**D. Módulo `Profile` (Público - Ruta Pública)**

- `GET /profile/:email`: Ruta pública. Recibe un email (o un *username* si se implementa). Devuelve la información *pública* del perfil (nombre, bio) y la lista de *links* asociados a ese usuario.

### 3. Conceptos Clave a Practicar

- **Arquitectura:** Patrón Módulo-Controlador-Servicio.
- **Base de Datos (Prisma):**
    - Creación del `schema.prisma` con una relación **uno-a-muchos** (un `User` tiene muchos `Links`).
    - Ejecutar `prisma migrate` para crear las tablas.
    - Usar `PrismaService` inyectado en los servicios.
- **Autenticación (JWT):**
    - `AuthModule` configurando `JwtModule`.
    - `AuthService` para `register` (con `bcrypt`) y `login` (firmando el token).
    - `JwtStrategy` para validar el token.
- **Autorización (Guards):**
    - `JwtAuthGuard` protegiendo todos los *endpoints* de `Users` y `Links`.
- **Validación (Pipes y DTOs):**
    - Usar `ValidationPipe` global.
    - Crear DTOs con `class-validator`: `RegisterUserDto`, `CreateLinkDto`, `UpdateProfileDto`.
- **Lógica de Negocio (Services):**
    - La parte más importante: Asegurarse en `LinksService` (para `PATCH` y `DELETE`) que el usuario que hace la petición sea el **dueño** del enlace que intenta modificar. (Ej: `if (link.userId !== authUser.id) throw ForbiddenException()`).
- **Documentación (Swagger):**
    - Configurar Swagger para documentar y probar la API.

### 4. Plan de accion sugerido

Este es un desglose agresivo pero factible que prioriza la funcionalidad central.

**Configuración y Autenticación**

- **Objetivo:** Tener un usuario que pueda registrarse e iniciar sesión.
- **Tareas:**
    1. Iniciar proyecto NestJS (`nest new`).
    2. Instalar Prisma, `class-validator`, `@nestjs/jwt`, `passport`, `bcrypt`.
    3. Diseñar `schema.prisma` (modelos `User` y `Link`).
    4. Ejecutar `prisma migrate dev`.
    5. Crear `PrismaService` y `PrismaModule` (global).
    6. Crear `AuthModule`, `AuthController`, `AuthService`.
    7. Implementar `POST /auth/register` (con hasheo de `bcrypt`).
    8. Implementar `POST /auth/login` (con firma de `JwtService`).
    9. Probar con Postman o Insomnia.

**Protección de Rutas**

- **Objetivo:** Crear el Guard y proteger una ruta de perfil.
- **Tareas:**
    1. Crear la `JwtStrategy` (validación del token).
    2. Crear el `JwtAuthGuard`.
    3. Crear `UsersModule`, `UsersController`, `UsersService`.
    4. Implementar `GET /users/me` y protegerla con `@UseGuards(JwtAuthGuard)`.
    5. Usar `@Request() req` en el controlador para extraer el `req.user` (inyectado por la estrategia) y devolver el perfil.

**Módulo de Links (CRUD Básico)**

- **Objetivo:** Permitir a un usuario autenticado crear y ver sus propios enlaces.
- **Tareas:**
    1. Crear `LinksModule`, `LinksController`, `LinksService`.
    2. Crear `CreateLinkDto` (con `@IsUrl()`, `@IsString()`).
    3. Implementar `POST /links` (protegido). El servicio debe tomar el `userId` del `req.user` para asociar el enlace.
    4. Implementar `GET /links` (protegido). El servicio debe buscar en la BD (`prisma.link.findMany`) usando un `where: { userId: authUser.id }`.

**Lógica de Autorización y Edición**

- **Objetivo:** Implementar la lógica de negocio *crítica*: solo el dueño puede editar/borrar.
- **Tareas:**
    1. Implementar `DELETE /links/:id` (protegido).
    2. **Lógica clave:** En el servicio, primero buscar el link. Luego, comprobar si `link.userId` es igual al `authUser.id` (del token). Si no lo es, lanzar `ForbiddenException`.
    3. Implementar `PATCH /links/:id` (protegido) usando la misma lógica de autorización.

**Rutas Públicas y Documentación**

- **Objetivo:** Finalizar la API con el *endpoint* público y la documentación.
- **Tareas:**
    1. Crear `ProfileModule` (o agregarlo a `UsersModule`).
    2. Implementar el *endpoint* público `GET /profile/:email`. El servicio buscará al usuario por email y hará un `include` de sus links (`prisma.user.findUnique({ where: { email }, include: { links: true } })`).
    3. Configurar **Swagger** en `main.ts`.
    4. (Tiempo extra) Configurar **CORS** en `main.ts`.

### Bonus (Para Alumnos Avanzados)

Si terminan antes, pueden añadir:

- **Roles:** Añadir un rol de `ADMIN` al usuario para que pueda ver/borrar *todos* los links.
- **Paginación:** Implementar paginación en `GET /links` si el usuario tiene muchos.
- **Subida de Imágenes:** Añadir un *endpoint* en `PATCH /users/me` para subir un avatar (requiere `multer`).