import sqlite3
from datetime import datetime
from typing import List, Optional, Tuple
from pathlib import Path
from ..utils.config import config

class MemoryDB:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or config.DATABASE_URL.replace("sqlite:///", "")
        self.init_db()
    
    def init_db(self):
        """Initialize database with schema"""
        schema_path = Path(__file__).parent.parent.parent.parent / "meta" / "schema.sql"
        
        with sqlite3.connect(self.db_path) as conn:
            # Create table if not exists
            conn.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key TEXT UNIQUE,
                    value TEXT,
                    scope TEXT DEFAULT 'global',
                    type TEXT DEFAULT 'string',
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
    
    def add_memory(self, key: str, value: str, scope: str = "global") -> bool:
        """Add or update a memory"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    INSERT OR REPLACE INTO memories (key, value, scope, updated_at)
                    VALUES (?, ?, ?, ?)
                """, (key, value, scope, datetime.now().isoformat()))
                conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
    
    def get_memory(self, key: str) -> Optional[str]:
        """Get a memory by key"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(
                    "SELECT value FROM memories WHERE key = ?",
                    (key,)
                )
                result = cursor.fetchone()
                return result[0] if result else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
    
    def get_recent_memories(self, limit: int = 5, scope: str = None) -> List[Tuple]:
        """Get recent memories, optionally filtered by scope"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                if scope:
                    cursor = conn.execute("""
                        SELECT key, value, scope, updated_at 
                        FROM memories 
                        WHERE scope = ? 
                        ORDER BY updated_at DESC 
                        LIMIT ?
                    """, (scope, limit))
                else:
                    cursor = conn.execute("""
                        SELECT key, value, scope, updated_at 
                        FROM memories 
                        ORDER BY updated_at DESC 
                        LIMIT ?
                    """, (limit,))
                
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def search_memories(self, query: str, limit: int = 5) -> List[Tuple]:
        """Search memories by content"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("""
                    SELECT key, value, scope, updated_at 
                    FROM memories 
                    WHERE value LIKE ? 
                    ORDER BY updated_at DESC 
                    LIMIT ?
                """, (f"%{query}%", limit))
                
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

# Singleton instance
memory_db = MemoryDB()