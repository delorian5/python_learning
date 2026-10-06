print("Поисковик максимального числа")
block = []
for i in range(5):
    num = int(input(f"Введите число {i + 1}: "))
    block.append(num)
# Считаем максимум
maximum = block[0]
for n in block:
    if n > maximum:
        maximum = n
# Считаем минимум
minimum = block[0]
for n in block:
    if n < minimum:
        minimum = n
# Считаем Сумму
summon = 0
for n in block:
    summon += n
# Считаем среднее
par = summon / len(block)
# Показываем
print(f"Большее: {maximum}")
print(f"Минимум: {minimum}")
print(f"Сумма: {summon}")
print(f"Среднее: {par}")