from pydantic import BaseModel, Field

class TaskCreate2(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    done: bool = False

class TaskUpdate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    done: bool

class TaskOut2(BaseModel):
    id: int
    title: str
    done: bool

class TaskOut(BaseModel):
    id: int
    title: str
    done: bool

class TaskPatch(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    done: bool | None = None


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    done: bool = False

