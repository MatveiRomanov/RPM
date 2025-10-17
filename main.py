from users_system import (
    UserFactory,
    demonstrate_user_system,
    check_user_permissions
)


def main():
    print("ЗАПУСК СИСТЕМЫ УПРАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯМИ\n")

    demonstrate_user_system()

    print("\n=== ПРОВЕРКА КОНКРЕТНЫХ ТИПОВ ПОЛЬЗОВАТЕЛЕЙ ===")

    check_user_permissions(UserFactory.USER_TYPE_ADMIN, "test_admin", "admin@test.com")
    check_user_permissions(UserFactory.USER_TYPE_MANAGER, "test_manager", "manager@test.com")
    check_user_permissions(UserFactory.USER_TYPE_GUEST, "test_guest", "guest@test.com")

    print("\n=== ДОПОЛНИТЕЛЬНОЕ ТЕСТИРОВАНИЕ ===")

    admin = UserFactory.create_user(UserFactory.USER_TYPE_ADMIN, "john", "john@company.com")
    print(f"Создан администратор: {admin.username}")
    print(f"Email: {admin.email}")
    print(f"Права: {admin.get_permissions()}")

    print("\n=== ПРОВЕРКА ОШИБОК ===")
    try:
        invalid_user = UserFactory.create_user("superuser", "error", "error@mail.com")
    except ValueError as e:
        print(f"Ошибка перехвачена: {e}")

    print("\nДемонстрация завершена!")


if __name__ == "__main__":
    main()