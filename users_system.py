from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    @abstractmethod
    def get_permissions(self) -> list:
        pass

    def get_info(self) -> str:
        return f"Пользователь: {self.username} ({self.email})"


class AdminUser(User):

    def get_permissions(self) -> list:
        return [
            "create_users",
            "delete_users",
            "manage_permissions",
            "view_all_data",
            "system_configuration",
            "backup_restore"
        ]

    def __str__(self):
        return f"Администратор: {self.username}"


class ManagerUser(User):

    def get_permissions(self) -> list:
        return [
            "create_content",
            "edit_content",
            "delete_content",
            "view_reports",
            "manage_users"
        ]

    def __str__(self):
        return f"Менеджер: {self.username}"


class GuestUser(User):

    def get_permissions(self) -> list:
        return [
            "view_public_content",
            "search_content",
            "register_account"
        ]

    def __str__(self):
        return f"Гость: {self.username}"


class UserFactory:

    USER_TYPE_ADMIN = "admin"
    USER_TYPE_MANAGER = "manager"
    USER_TYPE_GUEST = "guest"

    @staticmethod
    def create_user(user_type: str, username: str, email: str) -> User:

        if user_type == UserFactory.USER_TYPE_ADMIN:
            return AdminUser(username, email)
        elif user_type == UserFactory.USER_TYPE_MANAGER:
            return ManagerUser(username, email)
        elif user_type == UserFactory.USER_TYPE_GUEST:
            return GuestUser(username, email)
        else:
            raise ValueError(f"Неизвестный тип пользователя: {user_type}")


def demonstrate_user_system():
    print("=== СИСТЕМА УПРАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯМИ ===\n")

    users = [
        UserFactory.create_user(UserFactory.USER_TYPE_ADMIN, "alex_admin", "alex@company.com"),
        UserFactory.create_user(UserFactory.USER_TYPE_MANAGER, "maria_manager", "maria@company.com"),
        UserFactory.create_user(UserFactory.USER_TYPE_GUEST, "ivan_guest", "ivan@company.com"),
        UserFactory.create_user(UserFactory.USER_TYPE_ADMIN, "sophia_admin", "sophia@company.com")
    ]

    for user in users:
        print(f"{user}")
        print(f"Информация: {user.get_info()}")
        print(f"Права доступа: {', '.join(user.get_permissions())}")
        print("-" * 50)


def check_user_permissions(user_type: str, username: str, email: str):
    user = UserFactory.create_user(user_type, username, email)
    print(f"Создан: {user}")
    print(f"Права: {user.get_permissions()}")
    print(f"Количество прав: {len(user.get_permissions())}")
    print("=" * 30)