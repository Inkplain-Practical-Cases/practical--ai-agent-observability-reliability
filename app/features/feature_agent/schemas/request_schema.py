# Input boundary: Pydantic validates each synthetic user request.
from pydantic import BaseModel, Field
class RunRequest(BaseModel):
    tenant_id: str = Field(min_length=1, max_length=40)
    message: str = Field(min_length=1, max_length=500)
