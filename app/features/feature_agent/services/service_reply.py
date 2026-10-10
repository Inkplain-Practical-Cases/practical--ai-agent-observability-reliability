# ICS service: delegates the model call through an injectable offline adapter.
from app.providers.llm.fake_provider import fake_provider
async def service_reply(message: str) -> str:
    # The fixture intentionally returns a non-sensitive constant.
    return await fake_provider(message)
