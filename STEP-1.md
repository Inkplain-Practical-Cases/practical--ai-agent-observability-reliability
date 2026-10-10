# STEP-1 — Trace API request boundaries

## Goal
Trace API request boundaries. This cumulative step adds isolated code and regression checks without collecting raw user prompts in telemetry.

## Run
`pip install -r requirements.txt && pytest -q`

## Source
Read the component inventory in STEP-1.crd and the commented Python modules in `app/`.

## Failure scenario
A malformed request is rejected with HTTP 422. No secrets or raw prompts may appear in safe telemetry.
