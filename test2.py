## Реализация на основе использования deque:
# Плюсы:
# Код легче воспринимается, лаконичен
# Быстро выполняется
# Добавление элемента происходит за O(1) и удаление самого старого элемента —
# тоже O(1), что делает его более эффективным
# Минусы:
# Нужно импортировать модуль

from collections import deque

class CircularBufferFIFO:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def add(self, item):
        self.buffer.append(item)

    def get(self):
        return list(self.buffer)

    def __str__(self):
        return str(self.get())
