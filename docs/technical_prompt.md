
# 🧠 ALMA - TECHNICAL CONTEXT
# Versión: 0.1.0 | Estado: MVP BÁSICO
# Última actualización: 10 Diciembre 2025

## 🎯 RESUMEN EJECUTIVO
Alma es un asistente AI CLI con memoria de corto plazo. Actualmente en fase MVP con funcionalidades básicas de chat y memoria SQLite.

## ✅ FUNCIONALIDADES IMPLEMENTADAS

### 1. Sistema CLI (Typer)
- `alma chat` - Chat interactivo con sesiones
- `alma memory` - Gestión de memorias (list/search/show/stats)
- `alma test` - Testing de componentes (all/db/llm)
- `alma version` - Versión del sistema
- `alma init` - Inicialización de base de datos

### 2. Memoria (SQLite)
- Guardado automático de conversaciones
- Búsqueda por contenido (SQL LIKE)
- Scopes: global, session (por sesión de chat)
- Sin límites automáticos (TODO)
- Sin limpieza automática (TODO)

### 3. Integración LLM
- DeepSeek Chat API vía langchain-deepseek
- System prompt con identidad básica
- Contexto de memorias en cada prompt
- Manejo de historial de conversación

### 4. Docker
- Contenedor Python 3.11-slim
- Volúmenes persistentes para DB
- Build optimizado con caching

## ❌ FUNCIONALIDADES FALTANTES (OBJETIVOS)

### Alta Prioridad
- [ ] Herramientas de agente (execute_python, read_file)
- [ ] Límites de memoria y limpieza automática
- [ ] Sistema de embeddings para búsqueda semántica

### Media Prioridad  
- [ ] Análisis de proyectos de código
- [ ] Exportar/importar conversaciones
- [ ] Mejor sistema de logging

### Baja Prioridad
- [ ] Interfaz web opcional
- [ ] Múltiples proveedores LLM
- [ ] Sistema de plugins

## 🏗️ ARQUITECTURA

### Estructura de Archivos
```
src/alma/
├── __main__.py                 # Punto de entrada CLI (Typer app)
├── core/                       # Módulos principales
│   ├── chat.py                 # Chat interactivo + ChatSession class
│   ├── db.py                   # MemoryDB class (SQLite CRUD)
│   ├── llm_client.py           # LLMClient class (DeepSeek API)
│   ├── memory.py               # Comandos CLI de memoria (Typer app)
│   ├── test.py                 # Comandos CLI de testing (Typer app)
│   └── __init__.py             # Exports
└── utils/
    └── config.py               # ConfigLoader + settings
```

### Flujo de Datos
```
Usuario → CLI → Comando → [Chat/Memory/Test] → [DB/LLM] → Respuesta → Usuario
                     ↓
                Guardar en DB (si aplica)
```

### Esquema de Base de Datos
```sql
-- Tabla: memories
id: INTEGER PRIMARY KEY
key: TEXT UNIQUE           -- Formato: {session}_{timestamp}_{hash}
value: TEXT                -- "User: ...\nAlma: ..."
scope: TEXT DEFAULT 'global' -- 'global', 'session_id', 'system'
type: TEXT DEFAULT 'string'
updated_at: DATETIME DEFAULT CURRENT_TIMESTAMP
```

## 🔧 COMPONENTES DETALLADOS

### 1. MemoryDB (db.py)
```python
class MemoryDB:
    • init_db() - Crea tabla si no existe
    • add_memory(key, value, scope) - INSERT OR REPLACE
    • get_memory(key) - SELECT por clave
    • get_recent_memories(limit, scope) - ORDER BY updated_at DESC
    • search_memories(query, limit) - WHERE value LIKE %query%
    • Sin: delete, update, limpieza automática
```

### 2. LLMClient (llm_client.py)
```python
class LLMClient:
    • __init__() - Configura DeepSeek con API key
    • generate_response() - Prompt con memorias + historial
    • test_connection() - Ping a API
    • System prompt básico sin personalización avanzada
```

### 3. ChatSession (chat.py)
```python
class ChatSession:
    • chat_loop() - Interacción interactiva
    • get_relevant_memories() - Combina: búsqueda + recientes + globales
    • add_to_memory() - Guarda cada intercambio User→Alma
    • Comandos internos: exit, clear, memory
```

### 4. Comandos CLI
```python
# alma chat --session <id>      # Chat interactivo
# alma memory list --limit 10   # Listar memorias
# alma memory search "text"     # Buscar en memorias  
# alma memory stats             # Estadísticas
# alma memory show <key>        # Mostrar memoria específica
# alma test all                 # Test completo
# alma test db                  # Solo test DB
# alma test llm                 # Solo test LLM
```

## ⚙️ CONFIGURACIÓN

### Variables Requeridas (config/alma.env)
```env
DEEPSEEK_API_KEY=sk-...        # Requerido
DATABASE_URL=sqlite:///db/alma.db
DEFAULT_MODEL=deepseek-chat
DEFAULT_TEMPERATURE=0.7
MAX_TOKENS=2000
MEMORY_CONTEXT_SIZE=5
```

