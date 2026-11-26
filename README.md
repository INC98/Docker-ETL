# Docker ETL Project - Spotify Dataset

## 📖 Descripción

Este proyecto consiste en un pipeline ETL (Extract, Transform, Load) containerizado utilizando Docker, Python y PostgreSQL.

El objetivo es cargar información desde un archivo CSV con datos de canciones de Spotify hacia una base de datos PostgreSQL ejecutada en un contenedor Docker.

Durante el desarrollo se trabajó con conceptos fundamentales de Docker como:

- Dockerfile
- Docker Compose
- Redes entre contenedores
- Volúmenes persistentes
- Variables de entorno
- Construcción de imágenes personalizadas
- Comunicación entre servicios

---

## 🏗 Arquitectura

```text
┌─────────────────┐
│ Spotify CSV     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Python ETL      │
│ Container       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PostgreSQL      │
│ Container       │
└─────────────────┘
```

---

## 📂 Estructura del proyecto

```text
docker-etl-project/

├── data/
│   └── spotify.csv

├── etl/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile

├── docker-compose.yml

└── README.md
```

---

## ⚙️ Tecnologías utilizadas

- Docker
- Docker Compose
- Python 3.12
- Pandas
- SQLAlchemy
- PostgreSQL 16
- psycopg2

---

## 🚀 Ejecución

### Construcción y despliegue

```bash
docker compose up --build
```

### Ver contenedores

```bash
docker ps
```

### Entrar al contenedor PostgreSQL

```bash
docker exec -it docker-etl-project-postgres-1 bash
```

### Conectarse a la base de datos

```bash
psql -U admin -d company
```

### Consultar datos cargados

```sql
SELECT * FROM songs LIMIT 5;
```

---

## 🐳 Conceptos de Docker implementados

### Dockerfile

Se construyó una imagen personalizada para ejecutar el proceso ETL utilizando Python.

### Docker Compose

Se orquestaron dos servicios:

- PostgreSQL
- ETL Python

### Redes

Docker Compose creó automáticamente una red interna para permitir la comunicación entre ambos contenedores utilizando el hostname:

```text
postgres
```

### Volúmenes

Se implementó un volumen persistente:

```yaml
pgdata:/var/lib/postgresql/data
```

para garantizar la persistencia de la información almacenada en PostgreSQL.

### Variables de entorno

Se utilizaron variables para inicializar la base de datos:

```yaml
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
```

---

## 📸 Evidencias

### Contenedores ejecutándose

<img width="1632" height="169" alt="image" src="https://github.com/user-attachments/assets/3efe72ea-df78-463f-bdd6-671fd37556bd" />

### Datos cargados correctamente

<img width="1910" height="443" alt="image" src="https://github.com/user-attachments/assets/e1030edf-930d-4cc5-b47a-06722d2add4f" />

### Imágenes y volúmenes Docker

<img width="1635" height="236" alt="image" src="https://github.com/user-attachments/assets/b6d82144-c222-4b25-9634-d2c42a94ea56" />

---

## 🔍 Aprendizajes obtenidos

Durante este proyecto se profundizó en:

- Construcción de imágenes Docker
- Gestión de dependencias Python en contenedores
- Persistencia de datos mediante volúmenes
- Comunicación entre contenedores
- Troubleshooting de entornos Docker
- Integración entre Python y PostgreSQL
- Orquestación con Docker Compose

---

## 👤 Autor

Ignacio

Proyecto desarrollado con fines educativos para reforzar conocimientos de Docker, DevOps y Data Engineering.
