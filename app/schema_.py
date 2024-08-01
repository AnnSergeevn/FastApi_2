from __future__ import annotations

import datetime
from typing import Literal
from pydantic import BaseModel


class OkResponse(BaseModel):
    status: Literal['ok']


# class GetTodoResponse(BaseModel):
#     id: int
#     name: str
#     important: bool
#     done: bool
#     start_time: datetime.datetime
#     finish_time: datetime.datetime | None
#
#
# class CreateTodoRequest(BaseModel):
#     name: str
#     important: bool = False
#
#
# class CreateTodoResponse(BaseModel):
#     id: int


class GetAdvResponse(BaseModel):
    id: int
    heading: str
    description: str
    price: int
    date_of_creation: datetime.datetime
    user: str


class CreateAdvRequest(BaseModel):
    heading: str
    description: str
    price: int
    user: str


class CreateAdvResponse(BaseModel):
    id: int



class UpdateAdvRequest(BaseModel):
    heading: str | None = None
    description: str | None = None
    price: int | None = None


class UpdateAdvResponse(CreateAdvResponse):
    pass