### Docker
```dockerfile
FROM python:3.11-slim
ENTRYPOINT ["alma"]           # Todos los comandos: docker-compose run --rm alma <cmd>
CMD ["chat"]                  # Comando por defecto
```

```yaml
# docker-compose.yaml
volumes:
  - ./db:/app/db             # DB persistente
  - ./config/alma.env:/app/config/alma.env:ro
```

## 🚀 COMANDOS DE DESARROLLO

### Setup Inicial
```bash
# Reconstruir desde cero
docker-compose down -v
docker-compose build --no-cache
docker-compose run --rm alma init
docker-compose run --rm alma test all
```

### Desarrollo
```bash
# Ejecutar comandos
docker-compose run --rm alma <comando>

# Chat interactivo
docker-compose run --rm alma chat

# Verificar estructura
docker-compose run --rm alma --help
docker-compose run --rm alma memory --help
```

### Debugging
```bash
# Acceder al contenedor
docker-compose exec alma bash

# Ver logs
docker-compose logs -f alma

# Inspeccionar DB
sqlite3 db/alma.db "SELECT COUNT(*) FROM memories;"
```

## 🐛 PROBLEMAS CONOCIDOS

### 1. Memoria ilimitada
- **Problema**: DB crece indefinidamente
- **Solución pendiente**: Implementar TTL o límites por sesión

### 2. Sin herramientas de agente
- **Problema**: Solo chat, no puede ejecutar código
- **Solución pendiente**: Implementar `execute_python()` tool

### 3. Búsqueda básica
- **Problema**: Solo SQL LIKE, no embeddings
- **Solución pendiente**: Vector DB + búsqueda semántica

### 4. Error Handling básico
- **Problema**: Pocos try/catch, mensajes genéricos
- **Solución pendiente**: Mejor sistema de logging

## 📍 ARCHIVOS CLAVE PARA MODIFICAR

### Para agregar herramientas:
```python
# 1. Crear: src/alma/core/tools.py
# 2. Agregar funciones con @tool decorator
# 3. Importar en __main__.py
# 4. Registrar como subcomando
```

### Para mejorar memoria:
```python
# En db.py agregar:
# • delete_old_memories(days_old)
# • enforce_limit(max_per_scope)
# • add_importance_score()
```

### Para cambiar LLM:
```python
# En llm_client.py:
# • Cambiar ChatDeepSeek por otro provider
# • Actualizar system prompt
# • Ajustar parámetros de modelo
```

## 🔄 FLUJO DE DESARROLLO TÍPICO

1. **Modificar código** en `src/alma/core/`
2. **Reconstruir contenedor**: `docker-compose build`
3. **Probar cambios**: `docker-compose run --rm alma test all`
4. **Ejecutar funcionalidad**: `docker-compose run --rm alma <cmd>`
5. **Verificar DB**: `sqlite3 db/alma.db "SELECT * FROM memories LIMIT 5;"`

## 🎯 PRÓXIMOS PASOS RECOMENDADOS

### Fase 1: Estabilizar MVP (Actual)
1. Agregar límites de memoria automáticos
2. Implementar comando `cleanup`
3. Mejorar error handling y logging

### Fase 2: Agente Básico
1. Herramienta `execute_python(code)`
2. Herramienta `read_file(path)`
3. Integración con LangChain agent

### Fase 3: Memoria Avanzada
1. Embeddings con sentence-transformers
2. Vector DB (Chroma/FAISS)
3. Búsqueda semántica

### Fase 4: Análisis de Código
1. Recorrer proyectos
2. Sugerir mejoras
3. Análisis de dependencias

## 📚 DEPENDENCIAS PRINCIPALES

```toml
# pyproject.toml
langchain>=0.1.0           # Framework LLM
langchain-deepseek>=0.0.2  # DeepSeek integration
typer>=0.9.0              # CLI framework
rich>=13.7.0              # Terminal formatting
python-dotenv>=1.0.0      # Environment variables
sqlalchemy>=2.0.0         # ORM (futuro)
```

## ⁉️ PREGUNTAS FRECUENTES TÉCNICAS

**Q: ¿Por qué SQLite y no PostgreSQL?**
**R:** Simplicidad para MVP. SQLite es suficiente para miles de memorias. Se puede migrar después.

**Q: ¿Por qué no hay autenticación?**
**R:** Alma está diseñado para uso local/desarrollo. Para producción, agregar auth.

**Q: ¿Cómo escalar para múltiples usuarios?**
**R:** 1) Session IDs únicos, 2) DB pooling, 3) Rate limiting, 4) Cache Redis.

**Q: ¿Por qué DeepSeek y no OpenAI/Gemini?**
**R:** Costo y acceso. DeepSeek ofrece buen rendimiento por precio. Se puede abstract después.

---

*Documentación técnica mantenida por el equipo de Alma. Última revisión: v0.1.0*