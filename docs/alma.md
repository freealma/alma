> Rol: Eres alma agente copiloto de compañia diaria de bird, experto en python, SQL y docker.

# Alma chat cli con funciones de agente

Quiero construir junto a tì un chat cli con memoria de corto plazo en principio y conectado por LLM con la api key de deepseek.

---

## Objetivo: Construir un chat cli con futuro como agente

Mi idea base es construir un chat cli con el cual podamos hablar y pueda ejecutar funciones como agente y qe pueda recorrer su codigo y sugerir mejoras

Funciones esperadas:
 
 - Chat cli para poder hablar a tra vez de un terminal cli

 - Cargar memorias desde una base sqlite3

 - Contestar utilizando las memorias como contexto mas no como respuestas (formular nuevas respuestas en base a las memorias)

---

## Contexto: 

A continuacion te voy a dejar todo lo necesario para construir alma y lo qe deberiamos saber.

---

### Configuración:

Toda la configuracion ira dentro de la carpeta `config/` tanto el `Dockerfile` como `alma.env` que determinara el entorno de alma.

El pyroject y el docker compose iran en la raiz.

---

### Estructura fisica:

Esta es la estructura fisica actual 

```txt
~/alma
.
├── config
│   ├── alma.env                    # Configuracion de entorno de alma
│   ├── Dockerfile                  # Configuracion del contenedor
│   └── README.md
├── db
│   ├── alma.db                     # Base de datos para memorias de corto plazo
│   └── README.md
├── docker-compose.yaml             # Orquestador general
├── docs
│   ├── alma.md                     # Sprint actual de alma (este acrchivo)
│   ├── git_standards.md            # Standars de trabajo en git (obviar)
│   └── README.md
├── meta
│   ├── README.md
│   └── schema.sql                  # Schema para la base de datos
├── pyproject.toml                  # Configuracion de dependencias
├── README.md
└── src                             # Codigo fuente
    ├── alma                        # Paquete python alma
    │   ├── core
    │   │   ├── chat.py             # Script para chat
    │   │   ├── db.py               # Manejo de base de datos
    │   │   ├── __init__.py
    │   │   └── llm_client.py       # Script de coneccion al LLM
    │   ├── __init__.py
    │   ├── __main__.py             # Script cli qe llama a las funciones
    │   ├── README.md
    │   └── utils
    │       ├── config.py           # Configuracion general
    │       └── __init__.py
    └── README.md
```

---

### Tecnologias a utilizar.


**Server LLM:** Utilizaremos lang chain para el servicio llm y el cmportamiento como agente

**Typer:** Para interfaz de comandos

**Rich:** Para enriquecer el terminal

**SQLite3:** Para el manejo de las memorias de corto plazo

---

### ``schema.sql`` 

Este es el schema con el que vamos a trabajar en principio.

```sql
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,
    value TEXT,
    scope TEXT DEFAULT 'global',           -- global, session, project
    type TEXT DEFAULT 'string',            -- para futuras evoluciones
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## Respuesta esperada:

Entiendo que ahi muchas cosas por mejorar pero estamos en las primeras versiones vamos a trabajar en la coneccion base y que pueda responder a travez del chat y luego ya iremos agregando cosas pero por ahora quiisera hacer el chat que conecte y agregar memorias simples

### Scripts esperados:

 - chat.py: Script loop del chat
    
 - llm_client.py: Coneccion a llm a travez de deepseek api

 - db.py: Manejo de memorias para subir memorias y llamar memorias (no complejizar en principio)

 - config.py: Configuracion general de alma

 ### Configuraciones esperadas

 - docker-compose.yaml: Orquestador general

 - pyproject.toml: Script con dependencias 

 - Dockerfile

 ---

 > Nota: No complejizar en principio mantengamos con pocos scripts y vamos mejorando