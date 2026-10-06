import sqlite3

class Todos:
    def __init__(self, db_name="todos.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                todo TEXT
            )
        """)
        self.conn.commit()
    def add(self):
        todo = input("Введите дело: ")
        self.cursor.execute("INSERT INTO todos (todo) VALUES (?)", (todo,))
        self.conn.commit()
        print("Дело добавлено.")
    def remove(self):
        try:
            id = int(input("Введите номер: "))
        except ValueError:
            print("Это не число")
            return
        self.cursor.execute("DELETE FROM todos WHERE id = ?", (id,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print("Дело удалено.")
        else:
            print("Дело не найдено.")
    def show(self):
        self.cursor.execute("SELECT id, todo FROM todos")
        todos = self.cursor.fetchall()
        if not todos:
            print("Дел нет.")
            return
        for id, todo in todos:
            print(f"{id}. {todo}")
    def close(self):
        self.conn.close()
def main():
    todo = Todos()
    print("Список дел.")
    while True:
        print("1. Добавить. 2. Удалить. 3. Посмотреть. 4. Выход.")
        choice = input("Выбор: ")
        if choice == "1":
            todo.add()
        elif choice == "2":
            todo.remove()
        elif choice == "3":
            todo.show()
        elif choice == "4":
            todo.close()
            print("Дела сохранены.")
            break
        else:
            print("Неверный выбор.")
main()