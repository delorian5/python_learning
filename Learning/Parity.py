print("Программа определения четности")
number = int(input("ведите число :"))
# Определить всё
if number % 2 == 0:
    parity = "чётное"
else:
    parity = "нечётное"

if number > 100:
    cost = "больше 100"
elif number == 100:
    cost = "ровно 100"
else:
    cost = "меньше 100"

print(f"Число {number} {parity} и {cost}")