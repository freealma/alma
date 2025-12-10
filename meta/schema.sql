CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,
    value TEXT,
    scope TEXT DEFAULT 'global',           -- global, session, project
    type TEXT DEFAULT 'string',            -- para futuras evoluciones
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);