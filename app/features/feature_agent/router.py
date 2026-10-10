# HTTP door delegates each validated request to the handler.
from fastapi import APIRouter
from app.features.feature_agent.handlers.handle_run import handle_run
from app.features.feature_agent.schemas.request_schema import RunRequest
router = APIRouter()
@router.post('/run')
async def run(body: RunRequest):
    return await handle_run(body)
