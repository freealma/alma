
# ALMA - AI ASSISTANT CONTEXT
# Version: MVP 0.1.0 | Status: BASIC CHAT WITH MEMORY
# Last Updated: Dec 2024

## 🎯 CURRENT CAPABILITIES
- Chat interface with DeepSeek API
- Automatic conversation memory (SQLite)
- Memory search and retrieval
- Docker container with volumes

## 🚫 MISSING AGENT FEATURES (GOAL)
- Code execution tools ❌
- File system access ❌  
- Project analysis ❌
- Semantic search ❌

## 🏗️ ARCHITECTURE
```
src/alma/
├── __main__.py          # CLI (Typer): alma <command>
├── core/
│   ├── chat.py          # Interactive chat loop
│   ├── db.py            # SQLite: memories table
│   └── llm_client.py    # DeepSeek API wrapper
└── utils/config.py      # ENV: DEEPSEEK_API_KEY
```

## 🔄 DATA FLOW
User → CLI → Chat Loop → [Get Memories] → LLM → Response → [Save Memory] → User

## 💾 MEMORY SCHEMA
```sql
-- memories table
key: "{session}_{timestamp}"  -- Primary key
value: "User: ...\nAlma: ..." -- Conversation
scope: "global"|"session_id"  -- Context
updated_at: TIMESTAMP         -- Auto
```

## 🐳 DOCKER COMMANDS
```bash
docker-compose build
docker-compose run --rm alma init
docker-compose run --rm alma chat test
docker-compose run --rm alma chat chat
docker-compose run --rm alma chat memory
```

## ⚠️ KNOWN ISSUES
1. Redundant command: `alma chat chat`
2. No memory cleanup (grows indefinitely)
3. No agent tools implemented yet
4. Basic error handling

## 📌 NEXT PRIORITIES
1. Add `execute_python()` tool
2. Implement memory TTL/cleanup
3. Fix CLI structure
4. Add file reading tool

## 🛠️ QUICK DEV SETUP
1. `config/alma.env`: Add DEEPSEEK_API_KEY
2. `mkdir -p db`
3. Build: `docker-compose build`
4. Init: `docker-compose run --rm alma init`

## 🔗 KEY FILES TO MODIFY
- Tools: `src/alma/core/tools.py` (NOT YET CREATED)
- Agent: `src/alma/core/agent.py` (NOT YET CREATED)
- Memory: `src/alma/core/db.py` (EXISTS)
- Chat: `src/alma/core/chat.py` (EXISTS)