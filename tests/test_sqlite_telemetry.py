"""Check that persisted telemetry excludes sensitive text and keeps trace FK."""
import sqlite3
from app.features.feature_agent.providers.provider_store_event import provider_store_event

def test_trace_event_database(tmp_path):
    path = str(tmp_path / "safe.sqlite3")
    provider_store_event("trace-test", "success", 12.5, path)
    provider_store_event("trace-test", "retryable_failure", 4.0, path)
    with sqlite3.connect(path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM agent_traces").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM agent_events").fetchone()[0] == 2
        assert connection.execute("PRAGMA foreign_key_check").fetchall() == []
