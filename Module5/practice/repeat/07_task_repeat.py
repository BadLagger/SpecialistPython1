
# Иван кладет в банк x рублей под a процентов годовых на n лет. Напишите функцию, которая возвращает число -
# сколько денег получит Иван в результате.

def deposit(x, a, n):
    return x + x * a / 100 * n

print(deposit(300000, 3, 3))
