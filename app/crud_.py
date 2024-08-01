from models import Session, Todo, Advertisement
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import typing


async def add_item(session: Session, item: Advertisement):
    session.add(item)
    try:
        await session.commit()
    except IntegrityError as err:
        if err.orig.pgcode == "23505":
            raise HTTPException(status_code=409, detail='Item already exist')
        raise err
    return item


async def get_item(session: Session, orm_cls: typing.Type[Advertisement], item_id: int):
    orm_obj = await session.get(orm_cls, item_id)
    if orm_obj is None:
        raise HTTPException(
            status_code=404,
            detail=f'{orm_cls.__name__} not found'
        )
    return orm_obj

# async def get_item_qs(session: Session, orm_cls: typing.Type[Advertisement], param1: str):
#     orm_obj = await session.get(orm_cls, param1)
#     if orm_obj is None:
#         raise HTTPException(
#             status_code=404,
#             detail=f'{orm_cls.__name__} not found'
#         )
#     return orm_obj