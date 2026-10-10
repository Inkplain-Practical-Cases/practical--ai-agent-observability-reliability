# Offline provider: no network calls, model keys or external services.
async def fake_provider(message: str) -> str:
    # Never echo the user input; this protects teaching logs and examples.
    return 'classified'
