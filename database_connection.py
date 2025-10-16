import sqlite3

class DatabaseConnection:
    _instance = None

    def __new__(cls, db_name="database_for_lab.db"):
        if cls._instance is None:
            print("Создание нового подключения к базе данных")
            cls._instance = super().__new__(cls)
            cls._instance.db_name = db_name
            cls._instance.connection = sqlite3.connect(db_name)
            cls._instance.cursor = cls._instance.connection.cursor()
        else:
            print("Используется существующее подключение")
        return cls._instance

    def execute(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
        print("Подключение закрыто")
        DatabaseConnection._instance = None

