CREATE TABLE IF NOT EXISTS events (
    event_id TEXT PRIMARY KEY,
    type TEXT,
    user_id TEXT,
    repo TEXT,
    timestamp TIMESTAMP
);
