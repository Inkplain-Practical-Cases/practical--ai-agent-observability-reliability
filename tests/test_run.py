# The successful agent request has a generated trace ID and no raw prompt.
from fastapi.testclient import TestClient
from app.main import app
def test_run():
    r = TestClient(app).post('/run', json={'tenant_id':'sample','message':'synthetic'})
    assert r.status_code == 200 and len(r.json()['trace_id']) == 32
    assert r.json()['result'] == 'classified'
