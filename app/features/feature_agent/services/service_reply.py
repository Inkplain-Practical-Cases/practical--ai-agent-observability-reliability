# Offline model reply delegates to the injected provider module.
from app.providers.llm.fake_provider import fake_provider
async def service_reply(message:str)->str:
    return await fake_provider(message)
