from typing import List
from app.domain.model import User
from app.domain.repositories import UserRepository

class UserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self) -> List[User]:
        return self.repository.get_all_users()

    def get_user(self, user_id: int) -> User:
        return self.repository.get_user_by_id(user_id)
