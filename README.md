
# Alma - AI Assistant CLI with Memory

Alma es un asistente AI conversacional con memoria de corto plazo, construido como una interfaz CLI.

## Características

- 💬 Chat interactivo con DeepSeek AI
- 🧠 Memoria de corto plazo con SQLite
- 🔍 Búsqueda y recuperación de contexto
- 🐳 Contenedor Docker listo
- 🎨 Interfaz CLI enriquecida con Rich

## Instalación

### Local
```bash
# Instalar dependencias
pip install .

# Inicializar Alma
alma init

# Configurar API key en config/alma.env
```

### Docker
```bash
# Construir y ejecutar
docker-compose up --build

# Ejecutar comandos dentro del contenedor
docker-compose run alma [comando]
```

## Uso

```bash
# Iniciar chat
alma chat

# Chat con sesión específica
alma chat --session proyecto_x

# Gestionar memorias
alma memory
alma memory --search "python"
alma memory "memory_key"

# Verificar configuración
alma test

# Ver versión
alma version
```

## Estructura

- `src/alma/core/chat.py` - Loop principal del chat
- `src/alma/core/llm_client.py` - Cliente LLM DeepSeek
- `src/alma/core/db.py` - Gestión de base de datos SQLite
- `config/` - Configuración y Dockerfile
- `db/` - Base de datos SQLite
- `meta/` - Esquemas y metadatos


## 7. Cómo usar el sistema

1. **Primero, configura tu API key**:
   ```bash
   cp config/alma.env.example config/alma.env
   # Edita config/alma.env y agrega tu DEEPSEEK_API_KEY
   ```

2. **Instalación local**:
   ```bash
   # Instalar dependencias
   pip install -e .
   
   # Inicializar
   alma init
   
   # Probar
   alma test
   
   # Iniciar chat
   alma chat
   ```

3. **Usar con Docker**:
   ```bash
   # Construir
   docker-compose build
   
   # Ejecutar
   docker-compose up
   ```

## Próximos pasos sugeridos

1. **Agente con funciones**: Agregar herramientas para ejecutar código, leer archivos, etc.
2. **Memoria a largo plazo**: Implementar embeddings y búsqueda semántica
3. **Mejorar prompts**: Refinar el sistema prompt para mejores respuestas
4. **Interfaz web**: Agregar una interfaz web con FastAPI
5. **Plugin system**: Sistema de plugins para extender funcionalidades

El sistema está diseñado para ser modular y fácil de extender. ¡Comencemos a chatear con Alma y veamos cómo podemos mejorarlo juntos!