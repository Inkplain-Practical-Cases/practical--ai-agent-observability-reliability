# STEP-6 — Test reliability and privacy regressions

## Goal
Test reliability and privacy regressions.

## Run and check
`pip install -r requirements.txt && pytest -q`

## Learning source
Inspect the annotated Python functions and STEP-6.crd component inventory.

## Database (Entity) Relations
STEP-6 persists redacted telemetry in SQLite, in agent_traces and agent_events with agent_events.trace_id referring to agent_traces.trace_id. No prompt or answer text is saved. Set INKPLAIN_OBSERVABILITY_DB to change the location. View STEP-6.erd and the corresponding .inkp ERD tab.
