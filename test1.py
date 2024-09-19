### Решение из задания
# Плюсы:
# Просто и легко читается
# Минусы:
# Выполняется медленней, чем битовая операция
def isEven(value):
    return value % 2 == 0

### Моя версия
# Плюсы:
# Выполняется быстрее, чем арифметическая операция
# Минусы:
# Менее читабельно и понятно
def is_even(value):
    return (value & 1) == 0

