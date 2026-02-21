# API FLASK

API REST desarrollada con **Flask** para la gestión de autenticación de usuarios mediante **JWT**, documentación interactiva con **Swagger (Flasgger)** y control de base de datos con **Flask-Migrate**.

---

## 🚀 Tecnologías utilizadas

* **Flask** → Framework principal de la API
* **Flask SQLAlchemy** → ORM para la base de datos
* **Flask Migrate** → Control de migraciones
* **Flask JWT Extended** → Autenticación con tokens
* **Flasgger (Swagger)** → Documentación interactiva

---

## 📂 Estructura del proyecto

```
api_ing_82/
│
├── app.py                # Punto de entrada de la aplicación
├── config.py             # Configuración general
├── extensions.py         # Inicialización de extensiones (db, jwt, swagger)
│
├── controllers/          # Rutas (endpoints)
│   ├── UserController.py
│   └── HomeController.py
│
├── services/             # Lógica de negocio
│   └── authService.py
│
├── models/               # Modelos de base de datos
│
└── migrations/           # Historial de migraciones
```

---

## ⚙️ Instalación y configuración

### 1️⃣ Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
```

---

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configurar variables importantes

En `config.py` asegúrate de tener:

```python
JWT_SECRET_KEY = "tu_clave_secreta"
SQLALCHEMY_DATABASE_URI = "tu_cadena_de_conexion"
```

---

## 🗄️ Migraciones de base de datos

Ejecuta los siguientes comandos:

```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```

---

## ▶️ Ejecutar la aplicación

```bash
python app.py
```

La API se ejecutará en:

```
http://localhost:5000
```

---

## 📖 Documentación Swagger

Una vez levantado el servidor, puedes acceder a la documentación interactiva en:

```
http://localhost:5000/apidocs
```

Ahí podrás probar los endpoints directamente.

---

## 🔐 Autenticación

La API usa **JWT (Bearer Token)**.

### Flujo de autenticación:

1. Registrar usuario → `/api/auth/register`
2. Iniciar sesión → `/api/auth/login`
3. Copiar el token
4. Enviar en headers:

```
Authorization: Bearer <token>
```

---

## 📌 Endpoints principales

### 🔹 Auth

* **POST** `/api/auth/register` → Registrar usuario
* **POST** `/api/auth/login` → Obtener token

### 🔹 Home

* **GET** `/api/v1` → Endpoint de prueba

---

## 🧠 Objetivo del proyecto

Este proyecto tiene como finalidad servir como base para:

* Implementar autenticación con JWT
* Documentar APIs con Swagger
* Manejar migraciones de base de datos
* Estructurar una API en capas (controllers, services, models)

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica académica para la materia de ingeniería de software.

---

