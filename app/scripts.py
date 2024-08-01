import asyncio

from auth import hash_password
from models import Right, Role, Session, User, Advertisement


async def create_admin_user(
    session: Session,
    username: str,
    password: str,
) -> None:
    write_rights = [
        Right(
            model=model._model,
            write=True,
            read=False,
            only_own=False,
        )
        for model in (Right, Role, User, Advertisement)
    ]
    read_rights = [
        Right(
            model=model._model,
            write=False,
            read=True,
            only_own=False,
        )
        for model in (Right, Role, User, Advertisement)
    ]
    rights = [*write_rights, *read_rights]
    role = Role(name="admin", rights=rights)
    user = User(name=username, password=hash_password(password), roles=[role])
    session.add_all([*rights, role, user])
    await session.commit()


async def create_user_role(session: Session) -> None:
    rights = []
    for wr in True, False:
        for model in (User, Advertisement):
            rights.append(
                Right(
                    model=model._model,
                    write=wr,
                    read=not wr,
                    only_own=True,
                )
            )
    role = Role(name="user", rights=rights)
    session.add_all([*rights, role])
    await session.commit()

async def main():
    async with Session() as session:
        await create_admin_user(session, username = "admin", password = "admin")
        await create_user_role(session)

if __name__ == "__main__":
    asyncio.run(main())