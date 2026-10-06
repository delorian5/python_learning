print("Калькулятор")
def add(a, b):
    return a + b
def divide(a, b):
    if b == 0:
        return None
    return a / b
def multiply(a, b):
    return a * b
def substract(a, b):
    return a - b

a = float(input("Первое число: "))
b = float(input("Второе число: "))

print(f"Сумма: {add(a, b)}")
print(f"Разность: {substract(a, b)}")
print(f"Произведение: {multiply(a, b)}")
results = divide(a, b)
if results is None:
    print("На ноль делить нельзя")
else:
    print(f"Деление: {results}")