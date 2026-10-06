import sqlite3

class Contacts:
    def __init__(self, db_name="contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                phone TEXT
            )
        """)
        self.conn.commit()
    def add(self, name, phone):
        try:
            self.cursor.execute(
                "INSERT INTO contacts (name, phone) VALUES (?, ?)",
                (name, phone)
            )
            self.conn.commit()
            print("Контакт добавлен.")
        except sqlite3.IntegrityError:
            print("Такой контакт уже есть.")
    def find(self, name):
        self.cursor.execute("SELECT phone FROM contacts WHERE name = ?", (name,))
        result = self.cursor.fetchone()
        if result:
            print(f"{name}: {result[0]}")
        else:
            print("Не найден.")
    def show_all(self):
        self.cursor.execute("SELECT name, phone FROM contacts")
        rows = self.cursor.fetchall()
        if not rows:
            print("Список пуст.")
            return
        for name, phone in rows:
            print(f"{name}: {phone}")
    def delete(self, name):
        self.cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print("Удалено.")
        else:
            print("Не найден.")
    def update(self, name, phone):
        self.cursor.execute("UPDATE contacts SET phone = ? WHERE name = ?", (phone, name))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print("Обновлено.")
        else:
            print("Не найден.")
    def close(self):
        self.conn.close()
def main():
    book = Contacts()
    while True:
        print("1. Добавить  2. Найти  3. Все  4. Удалить  5. Обновить  6. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            name = input("Имя: ")
            phone = input("Номер: ")
            book.add(name, phone)
        elif choice == "2":
            name = input("Кого найти? ")
            book.find(name)
        elif choice == "3":
            book.show_all()
        elif choice == "4":
            name = input("Кого удалить? ")
            book.delete(name)
        elif choice == "5":
            name = input("Кого обновить? ")
            phone = input("Новый номер: ")
            book.update(name, phone)
        elif choice == "6":
            book.close()
            print("Пока")
            break
        else:
            print("Неверный выбор.")
main()