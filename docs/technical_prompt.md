
# Technical Prompt for Alma Development

## CONTEXT
Alma is a CLI AI assistant with short-term memory. Current version: MVP with basic chat.

## ARCHITECTURE SUMMARY

### Core Components:
1. `src/alma/__main__.py` - CLI entry point (Typer)
2. `src/alma/core/chat.py` - Chat loop with memory integration
3. `src/alma/core/db.py` - SQLite memory management
4. `src/alma/core/llm_client.py` - DeepSeek API wrapper
5. `src/alma/utils/config.py` - Configuration loader

### Data Flow:
```
User Input → Chat Loop → Get Relevant Memories → Format Prompt → 
DeepSeek API → Response → Save to Memory → Display to User
```

### Database Schema:
```sql
CREATE TABLE memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,           -- Format: {session}_{timestamp}
    value TEXT,                -- "User: ...\nAlma: ..."
    scope TEXT DEFAULT 'global', -- 'global' or session_id
    type TEXT DEFAULT 'string',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## CURRENT IMPLEMENTATION DETAILS

### Memory System:
- Automatically saves every conversation exchange
- Search uses SQL LIKE operator
- No automatic cleanup (TODO)
- All memories are stored indefinitely

### LLM Integration:
- Uses DeepSeek Chat model
- System prompt defines Alma's identity
- Memories are injected as context
- No token counting implemented

### CLI Structure:
```
alma [MAIN]
  ├── version
  ├── init
  └── chat [SUBCOMMAND]
        ├── chat      # Interactive chat (redundant, needs fix)
        ├── memory    # Memory management
        └── test      # Connection test
```

## QUICK START FOR DEVELOPMENT

```bash
# Rebuild and test
docker-compose down -v
docker-compose build --no-cache
docker-compose run --rm alma init
docker-compose run --rm alma chat test

# Run chat
docker-compose run --rm alma chat chat

# Check memories
docker-compose run --rm alma chat memory --limit 5
```

## NEXT STEPS TO IMPLEMENT

### Phase 1: Agent Tools (Highest Priority)
```python
# Planned tools:
1. execute_python(code: str) -> str
2. read_file(path: str) -> str  
3. list_directory(path: str) -> list
4. run_shell_command(cmd: str) -> str
```

### Phase 2: Memory Improvements
- Automatic memory cleanup (TTL)
- Importance scoring
- Vector embeddings
- Semantic search

### Phase 3: Code Analysis
- Project structure analysis
- Code quality suggestions
- Dependency analysis
- Auto-refactoring suggestions

## COMMON ISSUES & SOLUTIONS

### 1. "Database not found"
```bash
mkdir -p db
docker-compose run --rm alma init
```

### 2. "API Key not set"
```bash
# Edit config/alma.env
DEEPSEEK_API_KEY=your_key_here
```

### 3. Container restart loop
```bash
docker-compose down -v
docker-compose build --no-cache
```

## DEVELOPMENT NOTES
- All chat conversations are stored in `db/alma.db`
- No authentication or rate limiting implemented
- Error handling is basic
- Logging needs improvement