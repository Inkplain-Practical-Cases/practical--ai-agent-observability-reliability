# Door registration: FastAPI wiring without business logic.
from fastapi import FastAPI
from app.features.feature_agent.router import router
app = FastAPI(title='Agent Reliability Lab')
app.include_router(router)
