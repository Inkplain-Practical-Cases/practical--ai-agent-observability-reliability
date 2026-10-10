# ICS door: accepts a validated request and delegates without business logic.
from fastapi import APIRouter
from app.features.feature_agent.handlers.handle_run import handle_run
from app.features.feature_agent.schemas.request_schema import RunRequest
router = APIRouter()
@router.post('/run')
async def run(body: RunRequest):
    # The orchestration handler owns request processing.
    return await handle_run(body)
