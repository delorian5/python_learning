def load_shop(filename):
    shopping = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    shopping.append(line)
    except FileNotFoundError:
        pass
    return shopping
def save_shop(shopping, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in shopping:
            f.write(f"{item}\n")
def choice_item():
    filename = "shop.txt"
    stop = "Всё"
    shopping = load_shop(filename)
    while True:
        item = input("Выбери товар: ")
        if item != stop:
            shopping.append(item)
        else:
            print("Конец покупок.")
            save_shop(shopping, filename)
            break
    return shopping
def main():
    print("Выберите товар и напишите <Всё> Когда закончите")
    shopping = choice_item()
    if shopping:
        print(f"Кол-во покупок: {len(shopping)}")
        print(f"Список покупок: {shopping}")
        print(f"Первый: {shopping[0]}")
        print(f"Последний: {shopping[-1]}")
    else:
        print("Список пуст")
main()