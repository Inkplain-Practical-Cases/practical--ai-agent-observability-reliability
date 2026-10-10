# Pydantic schema validates synthetic input without storing it.
from pydantic import BaseModel, Field
class RunRequest(BaseModel):
    tenant_id: str = Field(min_length=1, max_length=40)
    message: str = Field(min_length=1, max_length=500)
