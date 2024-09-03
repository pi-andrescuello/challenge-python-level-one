from pydantic import BaseModel
from typing import Optional

class auth_schema(BaseModel):
    id: Optional[int]
    user_name: str
    password: str
