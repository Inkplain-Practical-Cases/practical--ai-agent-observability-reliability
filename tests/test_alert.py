# A meaningful error-rate crossing raises an alert.
from app.features.feature_agent.services.service_alert import service_alert
def test_threshold():
    assert service_alert(10,3)['alert']
    assert not service_alert(9,9)['alert']
