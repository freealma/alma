
# 🧠 Alma - AI Assistant CLI with Memory

Alma es un asistente AI conversacional con memoria de corto plazo, construido como interfaz CLI. 
Conecta con DeepSeek API y mantiene contexto de conversaciones en SQLite.

## ✨ Características

- 💬 **Chat interactivo** con DeepSeek AI
- 🗃️ **Memoria automática** - Guarda conversaciones en SQLite
- 🔍 **Búsqueda de historial** - Encuentra conversaciones pasadas
- 🐳 **Contenedor Docker** - Fácil despliegue
- 📊 **Estadísticas** - Monitorea uso de memoria
- 🧪 **Tests integrados** - Verifica conexiones

## 🚀 Instalación Rápida

### Prerrequisitos
- Docker y Docker Compose
- API Key de [DeepSeek](https://platform.deepseek.com/)

### Pasos
```bash
# 1. Clonar repositorio
git clone git@github.com:freealma/alma.git
cd alma

# 2. Configurar API Key
cp config/alma.env.example config/alma.env
# Editar config/alma.env y agregar: DEEPSEEK_API_KEY=tu_key_aqui

# 3. Construir contenedor
docker compose build

# 4. Inicializar Alma
docker compose run --rm alma init

# 5. Probar conexiones
docker compose run --rm alma test all
```

## 📖 Uso Básico

### Comandos Principales
```bash
# Iniciar chat interactivo
docker compose run --rm alma chat

# Con sesión específica
docker compose run --rm alma chat --session proyecto_x

# Ver versión
docker compose run --rm alma version

# Inicializar base de datos
docker compose run --rm alma init
```

### Gestión de Memorias
```bash
# Listar memorias recientes
docker compose run --rm alma memory list

# Buscar en memorias
docker compose run --rm alma memory search "python"

# Ver memoria específica
docker compose run --rm alma memory show "clave_de_memoria"

# Ver estadísticas
docker compose run --rm alma memory stats
```

### Testing
```bash
# Test completo del sistema
docker compose run --rm alma test all

# Solo test de base de datos
docker compose run --rm alma test db

# Solo test de LLM
docker compose run --rm alma test llm
```

## 🎮 Chat Interactivo

Dentro del chat, puedes usar:
- `exit` o `quit` - Salir
- `clear` - Limpiar historial de la sesión actual
- `memory` - Mostrar estado de memorias

Ejemplo:
```
$ docker compose run --rm alma chat
[Alma] ¡Hola! ¿En qué puedo ayudarte?
You: ¿Qué puedes hacer?
Alma: Soy Alma, un asistente AI con memoria. Puedo...
```

## 🏗️ Estructura del Proyecto

```
alma/
├── config/                 # Configuración
│   ├── alma.env            # Variables de entorno
│   └── Dockerfile          # Configuración Docker
├── db/                     # Base de datos SQLite
├── meta/                   # Schemas y metadatos
│   └── schema.sql          # Esquema de base de datos
├── pyproject.toml          # Dependencias
├── src/alma/               # Código fuente
│   ├── core/               # Módulos principales
│   │   ├── chat.py         # Chat interactivo
│   │   ├── db.py           # Gestión de base de datos
│   │   ├── llm_client.py   # Conexión DeepSeek
│   │   ├── memory.py       # Comandos de memoria
│   │   └── test.py         # Comandos de testing
│   ├── utils/              # Utilidades
│   │   └── config.py       # Configuración
│   └── __main__.py         # CLI principal
└── docker-compose.yaml     # Orquestación Docker
```

## 🔧 Configuración

### Variables de Entorno (`config/alma.env`)
```env
# DeepSeek API (requerido)
DEEPSEEK_API_KEY=tu_api_key_aqui

# Base de datos
DATABASE_URL=sqlite:///db/alma.db

# Configuración LLM
DEFAULT_MODEL=deepseek-chat
DEFAULT_TEMPERATURE=0.7
MAX_TOKENS=2000

# Memoria
MEMORY_CONTEXT_SIZE=5
```

## 🐛 Solución de Problemas

### Error: "API Key not set"
```bash
# Verificar que config/alma.env existe
ls config/alma.env

# Verificar que tenga la API key
cat config/alma.env | grep DEEPSEEK_API_KEY
```

### Error: "Database not found"
```bash
# Crear directorio de base de datos
mkdir -p db

# Inicializar base de datos
docker compose run --rm alma init
```

### Reconstruir contenedor
```bash
docker compose down
docker compose build --no-cache
docker compose run --rm alma init
```

## 📊 Esquema de Base de Datos

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

## 🚧 Próximas Características

- [ ] Herramientas de agente (ejecutar código)
- [ ] Análisis de proyectos
- [ ] Búsqueda semántica con embeddings
- [ ] Exportar/importar conversaciones
- [ ] Interfaz web opcional

## 📄 Licencia

[Tu licencia aquí]

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📞 Soporte

- Reportar issues: [GitHub Issues](tu-repo/issues)
- Documentación: `docs/TECHNICAL_PROMPT.md`