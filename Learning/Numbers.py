print("Сумма и среднее")
block = []
for i in range(5):
    num = int(input(f"Введите число {i + 1}: "))
    block.append(num)
# Второй этап
print(f"Сумма: {sum(block)}")
print(f"Среднее: {sum(block) / len(block)}")
print(f"Максимум: {max(block)}")
print(f"Минимум: {min(block)}")