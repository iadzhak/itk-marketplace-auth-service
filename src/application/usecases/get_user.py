from src.application.ports.uow import UnitOfWork
from src.application.ports.usecases import GetUserPort
from src.domain.entities import User
from src.application.exceptions import UserNotFoundError


class GetUser(GetUserPort):
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

    async def execute(self, user_id: int) -> User:
        async with self._uow:
            user = await self._uow.users.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f'Пользователь с id {user_id} не найден')
        return user
