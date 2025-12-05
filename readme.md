# 🧭 NomadLog – Diario de viajes colaborativo

NomadLog es una plataforma donde viajeros de todo el mundo pueden registrar sus aventuras, subir fotos, escribir anécdotas y compartir rutas o recomendaciones.  
Cada viaje contiene entradas diarias con texto, imágenes y ubicación GPS opcional.  
Otros usuarios pueden reaccionar o comentar tus entradas.

---

## 🌍 Idea principal

- Los usuarios crean viajes con fechas, país y descripción.
- Cada viaje contiene múltiples entradas (diarios de viaje).
- Otros viajeros pueden comentar y reaccionar.
- Sistema de estadísticas para ver los viajes y entradas más activas.

---

## 🗂 Entidades principales

| Entidad | Descripción |
|--------|-------------|
| **User** | Registro y autenticación de usuarios. |
| **Trip** | Viaje creado por un usuario (país, fechas, descripción). |
| **Entry** | Entradas dentro de un viaje (día, texto, fotos, ubicación GPS opcional). |
| **Comment** | Comentarios en las entradas de viaje. |
| **Reaction** | Reacciones tipo “❤️”, “🔥”, “😮” en las entradas. |

---

## 🔌 Endpoints principales

---

## 🔑 Auth

### `POST /api/auth/register/` — Registro de usuario  
### `POST /api/auth/login/` — Login y obtención de token  

---

## ✈️ Viajes

### `GET /api/trips/` — Listar viajes públicos  
### `POST /api/trips/` — Crear un nuevo viaje  
### `GET /api/trips/{id}/` — Detalles de un viaje  
### `DELETE /api/trips/{id}/` — Eliminar viaje (solo autor)  

---

## 📔 Entradas

### `GET /api/trips/{trip_id}/entries/` — Ver entradas del viaje  
### `POST /api/trips/{trip_id}/entries/` — Crear entrada con texto, fotos, coordenadas  
### `GET /api/entries/{id}/` — Ver detalle de una entrada  
### `DELETE /api/entries/{id}/` — Eliminar entrada (solo autor)  

---

## 💬 Comentarios

### `GET /api/entries/{id}/comments/` — Ver comentarios  
### `POST /api/entries/{id}/comments/` — Añadir comentario  

---

## 💖 Reacciones

### `POST /api/entries/{id}/react/` — Reaccionar a una entrada  
### `GET /api/entries/{id}/reactions/` — Ver conteo de reacciones  

---

## 📊 Estadísticas

### `GET /api/stats/popular/` — Entradas más reaccionadas  
### `GET /api/stats/active/` — Viajeros más activos del mes  

---

## 🚀 Tecnologías usadas

- Django / Django REST Framework  
- JWT Authentication  
- SQLite / PostgreSQL  
- Pillow (para imágenes)  

---

## 📦 Instalación rápida

```bash
git clone https://github.com/tuusuario/nomadlog.git
cd nomadlog
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
