from app.domain.repositories import UserRepository
from app.domain.model import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = [
            User(id=1, name="Alice", email="alice@example.com"),
            User(id=2, name="Bob", email="bob@example.com"),
        ]

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id: int):
        for user in self.users:
            if user.id == user_id:
                return user
        raise ValueError("User not found")
