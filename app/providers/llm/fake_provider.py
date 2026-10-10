# Offline deterministic model adapter; never reflects sensitive inputs.
async def fake_provider(message: str) -> str:
    return 'classified'
