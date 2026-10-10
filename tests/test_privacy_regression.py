# Response must not reflect synthetic credentials.
from fastapi.testclient import TestClient
from app.main import app
def test_secret_not_reflected():
    secret='synthetic-demo-secret'
    r=TestClient(app).post('/run',json={'tenant_id':'demo','message':secret})
    assert r.status_code==200 and secret not in r.text

def test_validation():
    assert TestClient(app).post('/run',json={'tenant_id':'demo'}).status_code==422
