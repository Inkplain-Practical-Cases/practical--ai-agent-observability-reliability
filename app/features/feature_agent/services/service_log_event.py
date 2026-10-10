# Safe event service: emit only allowlisted telemetry fields.
import json
import logging
logger = logging.getLogger('agent.safe_events')
def service_log_event(trace_id: str, outcome: str, duration_ms: float = 0.0):
    event = {'trace_id': trace_id, 'outcome': outcome, 'duration_ms': round(duration_ms, 2), 'redacted': True}
    logger.info(json.dumps(event))
    return event
