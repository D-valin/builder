# Sistema de Gestión de Inventario Pro

Aplicación web diseñada para que pequeños y medianos negocios puedan gestionar su inventario, registrar ventas, controlar proveedores y generar reportes, todo desde una interfaz rápida y moderna construida con **React** en el frontend y **FastAPI + PostgreSQL** en el backend.

---
## oeee
## ¿Qué incluye?

- **Autenticación completa** — Registro, inicio de sesión y recuperación de contraseña por correo electrónico.
- **Gestión de roles** — Diferencia entre usuario administrador y usuario estándar con accesos restringidos.
- **Inventario** — Agrega, edita y elimina productos con soporte para SKU, precios, stock y fechas de vencimiento.
- **Punto de Venta** — Registra salidas de stock y ventas rápidamente.
- **Proveedores** — Administra tu lista de proveedores y órdenes de compra.
- **Reportes** — Visualiza resúmenes de ventas y utilidad del negocio.

---

## Tecnologías

| Capa | Stack |
|---|---|
| Frontend | React 18 · Vite · TailwindCSS |
| Backend | FastAPI · SQLAlchemy · PostgreSQL |
| Auth | JWT · bcrypt |
| Email | SMTP (Gmail) |

---

## Cómo iniciar el proyecto

### Backend

```bash
# 1. Entrar a la carpeta del backend
cd backend

# 2. Crear entorno virtual e instalar dependencias
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 3. Crear el archivo .env con tus datos (ver ejemplo abajo)

# 4. Iniciar el servidor
python -m uvicorn app.main:app --reload
```

El servidor queda disponible en `http://localhost:8000`

#### Archivo `.env` del backend

```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_db
SECRET_KEY=una_clave_secreta_larga
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=tu@gmail.com
SMTP_PASSWORD=tu_app_password
EMAIL_FROM=tu@gmail.com
```

---

### Frontend

```bash
# 1. Entrar a la carpeta del frontend
cd product-tracker

# 2. Instalar dependencias
npm install

# 3. Crear el archivo .env
# VITE_API_URL=http://localhost:8000

# 4. Iniciar la app
npm run dev
```

La aplicación queda disponible en `http://localhost:5173`
