# Provider duration must remain numeric.
from app.features.feature_agent.services.service_log_event import service_log_event
def test_latency():
    assert service_log_event('provider','success',8.12)['duration_ms']==8.12
