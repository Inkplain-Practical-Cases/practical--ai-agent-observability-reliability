# Keep confidential inputs out of the structured event contract.
from app.features.feature_agent.services.service_log_event import service_log_event
def test_event_allowlist():
    assert set(service_log_event('id','success')) == {'trace_id','outcome','duration_ms','redacted'}
