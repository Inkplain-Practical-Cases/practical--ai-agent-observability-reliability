# ICS handler: assigns a trace ID and calls the business service.
import uuid
from app.features.feature_agent.services.service_reply import service_reply
async def handle_run(body):
    # Trace IDs are server-generated, never accepted from an untrusted caller.
    trace_id = uuid.uuid4().hex
    answer = await service_reply(body.message)
    return {'trace_id': trace_id, 'result': answer}
