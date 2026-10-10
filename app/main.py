# ICS door registration: FastAPI app only wires the case router.
from fastapi import FastAPI
from app.features.feature_agent.router import router
app = FastAPI(title='Agent Reliability Lab')
app.include_router(router)
