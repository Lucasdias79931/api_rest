from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Status(str, Enum):
    active = "active"
    inactive = "inactive"


class PersonDTO(BaseModel):
    person_id: Optional[str] = None
    name: str
    status: Status = Status.active
