import datetime

import fastapi
from models import Session, Todo, Advertisement
import schema
from lifespan import lifespan
from depencies import SessionDependency
from crud import add_item, get_item
from typing import Optional

app = fastapi.FastAPI(
    title="Todo API",
    version='0.0.1',
    description='some api',
    lifespan=lifespan
)

# @app.get('/v1/todo/{todo_id}/', response_model=schema.GetTodoResponse)
# async def get_todo(session: SessionDependency, todo_id: int):
#     todo = await get_item(session, Todo, todo_id)
#     return todo.dict
#
# @app.post('/v1/todo/', response_model=schema.CreateTodoResponse,
#           summary="Create new todo item")
# async def create_todo(
#         todo_json: schema.CreateTodoRequest, session: SessionDependency):
#     todo = Todo(**todo_json.dict())
#     todo = await add_item(session, todo)
#     return {'id': todo.id}
#
#
# @app.patch('/v1/todo/{todo_id}/',
#            response_model=schema.UpdateTodoResponse,
#          )
# async def update_todo(todo_json: schema.UpdateTodoRequest, session: SessionDependency, todo_id: int):
#     todo = await get_item(session, Todo, todo_id)
#     todo_dict = todo_json.dict(exclude_unset=True)
#     for field, valued in todo_dict.items():
#         setattr(todo, field, valued)
#     if todo_json.done:
#         todo.finish_time = datetime.datetime.utcnow()
#     todo = await add_item(session, todo)
#     return todo.dict
#
#
# @app.delete('/v1/todo/{todo_id}/', response_model=schema.OkResponse)
# async def delete_todo(todo_id: int, session: SessionDependency):
#     todo = await get_item(session, Todo, todo_id)
#     await session.delete(todo)
#     await session.commit()
#     return {'status': 'ok'}


@app.get('/v1/adv/{adv_id}/', response_model=schema.GetAdvResponse)
async def get_adv(session: SessionDependency, adv_id: int):
    adv = await get_item(session, Advertisement, adv_id)
    return adv.dict


@app.get("/v1/adv/")
async def read_root(param1: Optional[str] = None):
    url = f'http://127.0.0.1:8000/v1/adv/{param1}'
    return {'url': str(url), "param1": str(param1)}


@app.post('/v1/adv/', response_model=schema.CreateAdvResponse,
          summary="Create new todo item")
async def create_adv(
        adv_json: schema.CreateAdvRequest,  session: SessionDependency):
    adv = Advertisement(**adv_json.dict())
    adv = await add_item(session, adv)
    return {'id': adv.id}


@app.patch('/v1/adv/{adv_id}/',
           response_model=schema.UpdateAdvResponse)
async def update_adv(adv_json: schema.UpdateAdvRequest, session: SessionDependency, adv_id: int):
    adv = await get_item(session, Advertisement, adv_id)
    adv_dict = adv_json.dict(exclude_unset=True)
    for field, valued in adv_dict.items():
        setattr(adv, field, valued)
    adv = await add_item(session, adv)
    return adv.dict


@app.delete('/v1/adv/{adv_id}/', response_model=schema.OkResponse)
async def delete_adv(adv_id: int, session: SessionDependency):
    adv = await get_item(session, Advertisement, adv_id)
    await session.delete(adv)
    await session.commit()
    return {'status': 'ok'}
