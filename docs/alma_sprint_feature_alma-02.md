
# 🚀 Sprint Planning - ALMA-02: Sistema de Logs y Memoria (API-Based)

## 🎯 Objetivo del Sprint
Implementar sistema de gestión de memoria usando APIs externas para embeddings y LLM, con interfaz CLI para gestión de logs, ideas, memorias y decisiones.

## 📅 Timeline Estimado
- **Inicio:** Enero 2024
- **Duración:** 3-5 días de desarrollo
- **Release Target:** v0.2.0

## 🏗️ Arquitectura Realista

### Stack Tecnológico Actualizado
```
alma/
├── memory/           # Sistema de memoria
│   ├── cli/         # Interfaz de línea de comandos
│   ├── loaders/     # Cargadores de datos
│   ├── embeddings/  # Gestión con OpenAI API
│   └── llm/         # Integración DeepSeek API
├── database/        # PostgreSQL con esquema listo
└── scripts/         # Scripts de utilidad
```

### 🔌 APIs a Integrar
- **Embeddings:** OpenAI API (text-embedding-ada-002)
- **LLM:** DeepSeek API (chat/completions)
- **Database:** PostgreSQL (ya configurada)
- **CLI:** Typer para interfaz profesional

## 📋 User Stories REALES

### 🎪 Epic: Sistema de Carga de Datos
```yaml
US-01: Como usuario quiero cargar logs desde archivos YAML
Criterios:
  - ✅ Script `load_logs.py` funcional
  - ✅ Procesamiento de bitácoras existentes
  - ✅ Generación automática de embeddings

US-02: Como usuario quiero cargar ideas y decisiones
Criterios:
  - ✅ Scripts separados para cada tipo de dato
  - ✅ Validación de estructura YAML
  - ✅ Metadatos automáticos
```

### 🎪 Epic: Sistema de Embeddings
```yaml
US-03: Como sistema quiero generar embeddings con OpenAI
Criterios:
  - ✅ Integración con OpenAI API
  - ✅ Batch processing para eficiencia
  - ✅ Manejo de errores y rate limits

US-04: Como usuario quiero buscar contenido semánticamente
Criterios:
  - ✅ Consultas por similitud semántica
  - ✅ Filtros por tipo y fecha
  - ✅ Resultados ordenados por relevancia
```

### 🎪 Epic: Interfaz CLI
```yaml
US-05: Como usuario quiero interfaz CLI intuitiva
Criterios:
  - ✅ Comandos `alma logs`, `alma ideas`, `alma memories`
  - ✅ Opciones de filtrado y búsqueda
  - ✅ Output formateado y legible
```

## 🔧 Tareas Técnicas REALES

### Fase 1: Setup APIs (Día 1)
- [ ] Configurar OpenAI API para embeddings
- [ ] Configurar DeepSeek API para LLM
- [ ] Crear managers de API con error handling
- [ ] Setup environment variables seguro

### Fase 2: Sistema de Carga (Día 2)
- [ ] Script `load_logs.py` con Typer
- [ ] Script `load_ideas.py` 
- [ ] Script `load_decisions.py`
- [ ] Script `load_memories.py`
- [ ] Validador de esquemas YAML

### Fase 3: Embeddings & Búsqueda (Día 3)
- [ ] Generador de embeddings con OpenAI
- [ ] Sistema de búsqueda semántica
- [ ] Almacenamiento en PostgreSQL
- [ ] CLI de consultas básicas

### Fase 4: CLI Profesional (Día 4)
- [ ] Comando `alma` principal con Typer
- [ ] Subcomandos para cada tipo de dato
- [ ] Formateo de output profesional
- [ ] Logging de ejecuciones

## 📈 Métricas de Éxito REALES

### Criterios de Aceptación
- **Funcionalidad:** 4 scripts de carga funcionando
- **APIs:** OpenAI y DeepSeek integradas
- **CLI:** Interfaz intuitiva y documentada
- **Base de datos:** Datos con embeddings almacenados

### KPIs Técnicos
- **Tiempo de embedding:** <5 segundos por documento
- **Precisión búsqueda:** Resultados relevantes
- **Uso APIs:** Manejo correcto de rate limits
- **CLI:** Respuesta <2 segundos por comando

## 🔌 Configuración APIs

### OpenAI API (Embeddings)
```python
# Para embeddings de texto
model = "text-embedding-ada-002"
cost_estimate = ~$0.0001 / 1K tokens
```

### DeepSeek API (LLM)
```python
# Para análisis y generación
model = "deepseek-chat"
cost_estimate = ~$0.0014 / 1K tokens
```

## 🚀 Plan de Implementación Concreto

### Scripts a Desarrollar
```bash
src/alma/cli/
├── main.py           # Comando principal `alma`
├── load_logs.py      # Carga de logs con embeddings
├── load_ideas.py     # Carga de ideas
├── load_decisions.py # Carga de decisiones  
├── load_memories.py  # Carga de memorias
└── query.py          # Sistema de consultas
```

### Comandos CLI Planeados
```bash
alma logs load --file bitacora_ALMA-01.md
alma ideas load --dir data/ideas/
alma search "aprendizajes git" --type logs
alma stats --show-metrics
```

## 🔗 Dependencias Manejables

### Dependencias Confirmadas
- ✅ PostgreSQL funcionando
- ✅ Estructura ALMA-01 completada
- ✅ APIs disponibles (OpenAI, DeepSeek)

### Configuración Requerida
```bash
# Environment variables
OPENAI_API_KEY=sk-...
DEEPSEEK_API_KEY=...
DATABASE_URL=postgresql://...
```

## 💡 Beneficios de Este Enfoque

### ✅ Ventajas
- **Rápido desarrollo** - Sin entrenar modelos locales
- **Bajo costo** - Solo pagar por uso
- **Alta calidad** - Embeddings de OpenAI state-of-the-art
- **Escalable** - Fácil aumentar capacidad

### 🎯 Perfecto para
- Prototipado rápido
- Testing de conceptos
- Desarrollo iterativo

---

**👥 Equipo:** Arca (Dev)  
**📊 Capacidad:** 20-30 horas de desarrollo  
**🎯 Confidence Score:** 95% (muy realista)