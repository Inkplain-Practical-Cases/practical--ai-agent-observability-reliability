# Service measures monotonic provider duration and emits a redacted span.
import time
from app.providers.llm.fake_provider import fake_provider
from app.features.feature_agent.services.service_log_event import service_log_event
async def service_reply(message: str) -> str:
    started=time.perf_counter()
    try:
        result=await fake_provider(message)
        service_log_event('provider','success',(time.perf_counter()-started)*1000)
        return result
    except Exception:
        service_log_event('provider','error',(time.perf_counter()-started)*1000)
        raise
