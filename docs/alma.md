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
    │   │   ├── __init__.py
    │   │   └── llm_client.py       # Script de coneccion al LLM
    │   ├── __init__.py
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