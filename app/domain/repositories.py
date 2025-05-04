from typing import List
from .model import User

class UserRepository:
    def get_all_users(self) -> List[User]:
        raise NotImplementedError

    def get_user_by_id(self, user_id: int) -> User:
        raise NotImplementedError
