# Tests the thinnest successful slice and validates server-originated trace IDs.
from fastapi.testclient import TestClient
from app.main import app

def test_run_has_trace_id():
    response = TestClient(app).post('/run', json={'tenant_id':'synthetic','message':'fixture'})
    assert response.status_code == 200
    assert len(response.json()['trace_id']) == 32
    assert response.json()['result'] == 'classified'
