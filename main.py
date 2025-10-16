from database_connection import *

def main():
    db1 = DatabaseConnection()
    db1.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMERY KEY, name TEXT)")
    db1.execute("INSERT INTO users (name) VALUES (?)", ("Матвей",))
    print("Добавлен пользователь Матвей")

    db2 = DatabaseConnection()
    db2.execute("SELECT * FROM users")
    print("Содержимое таблицы:", db2.fetchall())

    print(db1 is db2)

    db2.close()

if __name__ == "__main__":
    main()