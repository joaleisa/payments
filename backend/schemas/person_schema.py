from pydantic import BaseModel


class PersonCreate(BaseModel):
    name: str

class PersonUpdateName(BaseModel):
    id: int
    name: str

class PersonResponse(BaseModel):
    id: int
    name: str