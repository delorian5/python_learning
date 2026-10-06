def load_todos(filename):
    todos = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    todos.append(line)
    except FileNotFoundError:
        pass
    return todos
def save_todos(filename, todos):
    with open(filename, "w", encoding="utf-8") as f:
        for todo in todos:
            f.write(f"{todo}\n")
def add_todos(todos):
    todo = input("Введите дело: ")
    todos.append(todo)
    print("Дело добавлено.")
def remove_todos(todos):
    try:
        todo = int(input("Введите номер: "))
        if 1 <= todo <= len(todos):
            del todos[todo - 1]
            print("Дело удалено.")
        else:
            print("Дело не найдено.")
    except ValueError:
        print("Это не номер.")
def show_all(todos):
    if not todos:
        print("Дела не найдены.")
        return
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo}")
def main():
    filename = "Todos2.txt"
    todos = load_todos(filename)
    print("Список дел.")
    while True:
        print("1. Добавить. 2. Удалить. 3. Посмотреть. 4. Выход.")
        choice = input("Выбор: ")
        if choice == "1":
            add_todos(todos)
        elif choice == "2":
            remove_todos(todos)
        elif choice == "3":
            show_all(todos)
        elif choice == "4":
            save_todos(filename, todos)
            print("Данные сохранены.")
            break
        else:
            print("Неверный выбор.")
main()