
# 🤖 ALMA - AI ASSISTANT CONTEXT
# 📅 Created: December 2024 | Version: 0.1.0 MVP
# 🔄 Last Updated: [CURRENT_DATE]
# 🎯 Status: BASIC CHAT WITH MEMORY | Next: AGENT TOOLS

## 🏁 QUICK SUMMARY FOR AI ASSISTANTS
I'm helping develop Alma, a CLI AI assistant with short-term memory. 
CURRENT: Basic chat with conversation memory in SQLite.
NEXT GOAL: Add agent tools (code execution, file reading).

## 🎯 CURRENT CAPABILITIES (WHAT WORKS)

### ✅ **Chat System**
- Interactive CLI chat with DeepSeek API
- Saves every conversation exchange to SQLite
- Maintains session context
- Internal commands: `exit`, `clear`, `memory`

### ✅ **Memory Management**
- Automatic conversation storage
- Search memories: `LIKE %query%` in SQL
- List recent memories with filters
- Memory statistics (count, scope distribution)

### ✅ **CLI Commands**
```bash
alma chat                       # Interactive chat
alma memory list                # List memories
alma memory search "text"       # Search memories
alma memory stats               # Memory statistics
alma memory show <key>          # Show specific memory
alma test all                   # Test all components
alma init                       # Initialize database
alma version                    # Show version
```

### ✅ **Technical Stack**
- **Backend**: DeepSeek API via langchain-deepseek
- **Database**: SQLite with simple schema
- **CLI Framework**: Typer + Rich for formatting
- **Container**: Docker with persistent volumes

## 🚫 MISSING FEATURES (WHAT WE WANT)

### 🔴 **Agent Tools (HIGH PRIORITY)**
- Execute Python code ❌
- Read/write files ❌
- Run shell commands ❌
- Browse file system ❌

### 🟡 **Memory Improvements**
- Automatic cleanup (TTL) ❌
- Vector embeddings ❌
- Semantic search ❌
- Memory limits ❌

### 🟢 **Code Analysis (FUTURE)**
- Project structure analysis ❌
- Code quality suggestions ❌
- Dependency analysis ❌

## 🏗️ ARCHITECTURE OVERVIEW

### **File Structure**
```
src/alma/
├── __main__.py              # CLI entry (Typer app)
├── core/
│   ├── chat.py              # Chat loop + ChatSession class
│   ├── db.py                # MemoryDB (SQLite CRUD operations)
│   ├── llm_client.py        # LLMClient (DeepSeek API wrapper)
│   ├── memory.py            # Memory CLI commands (Typer app)
│   ├── test.py              # Testing commands (Typer app)
│   └── __init__.py          # Exports
└── utils/
    └── config.py            # Configuration loader
```

### **Data Flow**
```
User Input → CLI → Chat Loop → [Get Memories from DB] → 
Format Prompt → DeepSeek API → Response → [Save to DB] → Output
```

### **Database Schema**
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

## 🛠️ KEY COMPONENTS DETAILS

### **1. MemoryDB (db.py)**
```python
# ONLY data layer, no CLI commands
class MemoryDB:
    def add_memory(key, value, scope="global")
    def get_memory(key) -> Optional[str]
    def get_recent_memories(limit=5, scope=None) -> List[Tuple]
    def search_memories(query, limit=5) -> List[Tuple]
    # Missing: delete, cleanup, limits
```

### **2. LLMClient (llm_client.py)**
```python
class LLMClient:
    # DeepSeek configuration
    llm = ChatDeepSeek(api_key=..., model="deepseek-chat")
    
    # Core method
    def generate_response(user_message, memories, conversation_history)
    
    # System prompt (simplified):
    "Eres Alma, asistente AI con memoria. Usa memorias como contexto."
```

### **3. ChatSession (chat.py)**
```python
class ChatSession:
    # Main loop
    def chat_loop()
    
    # Memory integration
    def get_relevant_memories(user_input)
    def add_to_memory(user_input, response)
    
    # Session management
    def show_memory_status()
```

## 🐳 DOCKER COMMANDS (HOW TO RUN)

### **Setup & Development**
```bash
# Fresh start
docker-compose down -v
docker-compose build --no-cache
docker-compose run --rm alma init
docker-compose run --rm alma test all

# Run chat
docker-compose run --rm alma chat

# Test specific components
docker-compose run --rm alma test db
docker-compose run --rm alma test llm
```

### **Memory Operations**
```bash
# View memories
docker-compose run --rm alma memory list --limit 10

# Search
docker-compose run --rm alma memory search "python"

# Stats
docker-compose run --rm alma memory stats
```

## ⚠️ KNOWN ISSUES & LIMITATIONS

