from pydantic import BaseModel


class PersonCreate(BaseModel):
    name: str
    user_id: int

class PersonUpdateName(BaseModel):
    # id: int
    name: str
    # user_id: int

class PersonResponse(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        form_attributes = True #todo: what's this for?