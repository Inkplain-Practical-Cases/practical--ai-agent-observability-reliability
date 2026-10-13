"""Emit allowlisted telemetry and persist the same redacted fields for audit."""
import json
import logging
from app.features.feature_agent.providers.provider_store_event import provider_store_event

logger = logging.getLogger("agent.safe_events")

def service_log_event(trace_id: str, outcome: str, duration_ms: float = 0.0):
    """Write safe structured telemetry without request or response contents."""
    event = {"trace_id": trace_id, "outcome": outcome, "duration_ms": round(duration_ms, 2), "redacted": True}
    logger.info(json.dumps(event))
    provider_store_event(trace_id, outcome, duration_ms)
    return event
