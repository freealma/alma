# Changelog

## [0.1.0] - 2025-12-10

### 🎉 Primer Release - MVP Básico

#### Características
- **Chat interactivo** con DeepSeek API
- **Memoria de conversaciones** en SQLite
- **Comandos CLI**:
  - `alma chat`: Chat interactivo con sesiones
  - `alma memory`: Gestión de memorias (list, search, show, stats)
  - `alma test`: Testing de componentes
  - `alma init`: Inicialización de base de datos
  - `alma version`: Versión del sistema
- **Contenedor Docker** con volúmenes persistentes
- **Documentación completa**:
  - README.md para usuarios
  - AI_CONTEXT.md para desarrolladores

#### Arquitectura
- Separación modular: chat.py, memory.py, db.py, llm_client.py
- Sistema CLI con Typer + Rich
- Configuración vía variables de entorno
- Base de datos SQLite con esquema básico

#### Notas Técnicas
- Dependencias: langchain-deepseek, typer, rich, python-dotenv
- Python 3.11+ o Docker
- Requiere API Key de DeepSeek

#### Límites Conocidos
- Sin herramientas de agente (solo chat)
- Memoria crece indefinidamente (sin límites)
- Búsqueda básica (SQL LIKE, no embeddings)

---

*Siguiente versión planificada: v0.2.0 con herramientas de agente*