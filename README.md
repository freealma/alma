# Alma - AI Assistant CLI with Memory

Alma es un asistente AI conversacional con memoria de corto plazo, construido como interfaz CLI. 
Actualmente en fase MVP con funcionalidades básicas de chat y memoria.

## 🚀 Estado Actual: MVP Básico

### ✅ **Funciones Implementadas**
- **Chat interactivo**: Conversación con DeepSeek API
- **Memoria automática**: Guarda todas las conversaciones en SQLite
- **Consulta de memorias**: Búsqueda y visualización de historial
- **Dockerizado**: Contenedor listo para usar

### ❌ **Funciones Pendientes** (objetivos futuros)
- [ ] Agente con herramientas (ejecutar código, leer archivos)
- [ ] Análisis de proyectos de código
- [ ] Sistema de embeddings y búsqueda semántica
- [ ] Gestión avanzada de memoria

## 📦 Instalación Rápida

### Con Docker (recomendado):
```bash
# 1. Clonar repositorio
git clone <repo>
cd alma

# 2. Configurar API key
cp config/alma.env.example config/alma.env
# Editar config/alma.env y agregar DEEPSEEK_API_KEY

# 3. Construir y ejecutar
docker compose build
docker compose run --rm alma init
docker compose run --rm alma chat test
```

### Sin Docker:
```bash
pip install -e .
export DEEPSEEK_API_KEY="tu_key"
alma init
alma chat test
```

## 🎯 Uso Básico

### Comandos principales:
```bash
# Iniciar chat interactivo
docker compose run --rm alma chat chat

# Ver versión
docker compose run --rm alma version

# Inicializar base de datos
docker compose run --rm alma init

# Probar conexiones
docker compose run --rm alma chat test
```

### Gestión de memorias:
```bash
# Ver últimas 10 memorias
docker compose run --rm alma chat memory

# Buscar en memorias
docker compose run --rm alma chat memory --search "python"

# Ver más memorias
docker compose run --rm alma chat memory --limit 20
```

## 🔧 Estructura del Proyecto
```
alma/
├── config/           # Configuración y Dockerfile
├── db/              # Base de datos SQLite
├── meta/            # Schemas SQL
├── src/alma/        # Código fuente
│   ├── core/        # Funcionalidades principales
│   │   ├── chat.py      # Loop de chat
│   │   ├── db.py        # Gestión de DB
│   │   └── llm_client.py # Conexión LLM
│   └── __main__.py  # CLI principal
└── docker-compose.yaml
```

## 🗃️ Esquema de Base de Datos
```sql
CREATE TABLE memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,
    value TEXT,
    scope TEXT DEFAULT 'global',
    type TEXT DEFAULT 'string',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## ⚠️ Limitaciones Actuales
1. **No borra memorias**: Se acumulan indefinidamente
2. **Sin herramientas de agente**: Solo chat básico
3. **Comandos redundantes**: `alma chat chat` (a mejorar)
4. **Contexto limitado**: Solo últimas conversaciones

## 🚧 Próximos Pasos
1. Agregar herramientas de agente (ejecutar código)
2. Implementar sistema de embeddings
3. Mejorar gestión de memoria (limpieza automática)
4. Simplificar estructura de comandos

## 🐛 Reportar Problemas
Si encuentras algún error:
1. Verificar que `config/alma.env` tenga la API key
2. Probar conexión: `docker compose run --rm alma chat test`
3. Reconstruir contenedor: `docker compose build --no-cache`