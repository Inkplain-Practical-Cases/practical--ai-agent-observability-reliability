# Handler traces one invocation and emits allowlisted observability evidence.
import uuid
from app.features.feature_agent.services.service_reply import service_reply
from app.features.feature_agent.services.service_log_event import service_log_event
async def handle_run(body):
    trace_id = uuid.uuid4().hex
    answer = await service_reply(body.message)
    service_log_event(trace_id, 'success')
    return {'trace_id': trace_id, 'result': answer}
