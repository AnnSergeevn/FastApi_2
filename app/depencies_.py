from fastapi import Depends
from models import Session
from typing import Annotated

async def get_db_session():
    async with Session() as session:
        yield session


SessionDependency = Annotated[Session, Depends(get_db_session)]
