"""Persist minimal, redacted agent trace telemetry to relational SQLite tables.

Each event references its trace and deliberately excludes raw prompts and replies.
"""
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

def provider_store_event(trace_id: str, outcome: str, duration_ms: float, db_path: str | None = None) -> None:
    """Save a redacted trace event with enforced foreign-key integrity."""
    location = db_path or os.getenv("INKPLAIN_OBSERVABILITY_DB", "agent_events.sqlite3")
    Path(location).parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(location) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("""CREATE TABLE IF NOT EXISTS agent_traces (
            trace_id TEXT PRIMARY KEY,
            first_seen_at TEXT NOT NULL
        )""")
        connection.execute("""CREATE TABLE IF NOT EXISTS agent_events (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            trace_id TEXT NOT NULL REFERENCES agent_traces(trace_id),
            outcome TEXT NOT NULL,
            duration_ms REAL NOT NULL,
            redacted INTEGER NOT NULL,
            recorded_at TEXT NOT NULL
        )""")
        connection.execute("INSERT OR IGNORE INTO agent_traces (trace_id, first_seen_at) VALUES (?, ?)", (trace_id, now))
        connection.execute("INSERT INTO agent_events (trace_id, outcome, duration_ms, redacted, recorded_at) VALUES (?, ?, ?, ?, ?)",
                           (trace_id, outcome, round(duration_ms, 2), 1, now))
