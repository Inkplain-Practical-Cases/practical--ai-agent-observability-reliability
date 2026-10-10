# AI Agent Observability & Reliability

This is an offline, synthetic FastAPI teaching case. It demonstrates trace IDs, telemetry allowlisting, provider latency spans, bounded timeouts/retries, alert thresholds and privacy-focused tests. No external provider key or real patient data is used.

Install: `python -m pip install -r requirements.txt`

Test: `python -m pytest -q`

Start server (after installing uvicorn): `uvicorn app.main:app`

Send a synthetic request: `POST /run` with JSON `{"tenant_id":"demo","message":"synthetic"}`.

Each step branch has STEP-N.md and STEP-N.crd. Main contains FINAL.crd. The current branch snapshots were created independently due to a restricted GitHub ref-update permission; code in later steps includes earlier capabilities, but Git ancestry is not a strict step-by-step chain. Automated CI verification is pending.
