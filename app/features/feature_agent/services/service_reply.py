# Service enforces finite wait and retry budgets while preserving cancellation.
import asyncio
import time
from app.providers.llm.fake_provider import fake_provider
from app.features.feature_agent.services.service_log_event import service_log_event
async def service_reply(message: str) -> str:
    for attempt in range(2):
        started=time.perf_counter()
        try:
            result=await asyncio.wait_for(fake_provider(message),timeout=0.5)
            service_log_event('provider','success',(time.perf_counter()-started)*1000)
            return result
        except (TimeoutError,ConnectionError):
            service_log_event('provider','retryable_failure',(time.perf_counter()-started)*1000)
            if attempt==1:
                raise
    raise RuntimeError('unreachable')
