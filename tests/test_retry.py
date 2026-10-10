# Failures get a finite retry budget.
import inspect
from app.features.feature_agent.services.service_reply import service_reply
def test_retry_is_finite():
    src=inspect.getsource(service_reply)
    assert 'range(2)' in src and 'timeout=0.5' in src