### **1. Memory Growth (URGENT)**
- **Problem**: No automatic cleanup, DB grows indefinitely
- **Impact**: Potential performance issues long-term
- **Solution Needed**: TTL or limit per session

### **2. No Agent Tools (MAIN GOAL)**
- **Problem**: Can only chat, cannot execute actions
- **Impact**: Limited utility for development tasks
- **Solution Needed**: Implement `execute_python()` tool first

### **3. Basic Search**
- **Problem**: Only SQL LIKE, no semantic understanding
- **Impact**: Poor memory retrieval for complex queries
- **Solution Needed**: Vector embeddings + semantic search

### **4. Error Handling**
- **Problem**: Basic try/catch, limited logging
- **Impact**: Hard to debug issues
- **Solution Needed**: Structured logging system

## 🎯 IMMEDIATE NEXT STEPS (PRIORITY ORDER)

### **PHASE 1: Stabilize MVP (NOW)**
1. Add memory limits (max 100 per session)
2. Implement cleanup command
3. Better error handling

### **PHASE 2: First Agent Tool (NEXT)**
1. Create `tools.py` module
2. Implement `execute_python(code)` function
3. Integrate with LangChain agent system
4. Add `read_file(path)` tool

### **PHASE 3: Enhanced Memory**
1. Add vector embeddings (sentence-transformers)
2. Implement semantic search
3. Add memory importance scoring

## 🔧 HOW TO ADD NEW FEATURES

### **Adding a Tool**
```python
# 1. Create/Edit: src/alma/core/tools.py
from langchain.tools import tool

@tool
def execute_python(code: str) -> str:
    """Execute Python code safely and return output"""
    # Implementation
    return result

# 2. Register in __main__.py
from .core.tools import app as tools_app
app.add_typer(tools_app, name="tools")
```

### **Modifying Memory System**
```python
# In db.py, add:
def delete_old_memories(days_old: int = 30):
    """Delete memories older than X days"""
    
def enforce_limits(max_per_scope: int = 100):
    """Keep only N memories per scope"""
```

### **Changing LLM Provider**
```python
# In llm_client.py:
# Change ChatDeepSeek to ChatOpenAI, ChatAnthropic, etc.
# Update system prompt accordingly
```

## 📁 CRITICAL FILES TO MODIFY

### **For Agent Tools:**
- `src/alma/core/tools.py` ← CREATE THIS
- `src/alma/__main__.py` ← Register tools
- `src/alma/core/chat.py` ← Integrate tools into chat

### **For Memory Improvements:**
- `src/alma/core/db.py` ← Add cleanup, limits
- `meta/schema.sql` ← Add new columns if needed

### **For Configuration:**
- `config/alma.env` ← Environment variables
- `pyproject.toml` ← Dependencies

## 🚨 COMMON ERRORS & FIXES

### **"Database not found"**
```bash
mkdir -p db
docker-compose run --rm alma init
```

### **"API Key not set"**
```bash
# Edit config/alma.env
DEEPSEEK_API_KEY=your_key_here
```

### **Container restart loop**
```bash
docker-compose down -v
docker-compose build --no-cache
```

## 🎪 PROJECT CONTEXT FOR AIs

### **When helping with Alma development:**
1. **Check AI_CONTEXT.md first** - This file!
2. **Focus on incremental changes** - Small, testable features
3. **Maintain separation of concerns** - db.py vs memory.py vs tools.py
4. **Keep it simple** - MVP mindset, avoid over-engineering

### **When suggesting improvements:**
- Consider current architecture limitations
- Suggest minimal changes first
- Include Docker commands if applicable
- Reference existing patterns from codebase

### **When debugging:**
- Ask for specific error messages
- Check if `alma test all` passes
- Verify `config/alma.env` exists
- Confirm Docker is running

## 🔮 LONG-TERM VISION
1. **Agent-first assistant** - Tools for developers
2. **Intelligent memory** - Semantic understanding of conversations  
3. **Project context awareness** - Understand codebases
4. **Multi-modal capabilities** - Images, documents, etc.

---

## 🤔 HOW TO USE THIS CONTEXT FILE

### **For AI Assistants (like me):**
1. Read this file to understand Alma's current state
2. Suggest changes that align with architecture
3. Provide code that works with existing patterns
4. Include Docker commands for testing

### **For Developers:**
1. Share this file when asking for help
2. Update it when making significant changes
3. Use it as onboarding document
4. Reference it in PR descriptions

### **Example Prompt for AIs:**
"Based on AI_CONTEXT.md, how would you implement `execute_python()` tool in Alma? Include: 
1. Code for tools.py
2. Integration with chat.py
3. Docker commands to test"

---

*This file should be updated whenever significant changes are made to Alma's architecture or capabilities.*
*Current focus: Transition from basic chat to agent with tools.*