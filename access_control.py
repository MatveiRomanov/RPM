class User:
    def __init__(self, user_id, name, role="user"):
        self.user_id = user_id
        self.name = name
        self.role = role


current_user = None


def set_current_user(user):
    global current_user
    current_user = user


def require_admin(func):
    def wrapper(user_id):
        if current_user is None:
            raise PermissionError("Пользователь не авторизован")
        if current_user.role != "admin":
            raise PermissionError(f"Доступ запрещен. Требуются права администратора. Текущая роль: {current_user.role}")
        return func(user_id)

    return wrapper


@require_admin
def delete_user(user_id):
    return f"Пользователь с ID {user_id} удален"
